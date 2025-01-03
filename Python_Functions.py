"""
Introducing Python Functions:
In simple terms, a function is a device that groups a set of statements, so they can be run more than
once in a program. Functions also can compute a result value and let us specify parameters that serve as function inputs
and may differ each time the code is run. Coding an operation as a function makes it a generally useful tool, which
we can use in a variety of contexts.
"""

# Defining Functions
# Functions are defined using the def keyword, followed by the function name, a set of parentheses, and a colon.
# The body of the function is indented.
# The return statement is used to return a value from the function.
# The return statement can be followed by an expression, which is evaluated and returned to the caller.
# If the return statement is not followed by an expression, None is returned.
# Functions can take parameters, which are specified in the parentheses following the function name.
# Parameters are used to pass values to the function.
# Parameters can have default values, which are used if the caller does not specify a value.
# Parameters can be passed by position or by name.
# Functions can return multiple values by returning a tuple.

# Example 1
def add(a, b):
    """
    This function adds two numbers
    :param a: int() or float()
    :param b: int() or float()
    :return: int() or float() - the sum of a and b
    """
    return a + b


# Example 2
def subtract(a, b):
    """
    This function subtracts two numbers
    :param a: int() or float()
    :param b: int() or float()
    :return: int() or float() - the difference of a and b
    """
    return a - b

def multiply(a, b):
    """
    This function multiplies two numbers
    :param a: int() or float()
    :param b: int() or float()
    :return: int() or float() - the product of a and b
    """
    return a * b

#using parameters with default values
def divide(a, b=1):
    """
    This function divides two numbers
    :param a: int() or float()
    :param b: int() or float()
    :return: int() or float() - the quotient of a and b
    """
    return a / b

# How to call a function
# To call a function, you use the function name followed by a set of parentheses.
# The arguments are specified in the parentheses.
# Example 1
print(add(1, 2)) # Outputs 3
print(subtract(3, 2)) # Outputs 1
print(multiply(2, 3)) # Outputs 6
print(divide(6, 2)) # Outputs 3
print(divide(6)) # Outputs 6 - b has a default value of 1


#Advanced Function Concepts
#Example 1

def add(*args):
    """
    This function adds any number of arguments
    :param args: int() or float()
    :return: int() or float() - the sum of all the arguments
    """
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 4, 5)) # Outputs 15

#Example 2
def build_profile(**kwargs): # **kwargs is a dictionary
    """
    This function builds a profile from keyword arguments
    :param kwargs: dict() - keyword arguments
    :return: dict() - a dictionary containing the keyword arguments
    """
    return kwargs

print(build_profile(name='Alice', age=25, city='New York')) # Outputs {'name': 'Alice', 'age': 25, 'city': 'New York'}


#Example 3
example_list = [1, 2, 3, 4, 5]

def using_list_with_statements(example):
    """
    This function demonstrates using a list with statements
    it will create a new list with a multiplication of 2 for each element in the example list
    :param example: list() - a list of integers
    :return: list() - a new list with the elements of the example list multiplied by 2
    """
    new_list = []
    for i in example:
        new_list.append(i * 2)
    return new_list
    