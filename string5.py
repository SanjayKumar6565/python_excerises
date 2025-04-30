#string5.py
"""6. Write a program that asks the user to enter a word and determines whether the word is a
palindrome or not. A palindrome is a word that reads the same backwards as forwards"""

string = input("enter the a word:-")

if string == string[::-1]:
    print("The word is Palindrome.")
else:
    print("The word is not a palindrome.")
