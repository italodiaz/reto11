from database.connection import Conexion
from orator.orm import has_one
from models.user import users as User

conn = Conexion()
Model = conn.model()


class message(Model):
    __table__ = 'message'
    __primary_key__ = 'id'
    __timestamps__ = True
    __connection__ = 'postgres'

    __guarded__ = ['id']

    __fillable__ = ['message_id', 'message', 'id_user']

    __casts__ = {
        'message': 'str',
        'message_id': 'str',
        'id_user': 'int'
    }

    @has_one('id', 'id_user')
    def user(self):
        return User
