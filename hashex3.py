#hashex3.py
# Read the input
n = int(input())
input_list = list(map(int, input().split()))

# Create the tuple
t = tuple(input_list)

# Compute and print the result of hash(t)
print(hash(t))
