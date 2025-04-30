#PyProg11.py
lst1 = list(input("Enter the list 1 values:").split())
lst2 = list(input("Enter the list 2 values:").split())
for val in lst1:
    if val in lst2:
        print("True")
    else:
        print("False")
