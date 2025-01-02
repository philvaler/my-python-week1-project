# Task 1: Interactive User Input: Create a script that 1) Asks for the user's name, age, and location, 2) Stores the inputs in variables.
name = input("What is your name? ").title() # the variable `name` has the user input their name. Then, the `.title()` capitalizes the first letter.
age_string = (input("How old are you? "))   # the variable `age` has the user input their age. `Input` always is saved as a string. So no need to worry about int.
location = input("Where in the world do you live? ").title().strip()    # the `location` variable has the user input their location. The .strip() removes whitespace.

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

# This is a test commit
print("Testing Git setup with user_summary.py")

# Optional Task 2: Script Enhancement: 1) Introduce random fun facts or motivational quotes based on user's input (e.g., use a dict to match locations with facts)

# Create a dictionary
my_dict = {
    "USA": "The population of the USA is over 340M? 🦅",
    "Japan": "Another name for Japan is Nippon. 🇯🇵",
    "Taiwan": "Taiwan invented boba tea! Yum! 🧋",
    "Peru": "Potatoes originate from Peru! Not from Idaho. 🥔",
    "Germany": "Oktoberfest is no longer celebrated by native Germans. It's mostly held by tourists now! 🍻",
    "Canada": "Canada is part of the British monarchy! Crazy, right? 🤴",
    "default": "I'd give you a fact about the world, but you didn't even tell me where you're from! ⛔️⛔️"
}

print(my_dict["USA"]) # Checking to see if it outputs correctly.

# Accessing fun facts based on user input. Majority of work already set up previously.
fact = my_dict.get(location, my_dict["default"])
print(f"Did you know? {fact}")

# Adding randomness
import random       # This is normally done at the beginning. This is just for practice purposes. Python imports the `random` function for the script.

quotes = [
    "Believe in yourself and all that you are. 🌟",
    "Every day is a second chance. 🌈",
    "The best way to predict the future is to create it. 🚀",
    "Dream big and dare to fail. 💪",
    "Keep going, you're doing great! 🌟"
]

# Choose a random quote
random_quote = random.choice(quotes)    # `random` calls the imported function to randomize. `.choice` is connected to the `random` function, and calls the function.
print(f"Here's a motivational quote for you: {random_quote}")