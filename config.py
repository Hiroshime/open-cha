import os

SECRET_KEY = os.getenv('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.getenv('DB_STRING')
#'sqlite:///scheduler.db'
