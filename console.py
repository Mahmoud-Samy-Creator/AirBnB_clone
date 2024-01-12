#!/usr/bin/python3
""" Entry point of the command interpreter """


# Imporing Cmd module for command interpreter
from cmd import Cmd

class HBNBCommand(Cmd):
    """
    Entry point of the command interpreter
    """
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """ Quit using EOF character """
        return True

    def do_quit(self, arg):
        """ Quitting the cmd session """
        return True

    def emptyline(self):
        """ Handling empty line """
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
