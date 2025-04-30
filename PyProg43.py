#PyProg43.py
#Write a Python program to generate groups of five consecutive numbers in a list.
def generate_consecutive_groups(start, end):
    groups = []
    for i in range(start, end + 1):
        if i + 4 <= end:
            groups.append([i, i + 1, i + 2, i + 3, i + 4])
    return groups

start_number = int(input("Enter the starting number: "))
end_number = int(input("Enter the ending number: "))

groups = generate_consecutive_groups(start_number, end_number)

print("Groups of five consecutive numbers:")
for group in groups:
    print(group)
