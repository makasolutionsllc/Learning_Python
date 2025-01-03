"""
Classes are pythons main object-oriented programming (OOP) tool. OOP offers as a different and often more
effective way of programming, in which we factor code to minimize redundancy, and write new programs by customizing
existing code instead of changing  it in place.

General syntax for defining a class is:
Class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>


Uses for classes:
- Representing complex data structures
- Representing real-world objects
- Simplifying code
"""

# Example 1: Creating a class
class StarlyteEmployee:
    # Class variable
    company = "Starlyte"
    def __init__(self, name, age, role): # Constructor
        #Constructor is a special method that is called when an object is created
        #from a class. It allows the class to initialize (assign values to) the object's attributes.
        # Instance variables
        self.name = name # Name of the employee
        self.age = age # Age of the employee
        self.role = role # Role of the employee
        self.phone_number = None # Phone number of the employee
        self.email = None
        self.address = None

    def __repr__(self): # Special method that returns a string representation of the object
        return f"Name: {self.name}, Age: {self.age}, Role: {self.role}, Company: {self.company}"

    def change_company(self, new_company):
        self.company = new_company

    def change_role(self, new_role):
        self.role = new_role

    def change_name(self, new_name):
        self.name = new_name

    def change_age(self, new_age):
        self.age = new_age

    def change_email(self, new_email):
        self.email = new_email

    def change_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number

    def change_address(self, new_address):
        self.address = new_address



# Creating an object of the class
# emp1 = StarlyteEmployee("John", 25, "Software Engineer")
# emp2 = StarlyteEmployee("Jane", 30, "Data Scientist")

# Accessing the attributes of the object
# print(emp1.name)
# print(emp1.age)
# print(emp1.role)
# print(emp1.company)


#You can create another class that inherits from the parent class

class StarlyteManager(StarlyteEmployee):
    def __init__(self, name, age, role, team): # Constructor
        super().__init__(name, age, role) # Call the constructor of the parent class and inherit its attributes such as name, age and role etc.
        self.team = team

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Role: {self.role}, Company: {self.company}, Team: {self.team}"

    def change_team(self, new_team):
        self.team = new_team


# Creating an object of the class

# manager1 = StarlyteManager("Mike", 35, "Manager", "Data Science")
# print(manager1)
# print(manager1.company)
# print(manager1.team)

class StarlyteDevelopmentTeam(StarlyteManager):
    """
    This class inherits from the StarlyteManager class and adds a new attribute called project
    This will hold the project that the development team is working on, in addition a dictionary
    called team_members is added to hold the members of the team
    """
    def __init__(self, name, age, role, team, project):
        super().__init__(name, age, role, team)
        self.project = project
        self.team_members = {}

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Role: {self.role}, Company: {self.company}, Team: {self.team}, Project: {self.project}, Team Members: {self.team_members}"

    def change_project(self, new_project):
        self.project = new_project


    def add_team_member(self, member: StarlyteEmployee):
        if isinstance(member, StarlyteEmployee): #we want to make sure the member is an instance of the StarlyteEmployee class
            self.team_members[member.name] = member.role

        else:
            raise ValueError("The member must be an instance of the StarlyteEmployee") #This will be discussed in the exception handling section

    def remove_team_member(self, member):
        del self.team_members[member.name]

    def change_team_member_role(self, member, new_role):
        self.team_members[member.name] = new_role



# Creating an object of the class
# Engineering_team = StarlyteDevelopmentTeam("Tom", 40, "Engineering Manager", "Engineering", "Data Pipeline")
# print(Engineering_team)
# print(Engineering_team.company)
# Engineering_team.add_team_member(emp1)
# print(Engineering_team.team_members)