def evn_checker():
    false = 1
    while false == 1:
        evn_num = input("Enter two numbers: ")
        verf = evn_num.split()
        if len(verf) == 2:
            false = 0
            try:
                num1 = int(verf[0])
                num2 = int(verf[1])
            except ValueError:
                false = 1
            if false == 1:
                print("Not a valid input")
        else:
            false = 1
            print("Not a valid input")
    # This loop keeps going until we have a valid input, to ensure no issues
    # Once we're past it, we know for sure we have two valid numbers to work with

    num1_str, num2_str = evn_num.split()
    # This one insists that it might not be defined
    num1 = int(num1_str)
    num2 = int(num2_str)
    # This gets our two input values out of the one string

    if num1 < num2:
        smaller = num1
        larger = num2
    else:
        smaller = num2
        larger = num1
    if smaller % 2 != 0:
        smaller += 1
# Checking to see which is larger, and making the smaller one even if it isn't already
    evn_list = []

    while smaller <= larger:
        evn_list.append(smaller)
        smaller += 2
    # Listing the current number and then going up by two, until it is no longer within the range given

    print(f"Every even number between those numbers:", " ".join(map(str, evn_list)))
    print("")

def alph_checker():
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    while True:
        total = 0
        alph = input("Enter a name: ")
        if not alph:
            print("No name provided")
            print("")
    # Make sure an input is given at all
        else:
            for letter in alph.lower():
                if letter in alphabet:
                    value = alphabet.index(letter)
                    total += value
    # This checks every character of the given input, and if it is a letter it has a value assigned to it
            print(f"The sum of {alph} is {total}")
            print("")
            return

def sqr_checker():
    while True:
        sqr = int(input("Enter a number: "))
        for i in range(1, sqr + 1):
            print(i * i)
        print("")
        return
# Short function, just squares every number leading up to the number given

def teepee():
    while True:
        nums = input("Enter a series of numbers: ").split()
        if not nums:
            print("No numbers provided")
        else:
            verf = list(map(int, nums))
            odds = sorted([n for n in verf if n % 2 != 0])
            evens = sorted([n for n in verf if n % 2 == 0], reverse=True)
            tp = odds + evens
            print(tp)
            print("")
            return
# This takes the list of numbers, determines whether they are odd or even based on whether they can divide by 2, and then sorts them accordingly.
# I didn't actually make it put the largest number in the center, because if the odds are going up and then the evens are going down the largest will end up in the center anyway

def next_high():
    while True:
        num = input("Enter a number: ")
        if not num:
            print("No number provided")
        else:
            digits = list(num)
            big_num = len(digits) - 2
            while big_num >= 0 and digits[big_num] >= digits[big_num + 1]:
                big_num -= 1
            if big_num < 0:
                print("This number is already as large as possible")
                return
# This checks each number to see if the number to the left of it is larger, and if not, it chooses that number to be switched
            bigger_num = len(digits) - 1
            while digits[bigger_num] <= digits[big_num]:
                bigger_num -= 1
            digits[big_num], digits[bigger_num] = digits[bigger_num], digits[big_num]
# Once a number has been found that could be larger, we move a new variable to the place just left of it and then swap them
            new_num = int("".join(map(str, digits)))
            print(f"The next largest number using these digits is: {new_num}")
            print("")

def main():
    while True:
        print("Even number checker:        1")
        print("Alphabet name calculator:   2")
        print("Squares:                    3")
        print("Teepee:                     4")
        print("Next higher number:         5")
        print("Quit the program:           0")
        print("")
# I decided to make this one less of a headache to access specific functions. I think I'll do this going forward, too
        func = input("Enter the number corresponding to the function you wish to run: ")
        if not func:
            func = "6"
        if func == "1":
            evn_checker()
        elif func == "2":
            alph_checker()
        elif func == "3":
            sqr_checker()
        elif func == "4":
            teepee()
        elif func == "5":
            next_high()
        elif func == "0":
            print("Have a nice day!")
            return
        else:
            print("Invalid choice")
        more = input("Would you like to continue? (y/n): ")
        if more == "n":
            print("Have a nice day!")
            return

if __name__ == "__main__":
    main()