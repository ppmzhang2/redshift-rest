#!/bin/bash
### BEGIN INIT INFO
#
# Short-Description: start / stop service
# Description:
#
### END INIT INFO

basepath="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

CPUS=$(getconf _NPROCESSORS_ONLN 2> /dev/null)
PID_FILE=${basepath}/gunicorn.pid
LOG_FILE="${basepath}/logs/gunicorn.log"
DAEMON="${PYTHON_ENV}/bin/gunicorn"
WORKERS=$((2*CPUS+1))
BIND=0.0.0.0:8000
APP_MODULE=run:app

cd "${basepath}" || exit
# mode selection
if [ "$1" = 'start' ]
then
    echo "Starting service..."
    $DAEMON --daemon $APP_MODULE --bind $BIND --pid "$PID_FILE" \
      --worker-class aiohttp.GunicornWebWorker \
      --workers=$WORKERS --log-file="$LOG_FILE"
elif [ "$1" = 'stop' ]
then
    echo "Stopping service..."
    kill -9 "$(cat "$PID_FILE")"
else
    echo "Wrong input!"
    exit 127
fi
