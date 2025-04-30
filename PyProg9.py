#PyProg9.py
lst = list(input("enter the list values:").split())
lst1 = lst#deep copy
print("This is list (deep copy) copied list of you entered{}".format(lst1))
print("="*70)
lst2 = lst.copy()
print("This is the (shallow copy) copied list of you entered{}".format(lst2))
print("="*70)