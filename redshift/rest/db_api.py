from concurrent.futures.thread import ThreadPoolExecutor

import asyncio
from aiohttp import web
from aiohttp.abc import Request

from redshift.models.dao import Dao


class DbApi(object):
    __slots__ = ['_dao', '_executor', '_loop']

    def __init__(self):
        self._dao = Dao()
        self._executor = ThreadPoolExecutor(10)
        self._loop = asyncio.get_event_loop()

    async def json_total_sales(self, request: Request):
        async def _aio_total_sales(dt: str):
            def helper():
                return self._dao.total_sales(dt=dt)

            return await self._loop.run_in_executor(self._executor, helper)

        date = request.rel_url.query.get('date')
        sales = await _aio_total_sales(date)
        return web.json_response(data={'sales': sales})
