import asyncio

import uvloop

from redshift.service import Service

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
loop = asyncio.get_event_loop()
service = Service()
app = service.app


if __name__ == '__main__':
    service.run()
