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
    elif arg != storage.class_list():
        print("** class doesn't exist **")
    else:
        
    


 __name__ == '__main__':
    HBNBCommand(cmd.Cmd).cmdloop()
