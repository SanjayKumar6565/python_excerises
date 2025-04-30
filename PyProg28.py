#PyProg28.py
#Write a Python program to find the second largest number in a list.
lst = list(map(int,input("enter the list of elements:-").split()))
lst.sort()
print("the smallest second number in list is",lst[-2])
