#!/usr/bin/python3
"""
A program that conatins the entry point of the
command interpreter.

"""
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

def do_quit(self, arg):
    return True

def do_EOF(self, arg):
    return True

def emptyline(self):
    pass


if __name__ == '__main__':
    HBNBCommand(cmd.Cmd).cmdloop()
