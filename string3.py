#string3.py
"""Write a program that asks the user to enter a word and prints out whether that word contains any
vowels."""
def has_vowels(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for char in word:
        if char.lower() in vowels:
            return True
    return False
def main():
    user_word = input("Enter a word: ")
    if has_vowels(user_word):
        print("The word contains vowels.")
    else:
        print("The word does not contain any vowels.")


main()
