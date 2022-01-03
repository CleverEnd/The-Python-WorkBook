letter = input("Enter a letter from the alphabet: ")

if letter in "aeiou":
    print("The letter", letter, "is a vowel")
elif letter == "y":
    print("The letter", letter, "its sometimes a vowel and sometimes a consonant")
else:
    print("Your letter", letter, "is a consonant")