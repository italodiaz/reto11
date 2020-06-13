from flask import request
from controllers.user import users
from helpers.helper import token_required
from requests import get

UserController = users()

def user_routes(app):
    @app.route('/users', methods=['POST'])
    @token_required
    def create_user():
        values = request.values
        UserController.username = values.get('username')
        UserController.password = values.get('password')
        UserController.name = values.get('name')
        UserController.last_name = values.get('last_name')
        UserController.age = values.get('age')
        return UserController.add_user(UserController, app)


    @app.route('/login', methods=['POST'])
    def login():
        # Consumo de api externa
        #response = get('http://google.com.pe')
        #print(response.text)
        values = request.values
        UserController.username = values.get('username')
        UserController.password = values.get('password')
        return UserController.login(UserController, app)
