import os
from dotenv import load_dotenv
from pathlib import Path
from flask import Flask, request
from pymessenger.bot import Bot
from controllers.user import users as User
from controllers.message import message as Message

UserController = User()

MessageController = Message()


app = Flask(__name__)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
VERIFY_TOKEN = os.getenv('VERIFY_TOKEN')
bot = Bot(ACCESS_TOKEN)


def routes(app):
    @app.route("/", methods=['GET', 'POST'])
    def index():
        if request.method == 'GET':
            if request.args.get("hub.verify_token") == VERIFY_TOKEN:
                return request.args.get("hub.challenge")
            else:
                return 'Invalid verification token'

        if request.method == 'POST':
            output = request.get_json()
            for event in output['entry']:
                messaging = event['messaging']
                for x in messaging:
                    if x.get('message'):
                        recipient_id = x['sender']['id']
                        if x['message'].get('text'):
                            message = x['message']['text']
                            message_id = x['message']['mid']
                            UserController.add_user(
                                ACCESS_TOKEN, message_id, recipient_id)
                            usuario = MessageController.add_message(
                                {"user_id": recipient_id, "message": message,
                                 "message_id": message_id})
                            response = f"Hola {usuario}"
                            bot.send_text_message(recipient_id, response)
                        if x['message'].get('attachments'):
                            for att in x['message'].get('attachments'):
                                bot.send_attachment_url(
                                    recipient_id, att['type'],
                                    att['payload']['url'])
                    else:
                        pass
            return "Success"
