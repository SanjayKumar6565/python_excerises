#PyProg26.py
#Write a python program to check whether two lists are circularly identical.
def is_circularly_identical(list1, list2):
    # Check if both lists are of the same length
    if len(list1) != len(list2):
        return False

    # Concatenate the first list with itself to check circular identity
    circular_list1 = list1 + list1

    # Check if the second list is a substring of the concatenated list
    if all(item in circular_list1 for item in list2):
        return True
    else:
        return False

# Example usage:
list_a = list(map(int,input("enter the values of list1:-").split()))
list_b = list(map(int,input("enter the values of list2:-").split()))

if is_circularly_identical(list_a, list_b):
    print("The lists are circularly identical.")
else:
    print("The lists are not circularly identical.")