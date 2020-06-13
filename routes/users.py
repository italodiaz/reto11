from flask import request
from controllers.user import User

UserController = User()


def user_routes(app):
    @app.route('/', methods=['POST'])
    def create_user():
        values = request.values
        UserController.username = values.get('user_id')
        UserController.name = values.get('name')
        UserController.last_name = values.get('email')
        return UserController.add_user(UserController, app)
