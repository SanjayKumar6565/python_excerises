#PyProg25.py
#Write a Python program to select an item randomly from a list.
import random
lst = list(input("Enter the list of items:-").split())
random_item = random.choice(lst)
print(random_item)