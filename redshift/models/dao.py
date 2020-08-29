from functools import wraps
from typing import List, NoReturn

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session

from config import Config
from redshift.models.base import Base
from redshift.models.tables import Users, Venue, Category, Date, Event, \
    Listing, Sales

__all__ = ['Dao']


def _commit(fn):
    @wraps(fn)
    def helper(*args, **kwargs):
        res = fn(*args, **kwargs)
        args[0].commit()
        return res

    return helper


class SingletonMeta(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instance


class Dao(metaclass=SingletonMeta):
    __slots__ = ['_engine']

    def __init__(self, echo=False):
        self._engine: Engine = create_engine(
            f'redshift+psycopg2://{Config.RS_USR}:{Config.RS_PWD}'
            f'@{Config.RS_HOST}:{Config.RS_PORT}/{Config.RS_DB}',
            echo=echo,
            echo_pool=echo,
            pool_size=20,
            max_overflow=5,
            pool_recycle=3600,
            pool_timeout=30)

    def _get_session(self) -> Session:
        _Session = sessionmaker(bind=self._engine)
        return _Session()

    def reset_engine(self) -> NoReturn:
        """Dispose of the connection pool

        """
        self._engine.dispose()

    def create_all(self) -> NoReturn:
        Base.metadata.create_all(self._engine)

    def drop_all(self) -> NoReturn:
        """drop all tables defined in `redshift.tables`

        there's no native `DROP TABLE ... CASCADE ...` method and tables should
        be dropped from the leaves of the dependency tree back to the root
        """
        tables = (Sales, Listing, Event, Users, Venue, Category, Date)
        list(
            map(
                lambda tb: tb.__table__.drop(bind=self._engine,
                                             checkfirst=True), tables))

    def all_tables(self) -> List[str]:
        return self._engine.table_names()

    def all_users(self) -> List[Users]:
        @_commit
        def _all_users(session: Session):
            return session.query(Users).all()

        return _all_users(self._get_session())
