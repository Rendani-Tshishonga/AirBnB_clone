#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User
from moels.city import City
from models.state import State
from models.place import Place
from models.review import Review

class FileStorage:
    __file_path = "file.json"
    __object = {}

def all(self):
    return FileStorage.__object

def new(self, obj):
    FileStorage.__object[key] = "{}.{}".format(type(obj).__name__,\
            obj.id)
    return FileStorage.__object

def save(self):
    """ Retrieve a dictionary in __object attribute """
    FileStorage.__object = FileStorage.__object.to_json()
    with open ('FileStorage.__file_path', 'w') as f:
        data = {key: value.to_dict() for key, value in FileStorage.__object.items()}
        json.dump(data, f)

def reload(self):
    """ Deserializes the JSON file to __objects."""
    if not os.path.isfile(FileStorage.__filepath):
        return
    with open('FileStorage.__file_path', 'r') as f:
        my_dict = json.load(f)
        FileStorage.__object = {key: value for key, value in my_dict.items()}

def class_list(self):
    
    class_list = {"BaseModel": BaseModel,
            "User": User,
            "City": City,
            "State": State,
            "Place": Place,
            "Review": Review
            }
    return class_list
