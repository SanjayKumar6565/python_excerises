#PyProg35.py
#Write a Python program to get variable unique identification number or string.
def unqiue(val):
    return id(val)
#main program
val = input("Enter the Numbers & Strings")

print(unqiue(val))