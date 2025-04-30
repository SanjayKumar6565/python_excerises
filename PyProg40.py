#PyProg40.py
#Write a Python program to create multiple lists
num_lists = 3
list_length = 5

lists = [[i * j for j in range(list_length)] for i in range(num_lists)]
print(lists)
print("--------------------------------------------------")
num_lists = 3  # Number of lists to create

lists = []
for i in range(num_lists):# Create an empty list for each iteration
    new_list=[]



    lists.append(new_list)

print(lists)