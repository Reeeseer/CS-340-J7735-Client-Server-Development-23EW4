from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.username = username
        self.password = password
        #self.client = MongoClient('mongodb://%s:%s@localhost:34339/?authsource=AAC' % (username, password))
        self.client = MongoClient("mongodb://aacuser:password@localhost:34339/AAC")
        # where xxxx is your unique port number
        self.db = self.client.AAC
        self.collection = self.db.animals
        

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            result = self.collection.insert_one(data)
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD
    def read(self, data):
        if data is not None:
            result = self.collection.find(data)
            if result is None:
                return "could not find your data"
            return result
        else:
            raise Exception("Nothing to read, because data is empty")
            
    def update(self, query, change):
        if query or change is not None:
            self.collection.update_one(query, change)
        else:
            raise Exception("Nothing to read, an arguement is empty")
            
    def delete(self, data):
        if data is not None:
            result = self.collection.find_one(data)
            if result is not None:
                self.collection.delete_one(data)
                print("data successfully deleted")
            else:
                raise Exception("No data exsists")
        else:
            raise Exception("Nothing to read, data is empty")
            
    def distinct(self, data):
        if data is not None:
            result = self.collection.distinct(data)
            return result
    
            
      
            
            