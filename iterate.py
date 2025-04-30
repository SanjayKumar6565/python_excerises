s = 'Python'
iteobj = iter(s)
while True:
    try:
        item = next(iteobj)      # Iterate by calling next
        print(item)
    except StopIteration:   # exception will happen when iteration will over
        break