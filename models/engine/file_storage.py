#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary
        Return:
            returns a dictionary of a given cls
            or
            returns a dictionary of __object
        """
        if cls is not None:
            a_dict = {}
            for key, val in self.__objects.items():
                a_key = key.split(".")
                if cls.__name__ == a_key[0]:
                    a_dict.update({key: val})
            return (a_dict)
        return (self.__objects)

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """deletes the obj from __objects
        """
        if obj is not None:
            del_obj = type(obj).__name__ + "." + obj.id
            if del_obj in self.__objects:
                self.__objects.pop(del_obj)

    def close(self):
        """ close method that calls reload
        """
        self.reload()
