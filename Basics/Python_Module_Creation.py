"""
To define a module, simply use your text editor to create a new file with a .py extension.
All names assigned at the top level of the module become attributes of the module object and
can be exported for use in other modules by importing the module.

For instance, if you type the following def (function) add(a, b): in a file called mymodule.py,
you can import the add function into another module using the following import statement:

from Python_Module_Creation import add

Refer to Python_Import_Modules.py for more information on importing modules.

"""


def add(a, b):
    """
    This function adds two numbers
    :param a: int() or float()
    :param b: int() or float()
    :return: int() or float() - the sum of a and b
    """
    return a + b

def subtract(a, b):
    """
    This function subtracts two numbers
    :param a: int() or float()
    :param b: int() or float()
    :return: int() or float() - the difference of a and b
    """
    return a - b
