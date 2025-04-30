
#SimpleIntEx1.py
def simpleint():
    p=float(input("Enter Principle Amount:"))
    t=float(input("Enter Time:"))
    r=float(input("Enter Rate of Interest:"))
    #Cal si and totamt
    si=(p*t*r)/100
    totamt=p+si
    return p,t,r,si,totamt

#main program
s=simpleint() # FUNCTION CALL WITH SINGLE ASSIGMENT
#here s is an object whose type is tuple
print("*"*50)
print("\t\tPrinciple Amount:{} ".format(s[0]))
print("\t\tTime: {}".format(s[1]))
print("\t\tRate of Interest: {}".format(s[2]))
print("\t\tSIMPLE INTEREST: {}".format(s[3]))
print("\t\tTOTAL AMT TO PAY: {}".format(s[4]))
print("*"*50)