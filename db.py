import os
from orator import DatabaseManager, Schema
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

default = os.getenv('DB_DEFAULT')
driver = os.getenv('DB_DRIVER')
host = os.getenv('DB_HOST')
database = os.getenv('DB_NAME')
port = os.getenv('DB_PORT')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')

databases = {
    'default': default,
    default: {
        'driver': driver,
        'host': host,
        'database': database,
        'user': user,
        'password': password,
        'port': port,
        'prefix': ''
    }
}

db = DatabaseManager(databases)
schema = Schema(db)