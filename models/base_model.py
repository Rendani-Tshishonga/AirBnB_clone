#!/usr/bin/python3
""" This is the Base Model of our program"""

from uuid import uuid4
import datetime
from models.engine import storage

class BaseModel:
    """
    This is the class of the Base Model
    *args will not be used.

    if kwargs is not empty:
        each key of this dictionary is an attribute name
        each value of this dictionary is the value of this attribute name
        Warning: created_at and updated_at are strings in this dictionary,
        but inside your BaseModel instance is working with datetime object.
        You have to convert these strings into datetime object.
        Tip: you know the string format of these datetime
    """
    def __init__(self, *args, **kwargs):

        if kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(self.__dict__["created_at"])
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(self.__dict__["updated_at"])
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

def __str__(self):
    """
    Should return [<class name>] (<self.id>) <self.__dict__>
    """
    return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

def save(self):
    """
    Updates the public instance variable
    with the current date. Save the current
    date of the storage instance 
    """
    updated_at = datetime.now()
    storage.save(self)

def to_dict(self):
    """
     returns a dictionary containing all keys/values of __dict__ of the instance
        by using self.__dict__, only instance attributes set will be returned.
        a key __class__ must be added to this dictionary with the class name of the object
        created_at and updated_at must be converted to string object in ISO format
        format: %Y-%m-%dT%H:%M:%S.%f
        you can use isoformat() of datetime object
    """
    my_dict = self.__dict__.copy()
    my_dict["__class__"] = type((self).__name__)
    my_dict["created_at"] = my_dict["created_at"].isoformat().\
            strftime("%Y-%m-%dT%H:%M:%S.%f")
    my_dict["updated_at"] = my_dict["updated_at"].isoformat().\
            strftime("%Y-%m-%dT%H:%M:%S.%f")
    return my_dict

