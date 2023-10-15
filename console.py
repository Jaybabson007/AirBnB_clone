#!/usr/bin/python3
"""This python script contains the main entry point of the command interpreter.

It uses the module cmd.
The class definition is: class HBNBCommand(cmd.Cmd):
The command interpreter implements:quit and EOF to exit the program,
help (this action is provided by default by cmd but you should keep it
updated and documented as you work through tasks),
a custom prompt: (hbnb),
an empty line + ENTER shouldn’t execute anything.
"""

import cmd
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
import shlex

class HBNBCommand(cmd.Cmd):
    """The class blueprint for the command processor.

    Args:
        cmd (_type_): _description_
    """
    prompt = "(hbnb) "
    classes_list = ["BaseModel", "User", "State", "City", "Amenity",
                    "Place", "Review"]
    commands_list = ["create", "show", "all", "destroy", "update", "count"]

    def do_quit(self, args):
        """This function defines the Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """This function defines the EOF command to exit the program
        """
        return True

    def emptyline(self):
        """This function defines an empty line. It shouldn't execute anything
        """
        pass

    def do_create(self, inp):
        """This functon creates a new instance of BaseModel, and saves it (to the JSON
        file) then prints the id.

        Args:
            class_name (class): The name of current class.
        """
        args = inp.split()
        if not self.class_verification(args):
            return

        inst = eval(str(args[0]) + '()')
        if not isinstance(inst, BaseModel):
            return
        inst.save()
        print(inst.id)

    def do_show(self, inp):
        """This function prints the string representation of an instance based on the
        class name and id.
        """
        args = inp.split()

        if not self.class_verification(args):
            return

        if not self.id_verification(args):
            return

        string_key = str(args[0]) + '.' + str(args[1])
        objects = models.storage.all()
        print(objects[string_key])

    @classmethod
    def class_verification(cls, args):
        """This function verifies class and checks if it is in the class list.

        Returns:
            boolean: Returns True or false pending on status of class.
        """
        if len(args) == 0:
            print("** class name missing **")
            return False

        if args[0] not in cls.classes_list:
            print("** class doesn't exist **")
            return False

        return True

    @staticmethod
    def id_verification(args):
        """This function verifies the id of class.

        Returns:
            boolean: Returns True or False pending on status of id.
        """
        if len(args) < 2:
            print("** instance id missing **")
            return False

        objects = models.storage.all()
        string_key = str(args[0]) + '.' + str(args[1])
        if string_key not in objects.keys():
            print("** no instance found **")
            return False

        return True

    def do_destroy(self, inp):
        """This function deletes an instance based on the class name and id (it saves the
        changes into the JSON file).
        """
        args = inp.split()
        if not self.class_verification(args):
            return
        if not self.id_verification(args):
            return
        string_key = str(args[0]) + '.' + str(args[1])
        objects = models.storage.all()
        models.storage.delete(objects[string_key])
        models.storage.save()

    def do_all(self, inp):
        """ This function prints all the string representation of all instances based or not
        on the class name.
        """
        args = inp.split()
        all_objects = models.storage.all()
        list_ = []
        if len(args) == 0:
            # print all classes
            for value in all_objects.values():
                list_.append(str(value))
        elif args[0] in self.classes_list:
            # print just arg[0] class instances
            for (key, value) in all_objects.items():
                if args[0] in key:
                    list_.append(str(value))
        else:
            print("** class doesn't exist **")
            return False
        print(list_)

    def do_update(self, line):
        """ This function updates an instance based on the class name and id by adding or
        updating attribute (it saves the changes into the JSON file).
        """
        act = ""
        for argv in line.split(','):
            act = act + argv
        args = shlex.split(act)
        if not self.class_verification(args):
            return
        if not self.id_verification(args):
            return
        if not self.attribute_verification(args):
            return
        all_objects = models.storage.all()
        for key, value in all_objects.items():
            object_name = value.__class__.__name__
            object_id = value.id
            if object_name == args[0] and object_id == args[1].strip('"'):
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    setattr(value, args[2], args[3])
                    models.storage.save()
                return

    def precmd(self, arg):
        """This function Hooks before the command is run.
        If the self.block_command returns True, the command doesn't run.
        else, it is run.
        """
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            command = cls[1].split('(')
            args = command[1].split(')')
            if cls[0] in HBNBCommand.classes_list and command[0] \
                    in HBNBCommand.commands_list:
                arg = command[0] + ' ' + cls[0] + ' ' + args[0]
        return arg

    def do_count(self, class_name):
        """This function retrieves the number of instances of a class.
        """
        count = 0
        all_objects = models.storage.all()
        for key, value in all_objects.items():
            keys_split = key.split('.')
            if keys_split[0] == class_name:
                count += 1
        print(count)

    @staticmethod
    def attribute_verification(args):
        """This function verifies attributes.
        """
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        if len(args) < 4:
            print("** value missing **")
            return False
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
