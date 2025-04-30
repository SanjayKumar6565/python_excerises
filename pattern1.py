n=int(input("enter a number:- "))
for i in range(n):
    for j in range(n-i-1):
        print("0 ",end="")
    print(n-i)