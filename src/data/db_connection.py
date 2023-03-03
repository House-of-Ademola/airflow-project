import pandas as pd
import psycopg2
from config.config import config


def load_db_table(config_db, query):  # Take in the PostgresSQL table and outputs a pandas dataframe
    params = config(config_db)
    engine = psycopg2.connect(**params)
    data = pd.read_sql(query, con=engine)
    return data
