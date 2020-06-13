from database.connection import Conexion
from bcrypt import checkpw

conn = Conexion()
Model = conn.model()

class users(Model):
    __table__ = 'users'
    __primary_key__ = 'id'
    __timestamps__ = True
    __connection__ = 'postgres'

    __guarded__ = ['id']

    __fillable__ = ['username', 'password', 'name', 'last_name', 'age']

    __casts__ = {
        'username': 'str',
        'password': 'str',
        'name': 'str',
        'last_name': 'str',
        'age': 'int'
    }

    __hidden__ = ['password']

    def password_valid(self, password):
        return checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
