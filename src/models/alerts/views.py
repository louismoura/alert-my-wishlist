from flask import Blueprint, render_template, request

from src.models.alerts.alert import Alert

alert_blueprint = Blueprint('alerts', __name__)

#Alert Index page
@alert_blueprint.route('/')
def index():
    return "This is alert page"

#Create alert page
@alert_blueprint.route('/new', methods=['POST','GET'])
def create_alert():
    if request.method == 'POST':
        pass

    return render_template('alerts/create_alert.html')

#Deactive an activated alert
@alert_blueprint.route('/deactive/<string:alert_id>')
def deactive_alert(alert_id):
    pass


#Display alert detail page
@alert_blueprint.route('/<string:alert_id>')
def alert_page(alert_id):
    alert = Alert.find_by_id(alert_id)
    return render_template('/alerts/alert.html', alert=alert)



#Check alert for specified user
@alert_blueprint.route('/for_user/<string:user_id>')
def get_alerts_for_user(user_id):
    pass