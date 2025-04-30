#Program generating 1 to n  mul tables where n is +ve
#InnerLoopEx5.py
n=int(input("Enter How Many Mul tables u want:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    for num in range(1,n+1): # Outer Loop supply the Number for gen Mul table
        print("------------------------------------------")
        print("Mult Table for {}".format(num))
        print("------------------------------------------")
        for i in range(1,11): # Inner loop--generates for Mul table for that number supplied by outer loop
            print("\t\t{} x {} = {}".format(num,i,num*i))
        else:
            print("------------------------------------------")