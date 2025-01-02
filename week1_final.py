# Task 1: Build a base greeting script: Prompt the user for their 1) name, 2) age, 3) location.
# Task 2: Add conditional responses: Personalize the greeeting bases on the user's age(switch up?)
# Task 3: Add a feature where the program suggest an activity based on the user's location or age
# Task 4: Include error handling for invalid inputs

# import random --> Don't need this since I wasn't able to use random function. I need a list for that.

name = input("What is your first and last name? Enter here: ").title()
age = input("Perfect! Now, how old are you? Enter here: ")
location = input("Now, where in the U.S. are you from? Enter here: ").title()

state_list = {
    "Alabama": "The official state dessert is pecan pie, reflecting Alabama's position as the third-largest pecan producer in the nation.",
    "Alaska": "Alaska has the longest coastline in the U.S., stretching 6,640 miles, which is greater than that of all other states combined.",
    "Arizona": "Tucson, Arizona, is home to the most telescopes in the world.",
    "Arkansas": "Arkansas has the only active diamond mine in the United States.",
    "California": """The state is home to \"General Sherman,\" 
a 3,500-year-old tree, and a stand of bristlecone pines that are 4,000 years old, 
making them the world's oldest living things.""",
    "Colorado": "The 13th step leading to the entrance of the Colorado State Capitol in Denver is exactly one mile above sea level.",
    "Connecticut": """The state song, \"Yankee Doodle,\"
is believed to have been written by the British to mock Connecticut volunteers during the French and Indian War.""",
    "Delaware": "Reggae star Bob Marley lived in Delaware from 1965 to 1977.",
    "Florida": "South Florida is the only place in the world where both crocodiles and alligators can be found in the wild.",
    "Georgia": "Gainesville, Georgia, passed a 1961 law making it illegal to eat fried chicken with a fork.",
    "Hawaii": "Hawaii is the most isolated large population center on Earth, almost 2,400 miles from California and about 4,000 miles from Japan.",
    "Idaho": "The state has the longest main street in America, stretching 33 miles in Island Park.",
    "Illinois": "The tallest building in the U.S., the Sears Tower (now Willis Tower), is located in Chicago.",
    "Indiana": "The state is home to the famous Indy 500 car race.",
    "Iowa": "The state has the shortest and steepest railroad in the U.S., located in Dubuque, with a 60° incline and 296 feet in length.",
    "Kansas": "Helium was discovered in 1905 at the University of Kansas.",
    "Kentucky": "About a fifth of the state's 120 counties are completely dry, meaning no liquor sales are allowed.",
    "Louisiana": " It's the only state in the country to adhere to a civil law system, as opposed to the common law used in the other 49 states.",
    "Maine": "Did you know? The state has almost 60 active lighthouses along its coast.",
    "Maryland": "Baltimore's NFL franchise, the Ravens, is named after local author Edgar Allan Poe's poem \"The Raven\".",
    "Massachusetts": "The state is home to Lake Chargo-ggagoggm-anchaug-gagoggcha-ubunagun gamaugg, which has the longest place name in America.",
    "Michigan": "The Mackinac Bridge, which spans 5 miles over the Straits of Mackinac, sometimes closes due to extreme weather.",
    "Minnesota": "The Mall of America in Bloomington is so large that seven Yankee Stadiums could fit inside it.",
    "Mississippi": "The state's name comes from the Ojibwe words Misi zipi, meaning \"Great River\".",
    "Missour": "The state was named after a tribe of Sioux Indians called the Missouria, which means \"he of the big canoe\".",
    "Montana": "It's the only state in the US with a Triple Divide, allowing waters to flow to Hudson Bay, the Atlantic Ocean, and the Pacific Ocean.",
    "Nebraska": "Kool-Aid was invented in the town of Hastings in 1927.",
    "Nevada": "It's the driest state in the US, averaging about 10 inches of rain a year.",
    "New Hampshire": "The first free public library in the United States was founded in Peterborough, New Hampshire in 1833.",
    "New Jersey": "Did you know? The state has the most diners in the country.",
    "New Mexico": "Did you know? The state has an official question: \"Red or green?\" referring to which variety of chile sauce you'd like on your food.",
    "New York": "George Washington was declared Commander in Chief at NYC's Federal Hall during the first United States Congress in 1789.",
    "North Carolina": """The waters off the Outer Banks are known as \"The Graveyard of the Atlantic\" 
due to over 1,000 shipwrecks caused by sandbars and strong currents.""",
    "North Dakota": "It's the number one producer of honey in the country.",
    "Ohio": "The state flag is the only burgee-shaped one in the country, resembling a pennant with a triangle missing at the end.",
    "Oklahmoa": "The official state poem is \"Howdy Folks,\" an ode to Oklahoma cowboy Will Rogers.",
    "Oregon": "The state is home to the world's largest living organism, a fungal colony in the Blue Mountains.",
    "Pennsylvania": "The first magazine in America, called the American Magazine, was published in Philadelphia for 3 months in 1741.",
    "Rhode Island": "The Rhode Island Red chickens, first bred in 1854, marked the start of poultry as a major American industry.",
    "South Carolina": "The first tea farm in the U.S. was created in 1890 near Summerville.",
    "South Dakota": "The world's largest natural, indoor warmwater pool, Evans' Plunge, is located in Hot Springs.",
    "Tennessee": "The state is home to Graceland, the estate and gravesite of Elvis Presley.",
    "Texas": "NASA's headquarters for all piloted U.S. space projects is located in Houston.",
    "Utah": "The state is home to Rainbow Bridge, the largest natural stone bridge in the world, standing 290 feet high and 275 feet across.",
    "Vermont": "The state is the largest producer of maple syrup in the U.S.",
    "Virginia": "The state capitol houses the only full-length statue of George Washington, placed there in 1796",
    "Washington": "The state shares its name with the first U.S. president, George Washington.",
    "West Virginia": "The state was formed during the Civil War when it separated from Virginia.",
    "Wisconsin": "The state is famous for its cheese production and is often referred to as \"America's Dairyland.\"",
    "Wyoming": "Yellowstone National Park, the first national park in the U.S., is largely located in Wyoming.",
    "default": "So yeah. You know, not telling me the state you live means I can't give you a random fact. Thanks, jerk."
}

