import os
from config import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from models import Base

# from dotenv import dotenv_values
# BASE_DIR = os.path.dirname(os.getcwd())
# env = dotenv_values(f'{BASE_DIR}/.env')


engine = create_engine(f'postgresql://'
                       f'{DB_USER}:'
                       f'{DB_PASS}@'
                       f'{DB_HOST}:'
                       f'{DB_PORT}/'
                       f'{DB_NAME}')

Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
session = DBSession()


def get_session():
    return session