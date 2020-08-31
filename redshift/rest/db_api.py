import logging.config

from aiohttp import web
from aiohttp.abc import Request

from config import Config
from redshift.log_maker import LogMaker
from redshift.models.dao import Dao

logging.config.dictConfig(Config.LOGGING)
logger = logging.getLogger('info_logger')
log_maker = LogMaker(logger)


class DbApi(object):
    __slots__ = ['_dao']

    def __init__(self):
        self._dao = Dao()

    @log_maker
    async def json_total_sales(self, request: Request):
        date = request.rel_url.query.get('date')
        sales = self._dao.total_sales(dt=date)
        return web.json_response(data={'sales': sales})
