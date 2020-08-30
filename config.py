import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # REST
    REST_URL_PREFIX = '/api/v1'
    REST_HOST = '0.0.0.0'
    REST_PORT = '8000'
    # Redshift
    RS_USR = 'awsuser'
    RS_PWD = ''
    RS_HOST = 'id.redshift.amazonaws.com'
    RS_PORT = '5439'
    RS_DB = 'dev'
    RS_IAM_ROLE = ''
    S3_BUCKET = ''
    S3_REGION = ''
