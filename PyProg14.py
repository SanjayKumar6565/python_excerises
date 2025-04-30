#PyProg14.py
lst = list(map(int,input("enter the list values:").split()))
for val in lst:
    if val % 2 == 0:
        lst2=lst.remove(val)
else:
    print(lst)

