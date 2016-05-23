from flask import Blueprint



item_blueprint = Blueprint('items', __name__)


#Item page
@item_blueprint.route('/item/<string:name>')
def item_page():
    pass


