#PyProg42.py
# Write a Python program to split a list into different variables.
def variables(lst):
    for i, var in enumerate(lst):
        print(var)




#main program
lst=list(input("enter the list values:-").split())
print(variables(lst))