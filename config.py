import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'some string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    '''开发环境配置'''
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI')

class TestingConfig(Config):
    '''测试环境配置'''
    TESTING = True
    SQLALCHEMY_DATABASE_URI = xxxx

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = xxx

config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}#用一个字典来统合地给出所有配置