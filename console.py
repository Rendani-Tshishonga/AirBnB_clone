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
    else: 
        arguments = arg.split(' ')
        if arguments[0] not in storage.class_list():
            print("** class doesn't exist **")
        elif arguments[1] is None:
            print("** instance id missing **")
        else:
            key_pam = "{}.{}".format(arguments[0], arguments[1])
            if key_pam not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key_pam])

def do_destroy(self, arg):
    """
    Deletes an instance based on the class name and id,
    save the change into the JSON file
    """
    if arg is None:
        print("** class name missing **")
    else:
        argument = arg.split(' ')
        if argument[0] not in storage.class_list():
            print("** class doesn't exist **")
        elif argument[1] is None:
            print("** instance id missing **")
        else:
            key_param = "{}.{}".format(argument[0], argument[1])
            if key_param not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key_param]
                storage.save()


def do_all(self, arg):
    if arg is not None:
        argument = arg.split(' ')
        if argument[0] not in storage.class_list():
            print("** class doesn't exist **")
        else:
            object_list = [str(obj) for key, obj in storage.all().items() if\
                    type(obj).__name__ == argument[0]
            print(object_list)
    """ Make provision for the all command """
    else:
        object_list_1 = [str(obj) for key, obj in storage.all().items()]
        print(object_list)
        
if __name__ == '__main__':
    HBNBCommand(cmd.Cmd).cmdloop()
