import requests
import psutil
state_cap = {
    "alabama": "Montgomery",
    "alaska": "Juneau",
    "arizona": "Phoenix",
    "arkansas": "Little Rock",
    "california": "Sacramento",
    "colorado": "Denver",
    "connecticut": "Hartford",
    "delaware": "Dover",
    "florida": "Tallahassee",
    "georgia": "Atlanta",
    "hawaii": "Honolulu",
    "idaho": "Boise",
    "illinois": "Springfield",
    "indiana": "Indianapolis",
    "iowa": "Des Moines",
    "kansas": "Topeka",
    "kentucky": "Frankfort",
    "louisiana": "Baton Rouge",
    "maine": "Augusta",
    "maryland": "Annapolis",
    "massachusetts": "Boston",
    "michigan": "Lansing",
    "minnesota": "Saint Paul",
    "mississippi": "Jackson",
    "missouri": "Jefferson City",
    "montana": "Helena",
    "nebraska": "Lincoln",
    "nevada": "Carson City",
    "new hampshire": "Concord",
    "new jersey": "Trenton",
    "new mexico": "Santa Fe",
    "new york": "Albany",
    "north carolina": "Raleigh",
    "north dakota": "Bismarck",
    "ohio": "Columbus",
    "oklahoma": "Oklahoma City",
    "oregon": "Salem",
    "pennsylvania": "Harrisburg",
    "rhode island": "Providence",
    "south carolina": "Columbia",
    "south dakota": "Pierre",
    "tennessee": "Nashville",
    "texas": "Austin",
    "utah": "Salt Lake City",
    "vermont": "Montpelier",
    "virginia": "Richmond",
    "washington": "Olympia",
    "west virginia": "Charleston",
    "wisconsin": "Madison",
    "wyoming": "Cheyenne"
}
    # I know you said we only had to do six, but I couldn't just not finish it

def pool_admission(age):
    if age < 2:
        return 0
    elif age <= 11:
        return 3
    elif age <= 60:
        return 6
    else:
        return 4

def main():
    div_test = int(input("Enter a number: "))
    if div_test % 5 != 0:
        print(f"That number does not evenly divide into 5. The result is {div_test / 5}")
    else:
        print(f"That number does evenly divide into 5. The result is {div_test // 5}")
    print("")
    state = input("Enter a US state: ").lower()
    if state in state_cap:
        print(f"The capital of {state.capitalize()} is {state_cap[state]}")
    else:
        print("That is not a state")
    print("")
    print("Here is the table for entry prices to the pool:")
    print("Under 2 years old: Free")
    print("Ages 2-11: $3")
    print("Ages 12-60: $6")
    print("Over 60 years old: $4")
    family = input("Please enter the ages of everyone in your group, separated by spaces: ")
    print("")
    entries = family.split()
    results = []
    for item in entries:
        try:
            age = int(item)
            result = pool_admission(age)
            print(f"Age: {age}, Ticket Price: ${result}")
            results.append(result)
        except ValueError:
            print(f"{item} is not a valid age")
    print(f"Total price: ${sum(results)}")
    print("See you soon!")
    print("")
    # I felt like making this one more interesting, so now you can calculate the price of a whole family visit all at once!
    # Maybe next I could add a discount system? Where you can apply coupons for various price discounts and have it apply them

    word = input("Enter a word you would like to search for on the Hugo webpage: ").lower()
    url = "https://gohugo.io/"
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text.lower()
    # Making sure the request was successful
    else:
        print("Failed to fetch the webpage")
        exit()
    count = content.count(word)
    print(f"The word '{word}' appears {count} times on the Hugo webpage.")
    print("")

    proc_check = input("Would you like to know how many processes are running on your device? ").lower()
    if proc_check == "yes":
        proc = psutil.pids()
        proc_num = len(proc)
        print(f"There are {proc_num} processes currently running on your device.")
    print("Have a nice day!")

if __name__ == "__main__":
    main()