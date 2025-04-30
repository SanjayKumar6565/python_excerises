#PyProg39.py
#write a Python program to split a list based on first character of word.
def split_list_by_first_char(word_list):

    char_dict = {}

    for word in word_list:
        first_char = word[0]
        if first_char not in char_dict:
            char_dict[first_char] = []
        char_dict[first_char].append(word)

    return char_dict

# Example usage:
words = list(input("Enter the list of words:-").split())
result = split_list_by_first_char(words)
print(result)