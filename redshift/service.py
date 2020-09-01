import asyncio

from aiohttp import web

from redshift import cfg
from redshift.rest.db_api import DbApi


class Service(object):
    __slots__ = ['app', '_db_api']

    def __init__(self):
        self.app = web.Application()
        self._db_api = DbApi()
        self.app.router.add_routes([
            web.get(f'{cfg.REST_URL_PREFIX}/sales',
                    self._db_api.json_total_sales)
        ])

    async def _get_runner(self):
        runner = web.AppRunner(self.app)
        await runner.setup()
        return runner

    async def _get_server(self, loop, host, port):
        runner = await self._get_runner()
        server = await loop.create_server(runner.server, host, port)
        return server

    def run(self, host: str = '127.0.0.1', port: str = '8000'):
        loop = asyncio.get_event_loop()
        srv = loop.run_until_complete(self._get_server(loop, host, port))
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
