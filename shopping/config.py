import os


class Settings:
    POSTGRES_USER = os.environ.get('POSTGRES_USER')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
    POSTGRES_SERVER = os.environ.get('POSTGRES_SERVER')
    POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
    POSTGRES_DB = os.environ.get('POSTGRES_DB')

    REDIS_HOST = os.environ.get('REDIS_HOST')
    REDIS_PORT = os.environ.get('REDIS_PORT')
    REDIS_CELERY_DB_INDEX = os.environ.get('REDIS_CELERY_DB_INDEX')
    REDIS_STORE_DB_INDEX = os.environ.get('REDIS_STORE_DB_INDEX')

    RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST')
    RABBITMQ_USERNAME = os.environ.get('RABBITMQ_USERNAME')
    RABBITMQ_PASSWORD = os.environ.get('RABBITMQ_PASSWORD')
    RABBITMQ_PORT = os.environ.get('RABBITMQ_PORT')

    BROKER_CONN_URI = f"amqp://{RABBITMQ_USERNAME}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}:{RABBITMQ_PORT}"
    BACKEND_CONN_URI = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CELERY_DB_INDEX}"
    REDIS_STORE_CONN_URI = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_STORE_DB_INDEX}"
    DB_CONN_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    stages = ["confirmed", "shipped", "in transit", "arrived", "delivered"]
    # STAGING_TIME = 15 # seconds


settings = Settings()
