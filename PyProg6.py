#PyProg6.py
def srt(tuple_list):
    srt_list = sorted(tuple_list,key=lambda x:x[-1])
    return srt_list
#main program
tuple_list=[]
input_tuple = tuple(map(int, input("Enter a tuple (comma-separated values): ").split()))
# Add the tuple to the list
tuple_list.append(input_tuple)
sorted_tuples = srt(tuple_list)
