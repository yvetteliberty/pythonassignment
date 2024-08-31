#!/usr/bin/env python
# coding: utf-8

# Create a Python class named Person.
# The Person class should have the following attributes:
# name: representing the person's name.
# age: representing the person's age.
# gender: representing the person's gender.
# Implement a method called introduce that prints a message introducing the person with their name, age, and gender.
# Create an instance of the Person class and call the introduce method to display the person's information.
# Create a GitHub repository for your assignment and submit the link.

# In[6]:


class Person:
   def __init__(self,name,age,gender):
       self.name = name
       self.age= age
       self.gender = gender
  
   def introduce(self):
       print(f"Hi, my name is {self.name}, I am {self.age} years old, and I am {self.gender}.")

# Create an instance of the Person class

person1=Person("Yvette", 30, "female")
person1.name
person1.age
person1.gender

# Call the introduce method
person1.introduce()


# In[ ]:




