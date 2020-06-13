import json
from requests import get
from models.user import users as UserModel


class users:
    def add_user(self, access_token, message_id, user_id):
        try:
            user_found = UserModel.where('user_id', user_id).first()
            if not user_found:
                user = self.search_fb(message_id, access_token)
                UserModel.insert({
                    'user_id': user_id,
                    'name': user['name'],
                    'email': user['email']
                })
        except Exception as e:
            print(str(e))

    def get_json(self, url, payload):
        r = get(url, params=payload)
        binary = r.content
        return json.loads(binary)

    def search_fb(self, message_id, access_token):
        url = f'https://graph.facebook.com/v7.0/{message_id}'
        payload = {'fields': 'from', 'access_token': access_token}
        output = self.get_json(url, payload)
        return output['from']
