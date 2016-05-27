from flask import Blueprint, render_template, redirect, url_for, request,json

from src.models.stores.store import Store

store_blueprint = Blueprint('stores', __name__)

#Store Index
@store_blueprint.route('/')
def index():
    stores = Store.all()
    return render_template('/stores/store_index.html', stores=stores)

#Store page
@store_blueprint.route('/store/<string:store_id>')
def store_page(store_id):
    store = Store.get_by_id(store_id)
    return render_template('stores/store.html', store=store)

#Create Store
@store_blueprint.route('/new', methods=['POST', 'GET'])
def create_store():
    if request.method == 'POST':
        name = request.form['name']
        url_prefix = request.form['url_prefix']
        tag_name = request.form['tag_name']
        query = json.loads(request.form['query'])

        Store(name, url_prefix, tag_name, query).save_to_mongo()

        return redirect(url_for('.index'))

    return render_template('/stores/create_store.html')

#Edit Store
@store_blueprint.route('/edit/<string:store_id>', methods=['POST','GET'])
def edit_store(store_id):
    store = Store.get_by_id(store_id)

    if request.method == 'POST':
        if request.method == 'POST':
            name = request.form['name']
            url_prefix = request.form['url_prefix']
            tag_name = request.form['tag_name']
            query = request.form['query']

            store.name = name
            store.url_prefix = url_prefix
            store.tag_name = tag_name
            store.query = query

            store.save_to_mongo()

            return redirect(url_for('.index'))

    return render_template('/stores/edit_store.html', store=store)

#Delete Store
@store_blueprint.route('/delete/<string:store_id>')
def delete_store(store_id):
    store=Store.get_by_id(store_id)
    store.delete()
    return redirect(url_for('.index'))
