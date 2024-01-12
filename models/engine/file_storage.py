#!/usr/bin/python3
"""Defines the FileStorage class."""

# Module for serializarion & derialization
import json
from models.base_model import BaseModel


class FileStorage:
    """Represent an abstracted storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        obj_name = obj.__class__.__name__
        key = f"{obj_name}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        objects = FileStorage.__objects
        path = FileStorage.__file_path
        # 1) Convert every object to dict
        obj_dict = {obj: objects[obj].to_dict() for obj in objects.keys()}

        # 2) Serialize every dict to json string
        with open(path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        # Need more understanding
        """ deserializes the JSON file to __objects """
        if (FileStorage.__file_path):
            with open(FileStorage.__file_path) as file:
                dict = json.load(file)
                for value in dict.values():
                    class_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(class_name)(**value))
        else:
            return
