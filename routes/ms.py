import os
from pymessenger.bot import Bot
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
token = os.getenv('TOKEN')
# app_secret = os.getenv('APP_SECRET')
bot = Bot(token)


def ms_routes(app):
    @app.route('/', methods=['GET'])
    def hola():
        return bot
