import uuid
from src.common.utils import Utils
from src.common.database import Database
import src.models.users.error as UserError

class User(object):

    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "User {}".format(self.email)


    @staticmethod
    def is_login_valid(email, password):

        user_data = Database.find_one('user', {'email':email})

        if user_data is None:

            raise UserError.UserNotExistError("User doesn't exist")

        if not Utils.check_hashed_password(password, user_data['password']):

            raise UserError.IncorrectPasswordError("Password is not correct")

        return True

    @staticmethod
    def register_user(email, password):
        user_data = Database.find_one('user', {'email':email})

        if user_data is not None:
            raise UserError.UserAlreadyHasError("User is existing, please try again")
        if not Utils.email_is_valid(email):
            raise UserError.InvalidEmailError("Email is invalid, please enter another email")

        User(email, Utils.hash_password(password)).save_to_mongo()

        return True


    def save_to_mongo(self):
        Database.insert('user', self.json())

    def json(self):
        return {'_id':self._id,
                'email':self.email,
                'password':self.password}