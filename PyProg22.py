#PyProg22.py
#Write a Python program to find the index of an item in a specified list.
try:
    lst = list(input("Enter the values :-").split())
    print(lst.index(input("enter the which element if you want:")))
except ValueError:
    print("You want The values are does not exists....")



