#PyProg33.py
#Write a Python program to generate all sublists of a list.
def generate_sublists(lst):
    sublists = [[]]

    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublists.append(lst[i:j])

    return sublists
#main program
    lst = list(map(int,input("enter the list elements :-").split()))
    all_sublists = generate_sublists(lst)
    print("All Sublists of", lst, "are:")
    for sublist in all_sublists:
        print(sublist)
