import os

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True

class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://pgadmin:admin@postgres:5432/test_db'
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
