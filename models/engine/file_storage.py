#!/usr/bin/python3
import json
import os

class FileStorage:
    __file_path = "file.json"
    __object = {}

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
        data = {for k, v in FileStorage.__object.items()}
        json.dump(data, f)

def reload(self):
    """ Deserializes the JSON file to __objects."""
    if not os.path.isfile(FileStorage.__filepath):
        return
    with open('FileStorage.__file_path', 'r') as f:
        my_dict = json.load(f)
        FileStorage.__object = {for k, v in my_dict.items()}

def class_list(self):
    class_list = ["BaseModel", "City", "User", "Place",\
            "State", "Review"]
    return class_list
