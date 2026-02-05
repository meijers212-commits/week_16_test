from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

db_host = os.getenv("DB_HOST", "localhost")
db_port = os.getenv("DB_PORT", 27017)
db_name = os.getenv("DB_NAME", "my_db")
col_name = os.getenv("COL_NAME","week_16")

uri = f'mongodb://{db_host}:{db_port}'

client = MongoClient(uri)

db = client[db_name]

col = db[col_name]



def get_collection():
    return client[db_name][col_name]





