#hashex2.py
if __name__ == '__main__':
    n = int(input("Enter the number of elements in the tuple: "))
    elements = tuple(map(int, input("Enter space-separated integers: ").split()))

    # Using the hash function to compute the hash value of the tuple
    result = hash(elements)

    print(result)

