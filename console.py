#!/usr/bin/python3
"""
Module: console.py
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for HBNB project.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program when EOF is reached (Ctrl+D)
        """
        print()
        return True

    def emptyline(self):
        """
        Called when an empty line is entered.
        """
        pass

    def help_quit(self):
        """
        Print help message for quit command.
        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        Print help message for EOF (Ctrl+D) command.
        """
        print("Exit the program when EOF is reached (Ctrl+D)")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
