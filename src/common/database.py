import pymongo
class Database(object):

    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)


    @staticmethod
    def find_one(colleciton, query):
        return Database.DATABASE[colleciton].find_one(query)


    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def update(collection, query, data):
        return Database.DATABASE[collection].update(query, data, upsert=True)