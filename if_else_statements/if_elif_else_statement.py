#!/usr/bin/python3

"""
This is just a simple program to show the use of Flow Control ( Working with conditions, true or false ).
Here we have two flow control statements, if , elif and else.
"""
name = input("Type your name please: ")

if name == "John":
    print("Hello dear %s, how have you been?" % name)


elif name == "Mary":
    print("Hey!, %s How have you been? I was expecting you!" % name)


else:
    print("Oh I'm sorry %s , I am expecting John and Mary." % name)

