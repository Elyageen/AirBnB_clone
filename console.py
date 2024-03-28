# console.py

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage

classes = {"BaseModel": BaseModel, "User": User, "State": State,
           "City": City, "Place": Place, "Amenity": Amenity,
           "Review": Review}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        print("")
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        objs = FileStorage().all()
        if key in objs:
            print(objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        objs = FileStorage().all()
        if key in objs:
            del objs[key]
            FileStorage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        objs = FileStorage().all()
        if not arg:
            for obj in objs.values():
                print(obj)
        else:
            args = arg.split()
            if args[0] not in classes:
                print("** class doesn't exist **")
                return
            filtered_objs = [v for k, v in objs.items() if k.startswith(args[0])]
            for obj in filtered_objs:
                print(obj)

    def do_update(self, arg):
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        objs = FileStorage().all()
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(objs[key], args[2], args[3])
        objs[key].save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
