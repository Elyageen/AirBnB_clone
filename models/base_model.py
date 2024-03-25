from datetime import datetime
import uuid


class BaseModel:
    """
    BaseModel class for other classes to inherit from.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes an instance of BaseModel.

        Args:
            *args: Unused.
            **kwargs: Dictionary of key-value pairs representing instance attributes.
                - If not empty, each key is an attribute name and each value is the value of that attribute.
                - If empty, id and created_at attributes are created as usual.

        """
        if kwargs:
            DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'

            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(value, DATE_TIME_FORMAT))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        """
        Return the string representation of BaseModel instance.

        Returns:
            str: String representation of the instance.
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
        from models import storage  # Import storage here to avoid circular import
        storage.new(self)
        storage.save()

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
