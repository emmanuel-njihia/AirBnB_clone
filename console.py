#!/usr/bin/python3
"""Program contains the entry point of the command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exits the program by quit"""
        return True

    def do_EOF(self, arg):
        """Exits program by EOF"""
        return True

    def do_create(self, arg):
        """creates nwe BaseModel and saves it"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)
            except ImportError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in storage.all():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")


    def do_destroy(self, arg):
        """instance delete based on class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in storage.all():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not arg:
            print([str(obj) for obj in storage.all().values()])
        else:
            args = arg.split()
            if args[0] not in storage.all():
                print("** class doesn't exist **")
            else:
                instances = [str(obj) for key, obj in storage.all().items() if key.startswith(args[0])]
                print(instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in storage.all():
            print("** class doesn't exist ** ")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                instance = storage.all()[key]
                setattr(instance, args[2], args[3].strip('"'))
                instance.save()
            else:
                print("** no instance found **")

    def emptyline(self):
        """Does nothing on an empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
