def count_vowels(text):
    count = 0

    for letter in text.lower():
        if letter in "aeiou":
            count += 1

    return count


string = input("Enter a string: ")

print("Number of Vowels =", count_vowels(string))