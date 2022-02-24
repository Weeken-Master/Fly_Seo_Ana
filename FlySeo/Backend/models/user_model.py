class User:
    def __init__(self, user_id=0, username='', password='', role=''):
        self.user_id = user_id
        self.username = username # duy nhhaats
        self.password = password
        self.role = role

    def serialize(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'role': self.role

            # ko trả về  password  ( tránh lộ thông tin)
        }