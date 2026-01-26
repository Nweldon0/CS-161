user_name = input("Please enter your name: ").capitalize() #Making sure the name is properly capitalized
print("Hello " + user_name + "!") #Even though I prefer f-strings, I wasn't sure if that is allowed
user_age = input("Please enter your age: ")
#print (user_age + 5)
#This print command doesn't work because the "user_age" variable is a string, and the number is an integer
#We can fix this by forcing the age to be an integer
user_age = int(user_age)
#print (f"In five years, you will be {user_age + 5} years old.")
years = int(input("Enter a number of years: "))
print("")
print(f"You are currently {user_age} years old. In {years} years, you will be {user_age + years} years old.")
print("")
death_check =input("Would you like to know when you will likely die? ").lower()
if death_check == "yes":
    print(f"The average human lifespan as of 2025 is 77 years old. Therefore, you are likely to die in {77 - user_age} years.")
#I just averaged the male and female death rates, it wouldn't be hard to ask for that though
print("")
hours_worked = float(input("How many hours do you work in an average week? "))
hourly_wage = float(input("What is your hourly wage? $"))
print(f"Your gross pay this week is ${hours_worked * hourly_wage}")
annual_income = hours_worked * hourly_wage * 50
#Making an annual income variable for ease of tax calculation
print(f"Your estimated annual gross pay is ${annual_income}")
if annual_income <= 11600: tax_rate = 0.90
elif annual_income <= 47150: tax_rate = 0.88
elif annual_income <= 100525: tax_rate = 0.78
elif annual_income <= 191950: tax_rate = 0.76
elif annual_income <= 243725: tax_rate = 0.68
elif annual_income <= 609350: tax_rate = 0.65
else: tax_rate = 0.63
#The tax rate here is the percentage that ISN'T taxed, so as to more easily calculate
print(f"After taxes, that makes ${annual_income * tax_rate}")