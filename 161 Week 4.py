from datetime import date
#All of this is old code for testing before I reworked it
    #print("The average of these three numbers is: ", average(num1, num2, num3))
    #def average(num1, num2, num3):
        #return(num1 + num2 + num3)/3
#Moving the function definition to after the print statements does not work, because the function needs to be defined BEFORE it is called upon to be used
    #print(num1)
#This does not work, as "num1" exists only in the function, and is not a global variable. It is just nonsense to any code outside the function
def average(num_dict):
    num_sum = sum(num_dict.values())
    num_count = len(num_dict)
    return num_sum/num_count
#This function adds all the numbers in a dictionary, checks how many total numbers there are, and then averages the entire dictionary based on these numbers

def human_to_dog_age(age):
    return 24 + (age - 2) * 4
#Nothing special, just does the math

def car_value(car_type, car_years, car_price):
    if car_type == "Italian":
        return car_price + (car_years * (car_price * 0.05))
    elif car_type == "German":
        return car_price - (car_years * (car_price * 0.05))
    else:
        return car_price - (car_years * (car_price * 0.07))
#Again just basic math to determine the car's new value

def icecream_price(icecream_scoops):
    current_year = int(icecream_year)
    years = current_year - icecream_year
    icecream_value = icecream_scoops * 1.15 + 2.25
    return icecream_value - (icecream_value * (years * 0.021)) - (icecream_value * (icecream_month * 0.00175))
#Google says about 16 scoops per half gallon of ice cream, which has risen in price approximately 2.1% per year, which is 0.175% per month
#I had a hard time finding specific prices or percents, so 2.1% is what I have to work with

num_input = input("Enter multiple numbers separated by spaces: ").split()
num_check = [float(x) for x in num_input if x.lstrip('-').replace('.', '', 1).isdigit()]
#This line verifies that everything input is actually a number, and if it isn't then it is excluded
#It also has special instructions for how to handle negatives and decimals by pretending the sign or dot isn't there to verify the numerical value, before then changing it into a float
num_dict = {f"num_{i+1}": val for i, val in enumerate(num_check)}
#The actual dictionary itself is created, using num_check instead of num_input to verify the validity of the numbers
print(f"The average of these numbers is {average(num_dict)}")
print("")

age = int(input("Enter your dog's age: "))
print(f"{age} dog years is equivalent to {human_to_dog_age(age)} human years.")
print("")
dog_name = input("What is your dog's name? ")
dog_age = input(f"How old is {dog_name}? ")
print(f"{dog_name} is {dog_age} in dog years, which makes them {human_to_dog_age(age)} in human years.")
#The instruction on this one confused me a bit, how is this any different from the above function? I was writing a new function for it but I can't find any difference between this and the earlier dog age calculator
print("")

car_type = input("Enter your car's origin (German, Japanese, Italian): ").capitalize()
car_price = int(input("Enter your car's original value when you purchased it: "))
print("")
car_years = int(input("Enter a number of years: "))
print("")
print(f"The value of your {car_type} car will be ${car_value(car_type, car_years, car_price)} after {car_years} years.")
print("")

icecream_scoops = int(input("How many ice cream scoops would you like? "))
icecream_year = int(input("In what year are you buying this cone? "))
icecream_month = int(input("In what month are you buying this cone (Numbered 1-12)? "))
print(f"Your ice cream cone would cost ${icecream_price(icecream_scoops)}. Enjoy!")