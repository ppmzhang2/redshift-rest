import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # REST
    REST_URL_PREFIX = '/api/v1'
    # Redshift
    RS_USR = 'awsuser'
    RS_PWD = ''
    RS_HOST = 'id.redshift.amazonaws.com'
    RS_PORT = '5439'
    RS_DB = 'dev'
    RS_IAM_ROLE = ''
    S3_BUCKET = ''
    S3_REGION = ''
    # Logging
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'nano': {
                'format': '%(asctime)s  %(message)s'
            },
            'micro': {
                'format':
                '%(asctime)s [%(levelname)s] '
                '%(name)s: '
                '%(message)s',
            },
            'small': {
                'format':
                '%(asctime)s [%(levelname)s] '
                '%(module)s - %(filename)s - %(lineno)s: '
                '%(message)s',
            },
        },
        'handlers': {
            'info_file': {
                'level': 'INFO',
                'formatter': 'small',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'when': 'H',
                'interval': 1,
                'backupCount': 6,
                'filename': f'{basedir}/logs/info.log',
            },
            'debug_streamer': {
                'level': 'DEBUG',
                'formatter': 'small',
                'class': 'logging.StreamHandler',
                'stream': 'ext://sys.stdout',
            },
            'debug_file': {
                'level': 'DEBUG',
                'formatter': 'small',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'when': 'M',
                'interval': 1,
                'backupCount': 30,
                'filename': f'{basedir}/logs/debug.log',
            },
        },
        'loggers': {
            'info_logger': {
                'handlers': ['debug_streamer', 'info_file'],
                'level': 'DEBUG',
                'propagate': False,
            },
        },
    }
