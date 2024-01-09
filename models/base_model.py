#!/usr/bin/python3
"""
Custom base class for the entire project
"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Custom base for all the classes in the AirBnb console project

    Attributes:
        id (str): handles unique user identity
        created_at: assigns current datetime
        updated_at: updates current datetime

    Methods:
        __str__: prints the class name, id, and creates dictionary
        save(self): updates instance attributes with current datetime
        to_dict(self): returns the dictionary values of the instance obj

    """

    
    def __init__(self):
        """initialize a public instance"""
        #convert id value to string
        self.id = str(uuid4()) 
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """return string representation of obj"""

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
    def save(self):
        """update the updated_at to current time"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation"""

        data_copied = self.__dict__.copy()
        #to access name of class
        data_copied["__class__"] = self.__class__.__name__
    #Convert to ISO format
        data_copied["created_at"] = self.created_at.isoformat()
        data_copied["updated_at"] = self.updated_at.isoformat()
        #return the dictionary
        return data_copied