from aiohttp import web
from aiohttp.abc import Request

from redshift.models.dao import Dao


class DbApi(object):
    __slots__ = ['_dao']

    def __init__(self):
        self._dao = Dao()

    async def json_total_sales(self, request: Request):
        date = request.rel_url.query.get('date')
        sales = self._dao.total_sales(dt=date)
        return web.json_response(data={'sales': sales})
