#!/usr/bin/python3
"""
A program that conatins the entry point of the
command interpreter.

"""
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    """ EOF character to exit the program """
    do_EOF = do_quit()

def do_quit(self, arg):
    return True
