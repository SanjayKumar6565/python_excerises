#PyProg19.py
def get_list_difference(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    difference = set1.difference(set2)
    return list(difference)

# Example usage:
list1 = list(map(int,input("Enter the list 1 values").split()))
list2 = list(map(int,input("Enter the list 2 values").split()))
result = get_list_difference(list1, list2)
print("Difference:", result)
