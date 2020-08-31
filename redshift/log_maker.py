import logging.config
from functools import wraps


class LogMaker(object):
    def __init__(self, logger: logging.Logger):
        self._logger = logger

    def __call__(self, fn):
        @wraps(fn)
        def helper(*args, **kwargs):
            try:
                res = fn(*args, **kwargs)
                return res
            except Exception as ex:
                self._logger.error(f'[{fn.__module__} - {fn.__name__}]: '
                                   f'{ex.__str__()}')
                raise ex

        return helper
