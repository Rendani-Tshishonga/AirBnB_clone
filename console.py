#!/usr/bin/python3
"""
A program that conatins the entry point of the
command interpreter.

"""
import cmd
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

def do_quit(self, arg):
    return True

def do_EOF(self, arg):
    return True

def emptyline(self):
    pass

def do_create(self, arg):
    if arg == "":
        print("** class name missing **")
    elif arg not in storage.class_list():
        print("** class doesn't exist **")
    else:
        vari = storage.class_list()[arg]
        vari.save()
        print(vari.id)

def do_show(self, arg):
    if arg is None or arg == "":
        print("** class name missing **")
    arguments = arg.split(' ')
    elif arguments[0] is not in storage.class_list():
        print("** class doesn't exist **")
    elif arguments[1] is None:
        print("** instance id missing **")
    else:
        key_pam = "{}.{}".format(arguments[0], arguments[1])
        if key_pam is not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[key_pam])


 __name__ == '__main__':
    HBNBCommand(cmd.Cmd).cmdloop()
