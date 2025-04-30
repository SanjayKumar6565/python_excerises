PyProg13.py
# Dimensions of the 3D array
depth = int(input("Enter the value of depth"))
rows = int(input("Enter the value of rows"))
cols = int(input("Enter the value of cols"))

three_d_array = [[[ '*' for _ in range(cols)] for _ in range(rows)] for _ in range(depth)]

for i in range(depth):
    for j in range(rows):
        for k in range(cols):
            print(three_d_array[i][j][k], end=" ")
        print()
    print()