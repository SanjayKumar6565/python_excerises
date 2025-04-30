#string1.py
'''1. Write a program that asks the user to enter a string. The program should then print the following:
(a) The total number of characters in the string
(b) The string repeated 10 times
(c) The first character of the string (remember that string indices start at 0) (d) The first three
characters of the string
(e) The last three characters of the string
(f) The string backwards
(g) The seventh character of the string if the string is long enough and a message otherwise
(h) The string with its first and last characters removed
(i) The string in all caps
(j) The string with every a replaced with an e'''


#program..
string = str(input("Enter a string :-"))
s = len(string)
print(s)#(a)


for st in range(10):
    print(string)#(b)

print(string[0])#(c)

print(string[0:2])#(d)

print(string[-3:])#(e)

print(string[::-1])#(f)

if len(string)>=7:#(g)
    seventh_char = string[6]
    print("the seventh character of the string is:",seventh_char)
else:
    print("the string is not long enough to have a 7th character.")

print(string[1:-1])#(h)

print(string.upper())#(i)

print(string.replace('a','e'))




