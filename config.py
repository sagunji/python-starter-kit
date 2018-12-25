import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    """Base configuration."""

    SQLALCHEMY_ECHO = False
    DEBUG_TB_ENABLED = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    WTF_CSRF_ENABLED = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "postgresql://postgres:password@localhost/test"
    )


class TestingConfig(BaseConfig):
    """Testing configuration."""

    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL", "sqlite:///")
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration."""

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    WTF_CSRF_ENABLED = True
