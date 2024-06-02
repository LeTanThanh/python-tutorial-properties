from person import Person

# Python Property

## Introduction to class properties

"""
The following defines a Person class that has two attributes name and age, and create a new instance of the Person class:
"""

john = Person("John", 18)
# print(john.age)

"""
Since age is the instance attribute of the Person class, you can assign it a new value like this:
"""

john.age = 19
# print(john.age)

"""
The following assignment is also technically valid:
"""

john.age = -1

"""
However, the age is semantically incorrect.

To ensure that the age is not zero or negative, you use the if statement to add a check as follows:
"""

age = -1
if age <= 0:
  raise ValueError("The age must be positive")
else:
  pass
  # john.age = age
"""
And you need to do this every time you want to assign a value to the age attribute.
This is repetitive and difficult to maintain.

To avoid this repetition, you can define a pair of methods called getter and setter.
"""

## Getter and setter

"""
The getter and setter methods provide an interface for accessing an instance attribute:

- The getter returns the value of an attribute

- The setter sets a new value for an attribute

In our example, you can make the age attribute private (by convention) and define a getter and a setter to manipulate the age attribute.

The following shows the new Person class with a getter and setter for the age attribute:
"""

"""
How it works.

In the Person class, the set_age() is the setter and the get_age() is the getter.
By convention the getter and setter have the following name get_<attribute>() and set_<attribute>():

In the set_age() method, we raise a ValueError is the age is less than or equal to zero.
Otherwise, we assign the age argument to the _age attribute:

The get_age() method returns the value of the _age attribute:

In the __init__() method, we call the set_age() setter method to initialize the _age attribute:

The following attempts to assign an invalid value to the age attribute
"""

john = Person("John", 18)
john.set_age(-19)

"""
And Python issued a ValueError as expected.

This code works just fine. But it has a backward compatibility issue.

Suppose you released the Person class for a while and other developers have been already using it.

And now you add the getter and setter, all the code that uses the Person won't work anymore.

To define a getter and setter method while achieving backward compatibility, you can use the property() class.
"""
