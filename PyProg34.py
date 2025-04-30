#PyProg34.py
"""
Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
	Sample list : ['p', 'q']
	n =5
	Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']"""
def concatlist(lst,n):
    res = []
    for i in range(1,n+1):
        for item in lst:
            res.append(item+str(i))
    return res
#main program
lst = list(input("Enter the sample list :-").split())
n = int(input("Enter the A Number:-"))
print(concatlist(lst,n))