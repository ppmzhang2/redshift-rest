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
