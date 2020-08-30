# Redshift REST Service

An `aiohttp` based REST service on querying Amazon Redshift. The sample data can be found via the Redshift [Getting Started Guide](https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-create-sample-db.html).

## Usage

The environment variable `PYTHON_ENV` is expected to be assigned with a valid Python environment path before starting service.

In trivial cases like testing or debugging, execute the `run.py` directly:

```shell
${PYTHON_ENV}/bin/python run.py
```

To utilize all CPU cores, start with Gunicorn:

```shell
./service.sh start
```

To stop service, use the same script:

```shell
./service.sh stop
```

## API

### Total Sales

Get total sales quantity at a given date.

* **Method**: `GET`
* **Example**: `/api/v1/sales?date=2008-01-05`
* **Arguments**
    + date: date string in `yyyy-mm-dd` format
* **Response Attributes**
    + sales: total sales on that day

## Reference

1. https://docs.aws.amazon.com/redshift/latest/dg/c_sampledb.html
2. http://mmariani.github.io/poss2016-aiohttp/
