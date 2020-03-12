#!/bin/python3
import re

s1 = "Hello"
s2 = "World"
#Complete the twoStrings function below.
def twoStrings(s1, s2):
    str1 = re.findall("[A-Za-z]", s1) # split the word to the letters 
    result = re.search(str(str1), s2) # search the letters in s2 
    if bool(result) == True:
        return "Yes"
    elif bool(result) == False:
        return "No" 

print(twoStrings(s1, s2))
