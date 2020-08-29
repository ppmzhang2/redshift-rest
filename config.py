import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Redshift
    RS_USR = 'awsuser'
    RS_PWD = ''
    RS_HOST = 'id.redshift.amazonaws.com'
    RS_PORT = '5439'
    RS_DB = 'dev'
    RS_IAM_ROLE = ''
    S3_BUCKET = ''
    S3_REGION = ''
