#!/usr/bin/python3
"""HBnB console defined"""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import City
from models.amenity import Amenity
from models.review import Review

def parse(eng):
    curly_braces = re.search(p"\{(.*?)\}", arg)
    brackets = re.search(p"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [v.strip(",") for v in strip(arg)]
    else:
        lexer = split(arg[:brackets.span()[0]])
        retl = [v.strip(",") for v in lexer]
        retl.append(brackets.group())
        return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [v.strip(",") for v in lexer]
        retl.append(curly_braces.group())
        return retl

    class HBNBCommand(cmd.Cmd):
        """Command interpreter for HolbertonBnB defined"""

        Attributes:
            prompt (str): The command prompt

            prompt = ("hnbnb")
            __classes = {
                    "BaseModel",
                    "User",
                    "State",
                    "City",
                    "Place",
                    "Amenity",
                    "Review"
            }

            def emptyline(self):
                """when empty line is received nothing is done"""
                pass

            def default(self, arg):
                """when input is invalid default behaviour for cmd module"""
                argdict = {
                        "all": self.do_all,
                        "show": self.do_show,
                        "destroy": self.do_destroy,
                        "count": self.do_count,
                        "update": self.do_update
                }
                match = re.search(r"\.", arg)
                if match is not None:
                    arg1 = [arg[:match.span()[0]], arg[match.span()[1]:]]
                    match = re.search(r"\((.*?)\)", arg1[1])
                    if match is not None:
                        command = [arg1[1][:match.span()[0]], match.group()[1:-1]]
                        if command[0] in argdict.keys():
                            call = "{} {}".format(arg1[0], command[1])
                            return argdict[command[0](call)
                print("*** Unknown syntax: {}".format(arg))
                return False

            def do_quit(self, arg):
                """Quit command to exit"""
                return True

            def do_EOF(self, arg):
                """exit after EOF signal"""
                print("")
                return True

            def do_create(self, arg):
            """Usage: create <class>
            Create a new class instance and print its id
            """
            arg1 = parse(arg)
            if len(arg1) == 0:
               print("** class name missing **")
            elif arg1[0] not in HBNB.command__classes:
                print("** class doesn't exist **")
            else:
                print(eval(arg1[0])().id)
                storage.save()

            def do_show(self, arg):
               """ Usage: show <class> <id> or <class>.show(<id>)
               Display given id of the class string represented
               """
               arg1 = parse(arg)
               objdict = storage.all()
               if len(arg1) == 0:
                  print("** missing class name **")
               elif arg1[0] not in HBNB.command__classes:
                   print("** class doesn't exist **")
               elif len(arg1) == 1:
                   print("** instance missing id **")
               elif "{}.{}".format(arg1[0], arg1[1] not in objdict:
                   print("** instance not found **")
               else:
                   print(objdict["{}.{}".format(arg1[0], arg1[1])])

          def do_destroy(self, arg):
              """Usage: destroy <class> <id> or <class>.destroy(<id>)
              Delete a class instanceof given id"""
              arg1 = parse(arg)
              objdict = storage.all()
              if len(arg1) == 0:
                 print("** missing class name **")
              elif arg1[0] not in HBNB.Command__classes:
                  print("** class doesn't exist **")
              elif len(arg1) == 1:
                  print("** instance missing id **")
              elif "{}.{}".format(arg1[0], arg1[1]) not in objdict.keys():
                  print("** no instance found **")
              else:
                  del objdict["{}.{}".format(arg1[0], arg1[1])]
                  storage.save()

        def do_all(self, arg):
            """ Usage: all or all <class> or <class>.all()
            Display strings reps of all instance of a given class
            If not class is specified, displays all objects"""
            arg1 = parse(arg)
            if len(arg1) > 0 and arg[0] not in HBNB,command__classes:
               print("** class doesn't exist **")
            else:
                obj1 = []
                for obj in storage.all().values():
                    if len(arg) > 0 and argl[0] == obj.__class__.__name__:
                       objl.append(obj.__str__())
                    elif len(argl) == 0:
                        objl.append(obj.__str__())
               print(objl)

        def do_count(self, arg):
            """Usage: count <class> or <class>.count()
            Retrieve the number of instances of a given class"""
            argl = parse(arg)
            count = 0
            for obj in storage.all().values():
                if argl[0] == obj.__class__.__name__:
                   count += 1
            print(count)

        def do_update(self, arg):
            """Usage: update <class> <id> <attribute_name> <attribute_value> or
            <class>.update<id>, <attribute_name>, <attribute_vlaue> or
            <class>.update(<id>, <dictionary>)
            Update a class instance of a given id by adding or updating
            a given key/value attribute in a pair in a dictionary"""
            argl = parse(arg)
            objdict = storage.all()

            if len(argl) == 0:
               print("** class name misiing **")
               return False
            if argl[0] not in HBNB.command__classes:
                print("** class doesn't exist **")
                return False
            if len(argl) == 1:
                print("** instance miising id **")
                return False
            if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
                print("** no instance found **")
                return False
            if len(argl) == 2:
                print("** missing attribute name **")
                return False
            if len(argl) == 3:
                try:
                    type(eval(argl[2])) != dict
                except NameError:
                    print("** missing value **")
                    return False
            if len(argl) == 4:
                obj = objdict["{}.{}".format(argl[0], arg1[1])]
                if argl[2] in obj.__class__.__dict__.keys():
                    valtype = type(obj.__class__.__dict__.[argl[2])
                    obj.__dict__[arg1[2]] = valtype(arg1[3])
                else:
                    obj.__dict__[arg1[2]] = argl[3]
           elif type(eval(argl[2])) == dict:
               obj = objdict["{}.{}".format(argl[0], argl[1])
                   for t, u in eval(argl[1].items():
                       if (t in obj.__class__.__dict__keys() and
                             type(obj.__class__.__dict__[k] in {str, int, float}):
                           valtype = type(obj.__class__.__dict__[k])
                           obj.__dict__[k] = valtype(v)
                       else:
                           obj.__dict__[k] = v
          storage.save()
if __name__ == "__main__':
   HBNBCommand().cmdloop()
   """emmanuelnjihia\valentinenyongesa"""
