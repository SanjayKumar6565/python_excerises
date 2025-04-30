#PyProg30.py
#Write a Python program to count the number of elements in a list within a specified range.

from collections import Counter


def get_frequency(lst):
    return Counter(lst)


if __name__ == "__main__":
    # Example list
    my_list = list(map(int,input("Enter the Elements:-").split()))

    # Get frequency of elements
    frequencies = get_frequency(my_list)

    # Print the frequencies
    for element, frequency in frequencies.items():
        print("The Elements {} Frequency is {}".format(element,frequency))