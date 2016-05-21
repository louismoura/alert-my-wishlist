from flask import Blueprint, request, session, url_for, render_template
from werkzeug.utils import redirect
import src.models.users.error as UserError
from src.models.users.user import User

user_blueprint = Blueprint('users', __name__)


#Login Page
@user_blueprint.route('/login', methods=['POST', 'GET'])
def user_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['hashed']

        if User.is_login_valid(email, password):
            session['email'] = email
            return redirect(url_for(".user_alert"))
        else:
            UserError.UserLoginFailed("You login failed")

    return render_template('/users/login.html')




#Register Page
@user_blueprint.route('/register')
def user_register():
    pass


#Alert Page
@user_blueprint.route('/alert')
def user_alert():
    return "This is alert page"



#Logout Page
@user_blueprint.route('/logout')
def user_logout():
    pass


#Check alerts by specified user
@user_blueprint.route('/check_alerts/<string:user_id>')
def check_user_alerts(user_id):
    pass