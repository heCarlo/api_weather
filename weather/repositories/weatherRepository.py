from django.conf import settings
from ..models import WeatherEntity
import pymongo

class WeatherRepository:
    collection = ''

    def __init__(self, collectionName) -> None:
        self.collection = collectionName

    def get_connection(self):
        client = pymongo.MongoClient(getattr(settings, "MONGO_CONNECTION_STRING"))
        connection = client[getattr(settings, "MONGO_DATABASE_NAME")]
        return connection
    
    def get_collection(self):
        conn = self.get_connection()
        collection = conn[self.collection]
        return collection
    
    def get_all(self):
        documents = self.get_collection().find({})
        return documents
    
    def insert(self, document):
        self.get_collection().insert_one(document)
    
        def update(self, filter_query, update_query):
            self.get_collection().update_one(filter_query, {"$set": update_query})
    
    def delete(self, query):
        self.get_collection().delete_one (query)

    def delete_all(self):
        self.get_collection().delete_many({})
        
    def filter_by_city(self, city):
        query = {"city": city}
        documents = self.get_collection().find(query)
        return list(documents)

