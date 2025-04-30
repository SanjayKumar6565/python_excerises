nub = int(input("Enter the a number:-"))
rev = 0
while nub!=0:
    rem = nub % 10
    rev = rev * 10 + rem
    nub = nub // 10
print(str(rev))
