#PyProg41.py
#Write a Python program to find missing and additional values in two lists.
	#Sample data : Missing values in second list: b,a,c
	#Additional values in second list: g,h
def missing_and_additional(lst1, lst2):


    missing = [x for x in lst1 if x not in lst2]
    additional = [x for x in lst2 if x not in lst1]

    return missing, additional

# Sample data
lst1 = list(input("enter the values in list1:-").split())
lst2 = list(input("enter the values in list2:-").split())

missing, additional = missing_and_additional(lst1, lst2)

print("Missing values in second list:", ", ".join(missing))
print("Additional values in second list:", ", ".join(additional))