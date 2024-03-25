import json
from models.base_model import BaseModel


# This class likely represents a file storage system in Python.
class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        This function is named "all" and it seems like the comment section is empty.
        """
        return self.__objects

    def new(self, obj):
        """
        This function is a constructor method that initializes a new object with the given input.
        
        :param obj: It looks like you have started defining a method called `new` that takes in a
        parameter `obj`. If you need any assistance with completing the method or have any specific
        questions, feel free to ask!
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        This function is used to save data or changes made within the class instance.
        """
        serialized_objects = {
            key: obj.to_dict() for key, obj in self.__objects.items()
        }
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        This function is used to reload a module or package in Python.
        """
        try:
            with open(self.__file_path, 'r') as file:
                serialized_objects = json.load(file)
                for key, obj_dict in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    # Dynamically create an instance of the corresponding class
                    cls = eval(class_name)
                    obj = cls(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
