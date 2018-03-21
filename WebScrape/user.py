

class User(object):
    def __init__(self,email, password, _id=None):
        self.email = email
        self.password = password
        self._id =_id
