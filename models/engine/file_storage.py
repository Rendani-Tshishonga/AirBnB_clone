#!/usr/bin/python3

class FileStorage:
    self.__file_path = "file.json"
    self.__object = {}

def all(self):
    return FileStorage.__object

def new(self, obj):
    key = "{}.{}".format(type(obj).__name__, obj.id)
    FileStorage.__object[key] = obj 
