from models.message import message as MessageModel


class users:
    def add_message(self, message, app):
        try:
            MessageModel.insert({
                'message': message.message,
                'id_user': message.id_user
            })
            return "Mensaje Añadido"
        except Exception as e:
            print(str(e))
