from flask import Blueprint




alert_blueprint = Blueprint('alerts', __name__)


#Create alert page
@alert_blueprint.route('/create', methods=['POST'])
def create_alert():
    pass

#Deactive an activated alert
@alert_blueprint.route('/deactive/<string:alert_id>')
def deactive_alert(alert_id):
    pass


#Display alert detail page
@alert_blueprint.route('/alert/<string:alert_id>')
def alert_page(alert_id):
    pass



#Check alert for specified user
@alert_blueprint.route('/for_user/<string:user_id>')
def get_alerts_for_user(user_id):
    pass