import logging.config
from datetime import datetime

from aiohttp import web
from aiohttp.abc import Request

from redshift import cfg
from redshift.log_maker import LogDbApi
from redshift.models.dao import Dao

logging.config.dictConfig(cfg.LOGGING)
logger = logging.getLogger('info_logger')
log_maker = LogDbApi(logger)


class DbApi(object):
    __slots__ = ['_dao']

    def __init__(self):
        self._dao = Dao()

    @log_maker
    async def json_total_sales(self, request: Request):
        fmt = '%Y-%m-%d'
        try:
            raw_str = request.rel_url.query.get('date')
            dt = datetime.strptime(raw_str, fmt)
            dt_str = dt.strftime(fmt)
        except (ValueError, TypeError):
            return web.json_response(
                status=400,
                data={
                    'message':
                    'parameter "date" accept only "yyyy-mm-dd" format'
                })
        else:
            sales = self._dao.total_sales(dt=dt_str)
            return web.json_response(data={'sales': sales})
