from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URI
from models import Base, Wine

import pandas as pd

engine = create_engine(DATABASE_URI)

session = sessionmaker(bind=engine)

'''
Import data from repositories and convert to pandas DataFrames
'''

reds_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
whites_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'

red_wine_df = pd.read_csv(reds_url, delimiter = ';')
white_wine_df = pd.read_csv(whites_url, delimiter = ';')

'''
Create session with Postgres using SQLAlchemy
'''

Base.metadata.create_all(engine)


s = session()

red_wine_df.to_sql(name='RedWine',
                   con=engine,
                   if_exists='replace',
                   index=True,
                   index_label='id')

white_wine_df.to_sql(name='WhiteWine',
                   con=engine,
                   if_exists='replace',
                   index=True,
                   index_label='id')

s.close()

'''
Helper functions
'''

def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)