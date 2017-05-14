"""Config module."""


class Config(object):
    """Main config class, do not load directly."""

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:toorroot@localhost/testdb'
    GRAPHIQL_ENABLED = False


class DevConfig(Config):
    """Development config."""

    DEVELOPMENT = True
    DEBUG = True
    GRAPHIQL_ENABLED = True


class StagingConfig(Config):
    """Staging config."""

    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    """Testing config."""

    TESTING = True


class ProductionConfig(Config):
    """Production config."""

    DEBUG = False
