#!/usr/bin/python3
"""
"""
import cmd
from models import storage  # import file_storage
from models.base_model import BaseModel  # import class model
from models.city import City  # import class City
from models.user import User  # import class User
from models.amenity import Amenity  # import class Amenity
from models.place import Place  # import class Place
from models.state import State  # import class State
from models.review import Review  # import class Review


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '
    __classes = ['BaseModel',
                 'Amenity',
                 'City',
                 'User',
                 'State',
                 'Place',
                 'Review']

    def do_quit(self, arg):
        """ exit """
        return True

    def do_EOF(self, arg):
        """ exit """
        print()
        return True

    def emptyline(self):
        """ emptyline """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
        """
        args = arg.split( )
        if not args:
            print('** class name missing **')
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            obj = eval(args[0])()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an
        instance based on the class name and id
        """
        args = arg.split( )
        k = "{}.{}".format(args[0],args[1])
        print(storage.all())
        for key, val in storage.all().items():
            if key == k:
                print(val.to_dict())
                return

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file).
        """
        pass

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name.
        """
        pass

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        """
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
