import asyncio

from aiohttp import web

from config import Config
from redshift.rest.db_api import DbApi


class Service(object):
    __slots__ = ['app', '_db_api']

    def __init__(self):
        self.app = web.Application()
        self._db_api = DbApi()
        self.app.router.add_routes([
            web.get(f'{Config.REST_URL_PREFIX}/sales',
                    self._db_api.json_total_sales)
        ])

    async def _get_runner(self):
        runner = web.AppRunner(self.app)
        await runner.setup()
        return runner

    async def _get_server(self, loop):
        runner = await self._get_runner()
        server = await loop.create_server(runner.server, Config.REST_HOST,
                                          Config.REST_PORT)
        return server

    def run(self):
        loop = asyncio.get_event_loop()
        srv = loop.run_until_complete(self._get_server(loop))
        print('serving on', srv.sockets[0].getsockname())

        try:
            loop.run_forever()
        except KeyboardInterrupt:
            pass
        finally:
            srv.close()
            loop.run_until_complete(srv.wait_closed())
            loop.run_until_complete(self.app.shutdown())
            loop.run_until_complete(self.app.cleanup())
        loop.close()
