from flask import Blueprint



item_blueprint = Blueprint('items', __name__)


#Item page
@item_blueprint.route('/item/<string:name>')
def item_page():
    pass


#Load page
@item_blueprint.route('/load')
def item_load():

    """
    get a item's data using its store and save it to JSON
    :return:
    """


    pass