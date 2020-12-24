import os
import json

class JsonDatabase():
    def __init__(self, path, name):
        self.path = os.path.expanduser(path)
        self.name = name
        self.deserialize(self.path)

    def deserialize(self, path):
        if (os.path.exists(path)):
            self.database = json.load(open(self.path, 'r'))
        else:
            self.database = {}

    def serialize(self):
        try:
            json.dump(self.database, open(self.path, 'w+'), indent=4)
        except:
            print('[{name}]: Error saving values to database'.format(name=self.name))

    def set(self, key, value):
        self.database[key] = value
        self.serialize()

    def get(self, key):
        if key in self.database:
            return self.database[key]
        print('[{name}]: No key in database named: '.format(name=self.name) + str(key))

    def get_all(self):
        return self.database

    def remove(self, key):
        if key in self.database:
            del self.database[key]
            self.serialize()
            return True
        print('[{name}] Cannot delete a value that is not in the database: '.format(name=self.name) + str(key))

    def clear(self):
        self.database = {}
        self.serialize()


