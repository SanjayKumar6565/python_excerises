#PyProg18.py
from itertools import permutations

def generate_permutations(input_list):
    all_permutations = permutations(input_list)


    for perm in all_permutations:
        print(perm)

# Example usage
my_list = list(map(int,input("enter the list values:").split()))
generate_permutations(my_list)