state_fact = state_list.get(location, state_list["default"])
#random_state = random.choice(state_list) ---> I screwed up with this one.

try:
    age_integer = int(age)

    if 0 <= age_integer <= 10:
        print(f"You're {age_integer}, {name}!? ⛔️ Just stay in {location} home with your parents!")

    elif 10 <= age_integer <= 17:
        print(f"So {name}, since you're {age_integer} years old, just stay in your {location} and finish school! 🎓 By the way, did you know? {state_fact}")
    elif 18 <= age_integer <= 22:
        print(f"Congratulations, {name}! You're an adult! Did you choose to go out of state for university? 🧠 If you stayed, here's a random fact. {state_fact}")
    elif 23 <= age_integer <= 39:
        print(f"Look at you, {name}! You're {age_integer}! 🥳 These are special years! To keep your mind spry, here's some random facts of {location}! 🌎 {state_fact}")
    elif 40 <= age_integer <=59:
        print(
            f"Have you been looking back throughout your life, {name}? Guess what!? These are your golden years! "
            f"Tech has advanced, so expect to feel like you're young again! {age_integer} is the new 20! 🤯 "
            f"Take this time to know this about {location} where you've lived for oh so long! {state_fact}"
        )
    else:
        print(f"Crazy how fast the years have gone! Did you know aging has been solved, {name}? {age_integer} is forever young! LFG!! 🤩 Did you stay in {location}? 🤔")
except ValueError:
    print(f"Okay, {name}. Why did you skip putting your age? ❌ No no no. You don't get a pass. Write your age! I mean it! 😤")