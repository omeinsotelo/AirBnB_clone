#!/usr/bin/python3
""" Base Model: defines all common attributes/methods for other classes """
from uuid import uuid4  # Module to generate a random ID
import models
from datetime import datetime
""" Return a string representing the date in ISO 8601 format, ‘YYYY-MM-DD’ """


class BaseModel:
    """ Mother class of all objets class """
    def __init__(self, *args, **kwargs):
        """ Constructor """
        if kwargs:
            del kwargs["__class__"]
            for key, val in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, val)
        else:
            self.id = str(uuid4())
            """ Generate id for the objet in str format """
            self.created_at = datetime.now()
            """ Generate date of the creation objet """
            self.updated_at = datetime.now()
            """ Generate date of the update modification of the objets """
            models.storage.new(self)

    def __str__(self):
        """ Print all atributes of the objets """
        string = "[{}] ".format(type(self).__name__)
        string += "({}) ".format(self.id)
        string += "{}".format(self.__dict__)
        return string

    def save(self):
        """
        Updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        dicti = self.__dict__.copy()
        dicti["__class__"] = type(self).__name__
        dicti["created_at"] = self.created_at.isoformat()
        dicti["updated_at"] = self.updated_at.isoformat()
        return dicti
