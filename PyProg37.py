#PyProg37.py
"""
Write a Python program to change the position of every n-th value with the (n+1)th in a list.
	Sample list: [0,1,2,3,4,5]
	Expected Output: [1, 0, 3, 2, 5, 4]
"""
def swap_nth_with_next(lst, n):
    for i in range(0, len(lst)-1, n):
        if i + n < len(lst):
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

# Test the function
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 3
    modified_list = swap_nth_with_next(my_list, n)
    print("Modified List:", modified_list)
