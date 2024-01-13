#!/usr/bin/python3
""" Entry point of the command interpreter """


# Imporing Cmd module for command interpreter
from cmd import Cmd

# Importing basemodel to use it creating new objects
from models.base_model import BaseModel
from models import storage


class HBNBCommand(Cmd):
    """
    Entry point of the command interpreter
    """
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_EOF(self, arg):
        """ Quit using EOF character """
        return True

    def do_quit(self, arg):
        """ Quitting the cmd session """
        return True

    def emptyline(self):
        """ Handling empty line """
        pass

    def do_create(self, args):
        """ Creating new instance of a class """
        if not args:
            print("** class name missing **")
        elif args not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_model = BaseModel()
            storage.save()
            print(f"{new_model.id}")

    def do_show(self, args):
        """ Show object details """
        # Get all objects
        object_dict = storage.all()

        args = args.split(" ")
        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")

        else:
            # Set object and id
            class_name = args[0]
            object_id = args[1]

            if f"{class_name}.{object_id}" not in object_dict:
                print("** no instance found **")
            else:
                print(object_dict[f"{class_name}.{object_id}"])

    def do_destroy(self, args):
        """ destroy an object """
        # Get all objects
        object_dict = storage.all()

        args = args.split(" ")
        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")

        else:
            # Set object and id
            class_name = args[0]
            object_id = args[1]

            del object_dict[f"{class_name}.{object_id}"]
            storage.save()

    def do_all(self, args):
        """ Print string representation of all objects """
        args = args.split(" ")
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            object_list = []
            for object in storage.all().values():
                if len(args) > 0 and args[0] in object.__class__.__name__:
                    object_list.append(object.__str__())
                elif len(args) == 0:
                    object_list.append(object.__str__())
            print(object_list)

    def do_update(self, args):
        """ update <class name> <id> <attribute name> "<attribute value> """
        args = args.split(" ")
        objdict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if f"{args[0]}.{args[1]}" not in objdict.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            print("** value missing **")
            return False
        if len(args) == 4:
            # Start updating
            # Get the object from storage dictionary
            obj = objdict["{}.{}".format(args[0], args[1])]

            # Check if the attr name in the keys
            if args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = objdict["{}.{}".format(args[0], args[1])]
            for k, v in eval(args[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
