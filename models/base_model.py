#!/usr/bin/python3
"""
Module: base_model.py
"""
from datetime import datetime
import uuid


class BaseModel:
    """
    BaseModel class for other classes to inherit from.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize instance attributes.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.my_number = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        Return the string representation of BaseModel instance.

        Returns:
            str: String representation of the instance.
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.my_number, self.__dict__)

    def save(self):
        """
        Update the attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary representation of BaseModel instance.

        Returns:
            dict: Dictionary representation of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
