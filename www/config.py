
class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'AAABBBBAAAA'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
