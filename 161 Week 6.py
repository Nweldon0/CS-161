def countdown(num):
    while num != 0:
        print(num)
        if num < 0:
            num = num + 1
        else:
            num = num - 1
    print("0")
    print("Liftoff!")
    print("")

def countdown_even(num_even):
    while num_even != 0:
        if num_even % 2 == 0:
            print(f"{num_even} is even")
        else:
            print(f"{num_even} is odd")
        num_even = num_even - 1
    print("0")
    print("Liftoff!")
    print("")

def countdown_int(num_int, num_int_value):
    while num_int >= 0:
        print(num_int)
        num_int = num_int - num_int_value
    print("Liftoff!")
    print("")

def countdown_word(num_word):
    tries = 0
    length = len(num_word)
    while length > 4:
        length = len(num_word)
        print(f"{num_word} is {length} letters long")
        if tries > 4:
            print("Too many tries. Moving on")
            return
        if length > 4:
            num_word = input("Enter another word: ")
        tries = tries + 1
    print(f"{num_word} is only {length} letters long. Moving on")
    print("")
# I think this function would be cleaner if I rewrote it to be based on the number of tries, with the length being secondary instead

# def countdown_star(num_star):
#     print("*" * num_star)

# I chose to just omit this one because the decrementing one is just an upgrade

def countdown_star(num_star):
    while num_star != 0:
        print("*" * num_star)
        num_star = num_star - 1
    print("")

def sum_check(num_sum):
    return sum(int(digit) for digit in num_sum)

def palindrome(text):
    if text == text[::-1]:
        return "is"
    else: return "is not"

def main():
    num = int(input("Enter a number: "))
    countdown(num)
    num_even = int(input("Enter a number: "))
    countdown_even(num_even)
    num_int = int(input("Enter a number: "))
    num_int_value = int(input("Enter a number to decrease by: "))
    countdown_int(num_int, num_int_value)
    num_word = input("Enter a word with more than five letters: ")
    countdown_word(num_word)
# I liked writing functions for all of these
    num_count = 0
    while num_count < 101:
        print(num_count)
        num_bin = bin(num_count)
        print(num_bin)
        num_hex = hex(num_count)
        print(num_hex)
        num_count = num_count + 10
        print("")
# I'm sure you could get this one as a function, but I chose not to

    num_star = int(input("Enter a number: "))
    countdown_star(num_star)

    num_sum = input("Enter any number of numbers: ")
    print(f"The sum of those numbers is: {sum_check(num_sum)}")
    print("")
# I struggled quite a bit with this one, getting it to see the numbers themselves and not as one long number

    text = input("Enter a word to check if it is a palindrome: ")
    print(f"'{text}' {palindrome(text)} a palindrome")
# Comparatively, this one was very easy

if __name__ == "__main__":
    main()