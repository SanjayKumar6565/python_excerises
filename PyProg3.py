#largest number from a list
lst = list(map(int,input().split()))
lst.sort(reverse=True)
print(lst[0])


