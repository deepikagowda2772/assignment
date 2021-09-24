#!/usr/bin/env python
# coding: utf-8

# In[1]:


##Write a Python function to sum all the numbers in a list.

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))


# In[5]:


#Write a Python program to reverse a string.
def reverse_string(str):  
    str1 = ""   
    for i in str:  
        str1 = i + str1  
    return str1    
     
str = "1234abcd"
print("The original string is: ",str)  
print("The reverse string is",reverse_string(str))


# In[9]:


#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.


def upperlower(string):
    upper = 0
    lower = 0
    for i in range(len(string)):
          
        # For lower letters
        if (ord(string[i]) >= 97 and
            ord(string[i]) <= 122):
            lower += 1
  
        # For upper letters
        elif (ord(string[i]) >= 65 and
              ord(string[i]) <= 90):
            upper += 1
  
    print('Lower case characters = %s' %lower)
    print('Upper case characters = %s' %upper)
  
string = 'The quick Brow Fox'
upperlower(string)


# In[ ]:




