string = list(map(str,input("enter the list of String:").split(",")))
count = 0
for st in string:
    if len(st) >= 2 and st[0] == st[-1]:
        count += 1
print(count)






