#!/usr/bin/python3

"""
A class BaseModelthat defines
all common attributes/methods for other classes
"""

# to generate unique id [ Use it in string only ]
from uuid import uuid4

# datetime - assign with the current datetime when an instance is created
from datetime import datetime


class BaseModel:
    def __init__(self):
        """
        Define public instance attributes
        - id: unique id for every instance
        - created_at: the time at which the instance created
        - updated_at: the time at which the instance updated
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    def __str__(self):
        """
        display string information about new instant
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        return a dictionary of all attributes information
        """
        class_name = self.__class__.__name__
        formatted_created_at = self.created_at.isoformat()
        formatted_updated_at = self.update_at.isoformat()

        final_dict = self.__dict__.copy()

        final_dict["__class__"]= class_name
        final_dict["updated_at"]= formatted_updated_at
        final_dict["created_at"]= formatted_created_at

        return final_dict
