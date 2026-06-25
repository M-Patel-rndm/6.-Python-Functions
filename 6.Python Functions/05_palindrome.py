def is_palindrome(word):
    return word == word[::-1]


text = input("Enter a word: ")

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a Palindrome")