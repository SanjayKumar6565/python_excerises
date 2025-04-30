def hollow_rectangle(R, C):
    for i in range(R):
        for j in range(C):
            # Print '*' for the first row, last row, first column, or last column
            if i == 0 or i == R - 1 or j == 0 or j == C - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()  # Move to the next line after each row

# Input: Number of rows and columns
R = int(input())
C = int(input())

# Generate hollow rectangle
hollow_rectangle(R, C)
