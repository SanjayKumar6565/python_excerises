#PyProg15.py
import random


def shuffle_and_print(input_list):
    random.shuffle(input_list)

    print("Shuffled List:", input_list)

#main prog
my_list = list(map(int,input("enter the list value :-").split()))
shuffle_and_print(my_list)
