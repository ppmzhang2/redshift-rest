FROM python:3.8.5-buster

MAINTAINER "Meng <ztz2000@gmail.com>"

COPY . /app

WORKDIR /app

RUN pip install -r /app/requirements.txt \
    && mkdir -p /app/logs \
    && chmod +x /app/wsgi.sh

CMD ["/app/wsgi.sh"]
