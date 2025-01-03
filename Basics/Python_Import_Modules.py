"""
Introducing importing modules:
Modules are imported using the import keyword. The import keyword is followed by the name of the module you want to import.
You can import a module by name, or you can import specific attributes from a module.
You can also import a module using an alias.
You can import all attributes from a module using the * operator.
You can import specific attributes from a module using the from keyword.
"""

# Example 1
import Python_Module_Creation # Imports the entire module
Python_Module_Creation.add(1, 2) # Outputs 3
from Python_Module_Creation import add # Imports the add function from the module
add(1, 2) # Outputs 3
import Python_Module_Creation as pmc # Imports the module using an alias
pmc.add(1, 2) # Outputs 3
from Python_Module_Creation import * # Imports all attributes from the module