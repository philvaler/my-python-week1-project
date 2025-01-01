# Task 1: Interactive User Input: Create a script that 1) Asks for the user's name, age, and location, 2) Stores the inputs in variables.
name = input("What is your name? ").title() # the variable `name` has the user input their name. Then, the `.title()` capitalizes the first letter.
age_string = str(input("How old are you? "))   # the variable `age` has the user input their age. Then, it takes the int and modifies to a string.
location = input("Where in the world do you live? ")    # the `location` variable has the user input their location.

# Task 2: Formatted Output: Use f-strings to neatly print a summary
print(f"Hello, {name}! You are {age_string} years old and live in {location}.")

# Task 3: Conditional Enhancements
try:
    age_integer = int(age_string)

    if age_integer < 18:
        print(f"Enjoy your youth!")
    elif 18 <= age_integer <= 30:
        print(f"You're in the prime of your life!")
    else:
        print(f"Age is just a number - keep thriving!")
# Task 4: Error Handling
except ValueError:
    print(f"🛑 I'm sorry, {name}. I'm afraid you can't do that.😢 You must enter an age!")

#elif age_integer >= range(18-30): is this possible? --> No. It is not possible.

# Task 5: Optional Enhancements: 1) Calculate how many years until the user is 100, 2) Add emojies or playful text for more engaging content.

years_to_100 = 100 - age_integer
print(f"Want to hear something crazy? In {years_to_100}, you will be 100 years old!")
