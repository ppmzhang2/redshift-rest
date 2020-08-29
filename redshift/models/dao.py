from functools import wraps

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from config import Config
from redshift.models.base import Base
from redshift.models.tables import Users

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
        self._engine = create_engine(
            f'redshift+psycopg2://{Config.RS_USR}:{Config.RS_PWD}'
            f'@{Config.RS_HOST}:{Config.RS_PORT}/{Config.RS_DB}',
            echo=echo,
            echo_pool=echo,
            pool_size=20,
            max_overflow=5,
            pool_recycle=3600,
            pool_timeout=30)

    def _get_session(self):
        _Session = sessionmaker(bind=self._engine)
        return _Session()

    def reset_engine(self):
        """Dispose of the connection pool

        """
        self._engine.dispose()

    def create_all(self):
        Base.metadata.create_all(self._engine)

    def drop_all(self):
        self.reset_engine()
        Users.__table__.drop(self._engine)

    def all_users(self):
        @_commit
        def _all_users(session: Session):
            return session.query(Users).all()

        return _all_users(self._get_session())
