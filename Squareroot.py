SquareN.py
n=int(input("Enter How Many Mul tables u want:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    for num in range(1,n+1): # Outer Loop supply the Number for gen Mul table
        print(