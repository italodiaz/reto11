from flask import Flask
from routes.users import user_routes

app = Flask(__name__)
user_routes(app)

if __name__ == '__main__':
    app.run()
