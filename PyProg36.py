#PyProg36.py
#Write a Python program to find common items from two lists.
ls1 = list(input("Enter the list 1 of items:-").split())
ls2 = list(input("Enter the list 2 of items:-").split())
lst1 = set(ls1)
lst2 = set(ls2)
common_items = lst1.intersection(lst2)
print(common_items)