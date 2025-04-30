#string8.py
""" Write a program that asks the user to enter a word and then capitalizes every other letter of that
word.
So if the user enters rhinoceros,
the program should print rHiNoCeRoS."""

string = input("enter the word:-")
cap_words = ''
for i in range(len(string)):
    if i % 2 == 1:
        cap_words += string[i].upper()
    else:
        cap_words += string[i]

print(cap_words)

