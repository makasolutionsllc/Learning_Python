"""
Intoducing Python Statements:
1. Python is an imperative language, which means that it is built around statements.
2. A statement is an instruction that the Python interpreter can execute.
3. Statements are the core building blocks of a Python program.
4. Python statements are executed sequentially, one after another, from top to bottom.
5. Python statements are usually written one per line.
6. Python statements can span multiple lines if they are enclosed in parentheses, brackets, or braces.
7. Python statements can be grouped together in blocks, which are defined by indentation.
8. Python statements can be conditionally executed using if statements.
9. Python statements can be repeated using loops. i.e for and while loops.
10. Python statements can be defined in functions, which are reusable blocks of code.
11. Python statements can be defined in classes, which are reusable templates for objects.
"""

# Python Statements
#If Statements
# The if statement is used to conditionally execute a block of code. The block is executed only if the condition is true.
# The if statement can be followed by an optional else statement, which is executed if the condition is false.
# The if statement can be followed by an optional elif statement, which is executed if the condition is false.

# Example 1
if 1 < 2:
    print("1 is less than 2")
else:
    print("1 is not less than 2")

# Example 2
if 1 > 2:
    print("1 is greater than 2")
elif 1 < 2:
    print("1 is less than 2")
else:
    print("1 is equal to 2")

example_list = [1, 2, 3, 4, 5]
if 6 in example_list:
    print("6 is in the list")
else:
    print("6 is not in the list")

# Loops
# Loops are used to repeat a block of code a specified number of times, or until a condition is met.
# Python has two types of loops: for loops and while loops.
# For Loops
# The for loop is used to iterate over a sequence of objects, such as a list or a range of numbers.
# The for loop can be followed by an optional else statement, which is executed when the loop completes normally.
# The for loop can be exited prematurely using the break statement, or skipped to the next iteration using the continue statement.

# Example 1
for i in range(5): # range(5) returns a sequence of numbers from 0 to 4
    print(i) # Outputs 0, 1, 2, 3, 4


# Example 2
for i in range(5):
    if i == 3:
        break # Exits the loop when i is equal to 3
    print(i) # Outputs 0, 1, 2

# Example 3 Lets use the example_list from the previous example
for i in example_list:
    print(i) # Outputs 1, 2, 3, 4, 5

# Example 4
for i in example_list:
    if i == 3:
        print("Found 3")
        continue # Skips the rest of the loop when i is equal to 3

    elif i == 5:
        print("Found 5")
        break

    print(i) # Outputs 1, 2, Found 3, 4, Found 5


# While Loops
# The while loop is used to repeat a block of code until a condition is met.
# The while loop can be followed by an optional else statement, which is executed when the loop completes normally.
# The while loop can be exited prematurely using the break statement, or skipped to the next iteration using the continue statement.

# Example 1
i = 0
while i < 5:
    print(i)
    i += 1 # Increment i by 1

# Example 2
i = 0
while i < 5:
    if i == 3:
        break # Exits the loop when i is equal to 3
    print(i)
    i += 1 # Increment i by 1

# Example 3
i = 0
while i < 5:
    if i == 3:
        print("Found 3")
        i += 1 # Increment i by 1
        continue # Skips the rest of the loop when i is equal to 3
    print(i)
    i += 1 # Increment i by 1



