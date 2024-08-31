#!/usr/bin/env python
# coding: utf-8

# Tasks:
# 
# File Creation:
# Create a Python script (file_handling_assignment.py) that does the following:
# Creates a new text file named "my_file.txt" in write mode ('w').
# Write at least three lines of text to the file, including a mix of strings and numbers.
# 
# 
# File Reading and Display:
# Enhance your script to read the contents of "my_file.txt" and display them on the console.
# 
# 
# File Appending:
# Modify the script to open "my_file.txt" in append mode ('a').
# Append three additional lines of text to the existing content.
# 
# 
# Error Handling:
# Implement error handling using try, except, and finally blocks to manage potential file-related exceptions (e.g., FileNotFoundError, PermissionError).

# In[69]:


#Task 1and 2

file = open("my_file.txt","r+")
file.write("This is the first line of code.\n")
file.write("Here is a number :42\n")
file.write("I am loving this.")
file.seek(0)
contents = file.read()
print(contents)


# In[94]:


# Appending to the file
file = open("my_file.txt", 'a') 
file.write("\nThis is an appended line.\n")
file.write("Another line added in append mode.\n")
file.write("Final appended line.")

print("Three lines appended to 'my_file.txt' successfully.")

# Reading and displaying the entire content (optional)
file = open("my_file.txt", 'r') 
content = file.read()
print("\nFull contents of 'my_file.txt':")
print(content)


# In[83]:


#Task 4

try:
    # Appending to the file
    file = open("my_file.txt", 'a') 
    file.write("\nThis is an appended line.\n")
    file.write("Another line added in append mode.\n")
    file.write("Final appended line.")

    print("Three lines appended to 'my_file.txt' successfully.")

except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except PermissionError:
    print("Error: You don't have permission to modify 'my_file.txt'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File operations completed.")

# Reading and displaying the entire content (optional)
try:
    file = open("my_file.txt", 'r') 
    content = file.read()
    print("\nFull contents of 'my_file.txt':")
    print(content)
except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")


# In[ ]:





# In[ ]:




