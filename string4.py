#string4.py
"""Write a program that asks the user to enter a string. The program should create a new string called
new_string from the user’s string such that the second character is changed to an asterisk and three
exclamation points are attached to the end of the string. Finally, print new_string.
Typical output is shown below:
Enter your string: Qbert
Output: Q*ert!!!"""

string = input("enter the string :-")
if len(string) < 2:
    print("You enter the string is too short ")
else:
    new_str = string[0]+"*"+string[2:]+"!!!"
    print("the modified the string is :",new_str)