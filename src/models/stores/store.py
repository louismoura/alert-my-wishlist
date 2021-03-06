import uuid
import src.models.stores.constants as StoreConstants
from src.common.database import Database
import src.models.stores.errrors as StoreError

class Store(object):

    def __init__(self, name, url_prefix, tag_name, query, _id=None):
        self.name = name
        self.url_prefix = url_prefix
        self.tag_name = tag_name
        self.query = query
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<Store {}>".format(self.name)

    def json(self):
        return {
            'name' : self.name,
            'url_prefix' : self.url_prefix,
            'tag_name' : self.tag_name,
            'query' : self.query,
            '_id' : self._id
        }

    def save_to_mongo(self):
        Database.update(StoreConstants.COLLECTION, {'_id':self._id}, self.json())

    @classmethod
    def get_by_id(cls, id):
        return cls(**Database.find_one(StoreConstants.COLLECTION, {'_id':id}))

    @classmethod
    def get_by_name(cls, name):
        return cls(**Database.find_one(StoreConstants.COLLECTION, {'name':name}))

    @classmethod
    def get_by_url_prefix(cls, url_prefix):
        return cls(**Database.find_one(StoreConstants.COLLECTION, {"url_prefix": {"$regex": '^{}'.format(url_prefix)}}))

    @classmethod
    def get_store_by_url(cls, url):
        for i in range(0, len(url)+1):
            try:
                store = cls.get_by_url_prefix(url[:i])
                return store
            except:
                return StoreError.StoreNotFoundError("The Url prefix give to us cannot find the results.")

    @classmethod
    def all(cls):
        return [cls(**elm) for elm in Database.find(StoreConstants.COLLECTION, {})]


    def delete(self):
        return Database.remove(StoreConstants.COLLECTION, {'_id':self._id})