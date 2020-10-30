import argparse

import uvicorn

from redshift.main import app

parser = argparse.ArgumentParser(description='Redshift Rest Service')
parser.add_argument('--port')


if __name__ == '__main__':
    args = parser.parse_args()
    uvicorn.run(app, host='127.0.0.1', port=int(args.port))
