# -*- coding: utf-8 -*-
"""user_input.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Z0xX4GFQ299fClLpu9RbZR0y33fHWz98
"""

#Write a program that asks the user for their name, age, and location and then prints out a personalized message.




#Instructions:
#Create a new Python file and name it "user_input.py"
#Use the input() function to ask the user for their name and store it in a variable called "name".
#Use the input() function to ask the user for their age and store it in a variable called "age".
#Use the input() function to ask the user for their location and store it in a variable called "location".
#Print out a personalized message using the user's name, age, and location. For example: "Hello [name], you are [age] years old and live in [location]."
#Save and run the program to see the output.

Name = input("What is your name?")
Age = input("How old are you?")
Location = input("Where do you live?")

print(f'Hello {Name},you are {Age} years old and live in {Location},')