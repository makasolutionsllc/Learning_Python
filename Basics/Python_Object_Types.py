"""
From a more concrete perspective, Python programs can be decomposed into modules, statements, expressions, and objects, as follows:
1. Programs are composed of modules.
2. Modules contain statements.
3. Statements contain expressions.
4. Expressions create and process objects.

In C or C++, centers on implementing objects - also known as data structures - to represent the components in your applications
domain. You have to declare the structure of each object in your program which could be tedious and error-prone.

Python, on the other hand, is built around objects. Each object can be classified as a type. Python's types automatically provide
powerful and flexible operations that are (mostly) consistent with the object's type. This means that you can focus on the objects
in your application, and the relationships between them, rather than on the implementation of the objects themselves.

"""


# Python Object Types
# Strings: A sequence of characters enclosed in quotes
# Numbers: Two types: integers and floating-point numbers
# Lists: A sequence of objects
# Dictionaries: A collection of objects stored by key
# Tuples: An immutable sequence of objects
# Files: A sequence of characters stored on the disk
# Sets: An unordered collection of unique objects
# Other core types: Booleans, types, None

this_is_a_string = "This is a string"
this_is_an_integer = 42
this_is_a_float = 3.14159
this_is_a_list = [1, 2, 3, 4, 5]
this_is_a_dictionary = {'key1': 'value1', 'key2': 'value2'}
this_is_a_tuple = (1, 2, 3, 4, 5)

# Now each of these objects can be manipulated in various ways. For example, you can concatenate strings, add numbers, and index
# into lists. You can also perform more advanced operations, such as sorting lists, and searching for substrings. The operations
# that are defined for each object are determined by its type.

#Strings
this_is_a_string.lower() # Returns a lowercase version of the string
this_is_a_string.upper() # Returns an uppercase version of the string
this_is_a_string + " that has been concatenated" # outputs "This is a string that has been concatenated"
this_is_a_string[0] # Returns the first character of the string "T"
f"Hello, {this_is_a_string}" # Outputs "Hello, This is a string" - f-strings are a way to format strings in Python

#Numbers
this_is_an_integer + 1 # Outputs 43
this_is_a_float * 2 # Outputs 6.28318
this_is_an_integer / 2 # Outputs 21.0 - Python 3 always returns a floating-point number when dividing
this_is_an_integer // 2 # Outputs 21 - Integer division
this_is_an_integer % 2 # Outputs 0 - Modulus operator

#Lists
this_is_a_list.append(6) # Adds 6 to the end of the list
this_is_a_list.pop() # Removes the last item from the list
this_is_a_list.sort() # Sorts the list
this_is_a_list.reverse() # Reverses the list
this_is_a_list[0] # Returns the first item in the list output: 1
this_is_a_list[1:3] # Returns a slice of the list output: [2, 3]
this_is_a_list.index(3) # Returns the index of the first occurrence of 3 in the list output: 2


#Dictionaries
# Dictionaries are unordered collections of objects that are stored by key. You can use a key to retrieve the object that is stored.
this_is_a_dictionary['key1'] # Returns 'value1'
this_is_a_dictionary.keys() # Returns a list of all the keys in the dictionary
this_is_a_dictionary.values() # Returns a list of all the values in the dictionary
this_is_a_dictionary.items() # Returns a list of key-value pairs in the dictionary

#Tuples
# Tuples are immutable sequences of objects. Once you create a tuple, you cannot change it.
this_is_a_tuple[0] # Returns 1
this_is_a_tuple[1:3] # Returns (2, 3)
this_is_a_tuple.index(3) # Returns the index of 3 in the tuple output: 2
this_is_a_tuple.count(3) # Returns the number of times 3 appears in the tuple output

#Files
# Files are objects that represent sequences of characters stored on the disk.
file = open('example.txt', 'w') # Open a file for writing
file.write('This is a test') # Write to the file
file.close() # Close the file
file = open('example.txt', 'r') # Open the file for reading
content = file.read() # Read the contents of the file
file.close() # Close the file

#Sets
# Sets are unordered collections of unique objects. You can use sets to test for membership, and to perform common mathematical
# operations on sets such as union, intersection, difference, and symmetric difference.
this_is_a_set = {1, 2, 3, 4, 5}
this_is_a_set.add(6) # Adds 6 to the set output: {1, 2, 3, 4, 5, 6}
this_is_a_set.remove(6) # Removes 6 from the set output: {1, 2, 3, 4, 5}
this_is_a_set.union({6, 7, 8}) # Returns the union of the two sets output: {1, 2, 3, 4, 5, 6, 7, 8}
this_is_a_set.intersection({4, 5, 6}) # Returns the intersection of the two sets output: {4, 5}
this_is_a_set.difference({4, 5, 6}) # Returns the difference of the two sets output: {1, 2, 3}



