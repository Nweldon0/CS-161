import datetime
from datetime import date

wone = input("Which part of the program would you like to see? (Pets, Savings, Months, Eggs) ").lower()
#I decided to make it one program that lets you view all the individual actions separately

if wone == "pets":
    #First up is the pet program, which I also changed to be interactable instead of just about my cat
    ptype = input('What type of pet do you have? ').lower()
    pname = input('What is the name of your pet? ').capitalize() #To make sure the pet's name is capitalized
    pgender = input('What is the gender of your pet? ').lower()
    #I named the variables with a "p" before them, just to be sure there was no overlap. The "p" is for the "pets" program
    if pgender == 'male':
        pgender2 = "his"
    elif pgender == 'female':
        pgender2 = "her"
    else: pgender2 = "their"
    print(f"You have a {ptype}, {pgender2} name is {pname}")

if wone == "savings":
    #The savings program, for which I didn't deviate as much as with the pet program
    sname = input('What is your name? ').capitalize()
    sage = int(input('How many years old are you? '))
    ssavings = int(input('Enter your yearly savings as a number: '))
    #These variables have an "s" before them, for the same reason as the pet variables
    print(f"Hello {sname}! You are currently {sage} years old.")
    print(f"In ten years, you will be {sage + 10} years old. (Wow!)")
    print(f"If you continue to save ${ssavings} each year, in five years you will have saved ${ssavings * 5}.")
    print(f"Your average monthly savings is ${ssavings / 12}.")
    print("Good luck!")

if wone == "months":
    #This one was a bit of a mess, but it accurately tells you how many seconds are in each month
    mmonth = datetime.datetime.now().month
    #Variables now start with an "m"
    if mmonth == 1:
        mmonth2 = "January"
        mseconds = "2,678,400"
    elif mmonth == 3:
        mmonth2 = "March"
        mseconds = "2,678,400"
    elif mmonth == 4:
        mmonth2 = "April"
        mseconds = "2,592,000"
    elif mmonth == 5:
        mmonth2 = "May"
        mseconds = "2,678,400"
    elif mmonth == 6:
        mmonth2 = "June"
        mseconds = "2,592,000"
    elif mmonth == 7:
        mmonth2 = "July"
        mseconds = "2,678,400"
    elif mmonth == 8:
        mmonth2 = "August"
        mseconds = "2,678,400"
    elif mmonth == 9:
        mmonth2 = "September"
        mseconds = "2,592,000"
    elif mmonth == 10:
        mmonth2 = "October"
        mseconds = "2,678,400"
    elif mmonth == 11:
        mmonth2 = "November"
        mseconds = "2,592,000"
    else: mmonth2 = "December"
    mseconds = "2,678,400"
    #February gets its own special section to determine if it is a leap year, in which case the number of seconds would be different
    if mmonth != 2:
        print(f"The current month is {mmonth2}. The number of seconds in this month is {mseconds}.")
    else:
        myear = date.today().year
        if myear % 4 == 0:
            myear = "is"
            mseconds = "2,505,600"
        else:
            myear = "is not"
            mseconds = "2,419,200"
        print(f"The current month is February. It {myear} a leap year, therefore the number of seconds this February is {mseconds}.")

if wone == "eggs":
    #Variable over here doesn't need the "e", but I wanted to be consistent in case we need to expand upon these later
    eeggs = int(input('How many eggs do you have? '))
    if eeggs % 12 == 0:
        print(f"That makes {eeggs // 12} dozen eggs even.")
    else:
        print(f"That makes {eeggs // 12} dozen, with {eeggs % 12} eggs left over.")