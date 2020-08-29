from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import Config
from redshift.models.base import Base

__all__ = ['Dao']


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

    def _session_maker(self):
        _Session = sessionmaker(bind=self._engine)
        return _Session()

    def _create_tables(self):
        Base.metadata.create_all(self._engine)
