import time

def shouting():
    word_1 = input("Enter a phrase: ")
    word_2 = input("Repeat the same phrase: ")
    if not word_1 or not word_2:
        print("You didn't speak at all!")
        return
    if word_1.upper() == word_2:
        print("Stop shouting please!")
    elif not word_1.lower() == word_2.lower():
        print("You didn't repeat yourself!")
    else:
        print("Thank you for keeping your voice down.")
# Just a small check to see if the capitalized version of the first input matches the second

def vowel_check():
    count = 0
    word = input("Enter a word or phrase: ").lower()
    if not word:
        print("No input found")
        return
    for letter in word:
        if letter in "aeiou":
            count += 1
    count_2 = 0
    if 'a' in word:
        count_2 += 1
    if 'e' in word:
        count_2 += 1
    if 'i' in word:
        count_2 += 1
    if 'o' in word:
        count_2 += 1
    if 'u' in word:
        count_2 += 1
    print("")
    print(f"There are {count} vowels in that word/phrase.")
    print(f"There are {count_2} types of vowels in that word/phrase.")
# This checks not just how many kinds of vowels there are, but the total number too

def alphabetized():
    word_1 = input("Enter a word: ").lower()
    word_2 = input("Enter another word: ").lower()
    if not word_1 or not word_2:
        print("No input found")
        return
    if word_1 == word_2:
        print("Neither word is greater")
    elif word_1 < word_2:
        print(f"{word_1} is less than {word_2}")
    else:
        print(f"{word_2} is less than {word_1}")
# No need to check if word 2 is greater, if word 1 isn't greater and they aren't equal then it must be

def email():
    while True:
        word = input("Enter your email: ").lower()
        if not word:
            print("No email entered")
            return
        word_2 = input("Confirm your email: ").lower()
        if not word_2:
            print("No email entered")
            return
        if word_2 != word:
            print("The two emails did not match")
        elif not '@' in word:
            print("Not a valid email")
        else:
            print("Thank you")
            print("Have a great day!")
            return
# Decided to also make sure it has an @, otherwise it couldn't be an email. Could take it further by checking for @gmail or @yahoo or something, but not this time

def factorial_iterative():
    number = int(input("Enter a number: "))
    if not number:
        print("No number given")
    elif number < 0:
        print("The number cannot be negative")
    elif number == 0:
        print("1")
        return
    else:
        start = time.perf_counter()
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        print(f"The factorial of {number} is {factorial}")
        end = time.perf_counter()
        print(f"This method took {end - start:.8f} seconds.")
# Simple and effective. Goes from 1 to the chosen number, multiplying every step along the way

def factorial_recursive():
    number = int(input("Enter a number: "))
    if not number:
        print("No number given")
    elif number < 0:
        print("The number cannot be negative")
    elif number == 0:
        print("1")
        return
    else:
        start = time.perf_counter()
        factorial = 1
        i = 1
        while i <= number:
            factorial *= i
            i += 1
        print(f"The factorial of {number} is {factorial}")
        end = time.perf_counter()
        print(f"This method took {end - start:.8f} seconds.")
# This one sets factorial to be 1 and then multiplies it by every number one by one until it stops at the chosen number

def main():
    while True:
        print("")
        print("Which program would you like to view?")
        print("Shouting, Vowels, Alphabetical, Email, Factorial Iterative, Factorial Recursive")
        print("'Exit' to quit")
        choice = input("").lower()

        if choice == "shouting":
            shouting()
        elif choice == "vowels":
            vowel_check()
        elif choice == "alphabetical":
            alphabetized()
        elif choice == "email":
            email()
        elif choice == "factorial iterative":
            factorial_iterative()
        elif choice == "factorial recursive":
            factorial_recursive()
        elif choice == "exit":
            break
        else:
            print("That is not an option")



if __name__ == "__main__":
    main()