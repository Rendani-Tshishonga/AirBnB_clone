#!/usr/bin/python3
import json

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
    if FileStorage.__file_path != "":
        with open('FileStorage.__file_path', 'r') as f:
            FileStorage.__object = json.load(f)
        FileStorage.__object = FileStorage(FileStorage.__object)

def class_list(self):
    class_list = ["BaseModel", "City", "User", "Place",\
            "State", "Review"]
    return class_list
