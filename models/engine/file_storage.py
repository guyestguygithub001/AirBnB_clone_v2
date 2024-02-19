#!/usr/bin/python3
"""The file storage class for AirBnB clone v2."""

import json
from models.base_model import BaseModel
import shlex
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.place import Place

class FileStorage:
    """ Class to serialize instances to JSON file and
    deserializes JSON file to instances,
    Attributes:
        __file_path: path to the JSON file,
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns a dictionary,
        Return:
            returns dictionary of __object,
        """
        dic = {}
        if cls:
            dictionary = self.__objects
            for key in dictionary:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    dic[key] = self.__objects[key]
            return (dic)
        else:
            return self.__objects

    def save(self):
        """serializes file path to a JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def new(self, obj):
        """sets __object to given object,
        Args:
            obj: given object.
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj


    def reload(self):
        """serializes path to file to JSON file path.
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def close(self):
        """ To call reload.()
        """
        self.reload()

    def delete(self, obj=None):
        """ removes present element
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

