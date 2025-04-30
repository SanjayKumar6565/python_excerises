#Program for Reading the list of numerical values and find sum and average
#AddlFunEx1.py
def  readvalues():
	n=int(input("Enter How Many Values sum and average want to find:"))
	if(n<=0):
		return []  # returning empty list  OR return list()
	else:
		lst=[] # create an empty list
		for i in range(1,n+1):
			val=float(input("Enter {} Value:".format(i)))
			lst.append(val)
		return lst  # returning non-empty list

def  findsumavg(lst):
	if(len(lst)==0):
		print("Given List is empty--can't find sum and average:")
	else:
		print("Given List Elements={}".format(lst)) # [10.0, 2.3, 12.0, 5.6, 0.0]
		s=0
		for val in lst:
			s+=val
		else:
			print("Sum({})={}".format(lst,s))
			print("Avg(({})={}".format(lst, s/len(lst)))

#main program
lst=readvalues()  # Function Call
findsumavg(lst) # Function Call