from flask import Blueprint

user_blueprint = Blueprint('users', __name__)


#Login Page
@user_blueprint.route('/login')
def user_login():
    pass


#Register Page
@user_blueprint.route('/register')
def user_register():
    pass


#Alert Page
@user_blueprint.route('/alert')
def user_alert():
    pass



#Logout Page
@user_blueprint.route('/logout')
def user_logout():
    pass


#Check alerts by specified user
@user_blueprint.route('/check_alerts/<string:user_id>')
def check_user_alerts(user_id):
    pass