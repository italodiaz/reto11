from models.user import users as UserModel


class users:
    def add_user(self, user, app):
        try:
            user_found = UserModel.where('user_id', user.user_id).first()
            if user_found:
                user_found.update({
                    'name': user.name,
                    'email': user.email
                })
                return "Update"
            UserModel.insert({
                'user_id': user.user_id,
                'name': user.name,
                'email': user.email
            })
            return "Creado"
        except Exception as e:
            print(str(e))
