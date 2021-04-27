
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://maryam:1234@localhost/pomodoro'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG =True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://maryam:1234@localhost/pomodoro'



config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}