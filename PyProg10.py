#PyProg10.py
def filter_words(words, n):
    result = [word for word in words if len(word) > n]
    return result


word_list = list(input("enter the list of words :").split())
n_value = int(input("enter the a number:"))

filtered_words = filter_words(word_list, n_value)
print(f"Words longer than {n_value}: {filtered_words}")
