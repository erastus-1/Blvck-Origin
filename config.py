import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = ('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://erastus:Angular2020@localhost/photo'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'erastuskariuki15@gmail.com@gmail.com'
    MAIL_PASSWORD = '@e1r2a3s4#'
    
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://erastus:Angular2020@localhost/photo_test'



class ProdConfig(Config):
    pass

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://erastus:Angular2020@localhost/photo'

    DEBUG = True
    ENV = 'development'
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
