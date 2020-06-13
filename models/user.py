from database.connection import Conexion

conn = Conexion()
Model = conn.model()


class users(Model):
    __table__ = 'user'
    __primary_key__ = 'id'
    __timestamps__ = True
    __connection__ = 'postgres'

    __guarded__ = ['id']

    __fillable__ = ['user_id', 'name', 'email']

    __casts__ = {
        'user_id': 'bigint',
        'name': 'str',
        'email': 'str'
    }
