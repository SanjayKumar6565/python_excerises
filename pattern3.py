n=int(input(" Enter the number:-"))
for i in range(n):
    for j in range(n):
        val = max(i,j,n-1-i,n-1-j)+1
        print(val, end="")
    print()