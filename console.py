#!/usr/bin/python3
"""The console module."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """The console class."""
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing when empty line is entered."""
        pass

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """Handle EOF."""
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_dict = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in obj_dict:
            print(obj_dict[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key in obj:
            del obj[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances."""
        args = arg.split()
        obj_list = []
        if not arg:
            for key, value in storage.all().items():
                obj_list.append(str(value))
        elif args[0] in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            for key, value in storage.all().items():
                if args[0] in key:
                    obj_list.append(str(value))
        else:
            print("** class doesn't exist **")
            return
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key not in obj:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj_instance = obj[key]
        setattr(obj_instance, args[2], args[3])
        obj_instance.save()

    def do_User(self, arg):
        """Retrieve all instances of User class."""
        self.do_all("User")

    def do_BaseModel(self, arg):
        """Retrieve all instances of BaseModel class."""
        self.do_all("BaseModel")

    def do_State(self, arg):
        """Retrieve all instances of State class."""
        self.do_all("State")

    def do_City(self, arg):
        """Retrieve all instances of City class."""
        self.do_all("City")

    def do_Amenity(self, arg):
        """Retrieve all instances of Amenity class."""
        self.do_all("Amenity")

    def do_Place(self, arg):
        """Retrieve all instances of Place class."""
        self.do_all("Place")

    def do_Review(self, arg):
        """Retrieve all instances of Review class."""
        self.do_all("Review")

    def do_count(self, arg):
        """Count the instances of a class."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        count = 0
        obj_dict = storage.all()
        for key, value in obj_dict.items():
            class_name = key.split('.')[0]
            if class_name == args[0]:
                count += 1
        # print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
