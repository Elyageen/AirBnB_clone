import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


# This class likely represents a file storage system in Python.
class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        This function is named "all" and it seems like the comment section is empty.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        This function is a constructor method that initializes a new object with the given input.
        
        :param obj: It looks like you have started defining a method called `new` that takes in a
        parameter `obj`. If you need any assistance with completing the method or have any specific
        questions, feel free to ask!
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        This function is used to save data or changes made within the class instance.
        """
        serializable_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(serializable_dict, file)

    def reload(self):
        """
        This function is used to reload a module or package in Python.
        """
        try:
            with open(FileStorage.__file_path, "r") as file:
                json_dict = json.load(file)
            for key, value in json_dict.items():
                cls_name, obj_id = key.split('.')
                cls = eval(cls_name)
                FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
