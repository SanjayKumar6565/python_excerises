#string2.py
"""2. A simple way to estimate the number of words in a string is to count the number of spaces in the
string. Write a program that asks the user for a string and returns an estimate of how many words
are in the string."""
string = input("Enter a String: ")
space_count = string.count(" ")
word_count = space_count+1
print(word_count)