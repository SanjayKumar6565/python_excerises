def hollow_rectangle(R, C):
    # Loop over each row
    for i in range(1, R+1):
        # For the first and last row, print a complete line of stars
        if i == 1 or i == R:
            print('* ' * C)
        else:
            # For the middle rows, print stars at the beginning and end, with spaces in between
            print('*' + '  ' * (C-2) + ' *')

# Sample Input
R, C = map(int, input().split())
hollow_rectangle(R, C)
