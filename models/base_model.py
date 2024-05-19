#!/usr/bin/python3
""" This is the Base Model of our program"""

from uuid import uuid4
import datetime
from engine.file_storage import FileStorage

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(self.__dict__["created_at"])
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(self.__dict__["updated_at"])
                else
                    self.__dict__[key] = kwargs[key]
        else
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

def __str__(self):
    return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

def save(self):
    updated_at = datetime.now()
    storage = FileStorage()
    storage.save(self)

def to_dict(self):
    my_dict = self.__dict__.copy()
    my_dict["__class__"] = type((self).__name__)
    my_dict["created_at"] = my_dict["created_at"].isoformat().\
            strftime("%Y-%m-%dT%H:%M:%S.%f")
    my_dict["updated_at"] = my_dict["updated_at"].isoformat().\
            strftime("%Y-%m-%dT%H:%M:%S.%f")
    return my_dict

