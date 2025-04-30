#PyProg32.py
#Write a Python program to check whether a list contains a sublist.
def is_sublist(lst, sublst):

    sub_len = len(sublst)

    
    for i in range(len(lst) - sub_len + 1):

        if lst[i:i + sub_len] == sublst:
            return True


    return False


# Example usage
main_list = list(map(int,input("Enter the list values :-").split()))
sub_list = list(map(int,input("enter the sub list values :-").split()))
print(is_sublist(main_list, sub_list))
