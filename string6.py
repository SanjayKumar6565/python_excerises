#string6.py
""". At a certain school, student email addresses end with @student.college.edu, while professor
email addresses end with @prof.college.edu. Write a program that first asks the user how many
email addresses they will be entering, and then has the user enter those addresses. After all the
email addresses are entered, the program should print out a message indicating either that all the
addresses are student addresses or that there were some professor addresses entered."""

no_of_mail = int(input("How many email addresses will you enter?"))
student = 0
professor = 0

for _ in range(no_of_mail):
    email = input("Enter an email address: ")
    if email.endswith("@student.college.edu"):
        student += 1
    elif email.endswith("@prof.college.edu"):
        professor += 1

if professor == 0:
    print("all the email addresses are student addresses.")
else:
    print("Some email addresses are professor addresses.")