from flask import Blueprint, render_template, request, session, redirect, url_for

from src.models.alerts.alert import Alert
from src.models.items.item import Item

alert_blueprint = Blueprint('alerts', __name__)

#Alert Index page
@alert_blueprint.route('/')
def index():
    return "This is alert page"

#Create alert page
@alert_blueprint.route('/new', methods=['POST','GET'])
def create_alert():
    if request.method == 'POST':
        name = request.form['name']
        url = request.form['url']
        price_limit = float(request.form['price'])
        item = Item(name, url)
        item.save_to_mongo()
        alert = Alert(session['email'], price_limit, item._id)
        alert.load_item_price()

    return render_template('alerts/create_alert.html')

#Edit alert page
@alert_blueprint.route('/edit/<string:alert_id>', methods=['POST', 'GET'])
def edit_alert(alert_id):
    alert = Alert.find_by_id(alert_id)

    if request.method == 'POST':

        price_limit = float(request.form['price'])
        alert.price_limit = price_limit
        alert.save_to_mongo()

        return redirect(url_for('users.user_alert'))

    return render_template('alerts/edit_alert.html', alert=alert)


#Deactive an activated alert
@alert_blueprint.route('/deactivate/<string:alert_id>')
def deactive_alert(alert_id):
    Alert.find_by_id(alert_id).deactivate()
    return redirect(url_for('users.user_alert'))

#Active an deactivated alert
@alert_blueprint.route('/activate/<string:alert_id>')
def active_alert(alert_id):
    Alert.find_by_id(alert_id).activate()
    return redirect(url_for('users.user_alert'))

#Delete an deactivated alert
@alert_blueprint.route('/delete/<string:alert_id>')
def delete_alert(alert_id):
    Alert.find_by_id(alert_id).delete()
    return redirect(url_for('users.user_alert'))


#Display alert detail page
@alert_blueprint.route('/<string:alert_id>')
def alert_page(alert_id):
    alert = Alert.find_by_id(alert_id)
    return render_template('/alerts/alert.html', alert=alert)

#Refresh Price
@alert_blueprint.route('/check_price/<string:alert_id>')
def check_price(alert_id):
    Alert.find_by_id(alert_id).load_item_price()
    return redirect(url_for('.alert_page', alert_id=alert_id))


#Check alert for specified user
@alert_blueprint.route('/for_user/<string:user_id>')
def get_alerts_for_user(user_id):
    pass