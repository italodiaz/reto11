from models.message import message as MessageModel
from models.user import users as UserModel


class message:
    def add_message(self, msg):
        try:
            user_found = UserModel.where('user_id', msg['user_id']).first()
            print(user_found)
            MessageModel.insert({
                'message': msg['message'],
                'message_id': msg['message_id'],
                'id_user': user_found.id
            })
            return user_found.name
        except Exception as e:
            print(str(e))
