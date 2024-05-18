#!/usr/bin/python3
import json

class FileStorage:
    self.__file_path = "file.json"
    self.__object = {}

def all(self):
    return FileStorage.__object

def new(self, obj):
    FileStorage.__object = "{}.{}".format(type(obj).__name__,\
            obj.id)
    return FileStorage.__object

def save(self):
    """ Retrieve a dictionary in __object attribute """
    FileStorage.__object = FileStorage.__object.to_json()
    with open ('FileStorage.__file_path', 'w') as f:
        json.dump(FileStorage.__object, f,  sort_keys=True)

def reload(self):
    """ Deserializes the JSON file to __objects."""
    if FileStorage.__file_path != "":
        with open('FileStorage.__file_path', 'r') as f:
            FileStorage.__object = json.load(FileStorage.__object)
        storage = FileStorage(FileStorage.__object)
