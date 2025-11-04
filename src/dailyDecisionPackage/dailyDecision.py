# This is where we will write our actual functions for the package
import random


def pick_clothes(weather: str = None, occasion: str = None) -> None:
    clothes_by_weather = {
        "sunny": [
            "sports bra",
            "jersey",
            "T-shirt",
            "shorts",
            "sneakers",
            "khakis",
            "jeans",
            "sandals",
            "sombrero",
            "high heels",
        ],
        "rainy": ["poncho", "raincoat", "boots"],
        "snowy": ["fleece jacket", "scarf", "neckerchief", "beanie", "mittens"],
        "windy": ["light jacket", "hoodie", "athletic pants", "earmuffs"],
    }
    clothes_by_occasion = {
        "casual": ["T-shirt", "shorts", "sneakers", "hoodie", "jeans", "sandals"],
        "formal": [
            "necktie",
            "neckerchief",
            "bowtie",
            "tuxedo",
            "dress shoes",
            "button-up shirt/blouse",
            "khakis",
            "skirt",
        ],
        "athletic": ["sports bra", "jersey", "cleats", "athletic pants", "headband"],
        "party": [
            "sequin dress",
            "high heels",
            "blazer",
            "fedora",
            "rings",
            "slacks",
            "halter top",
        ],
        "beach": [
            "sandals",
            "bikini",
            "swimtrunks",
            "speedo",
            "sombrero",
            "cap",
            "one-piece suit",
            "crocs",
        ],
    }

    # build full set of clothes
    allClothes = set()
    for clothes in clothes_by_weather.values():
        allClothes.update(clothes)
    for clothes in clothes_by_occasion.values():
        allClothes.update(clothes)

    # No arguments (pick random clothes)
    if weather is None and occasion is None:
        print(
            f"Try these clothes! They look good on you: {random.choice(list(allClothes))}"
        )
    # Only weather, no occasion
    elif occasion is None:
        # Invalid weather
        if weather.lower() not in clothes_by_weather:
            print(f"Oopsie poopsie! :( '{weather}' isn't a weather!")
            print(f"Choose from: sunny, rainy, snowy, windy")
            print(
                f"Otherwise, what do you think of these clothes? {random.choice(list(allClothes))}"
            )
            return
        # Valid weather
        validClothes = set(clothes_by_weather[weather.lower()])
        print(
            f"You chose: '{weather}', so why not wear this bad boy? {random.choice(list(validClothes))}"
        )
    # Only occasion, no weather
    elif weather is None:
        # Invalid occasion
        if occasion.lower() not in clothes_by_occasion:
            print(f"Oopsie poopsie! :( '{occasion}' isn't a real occasion!")
            print(f"Choose from: casual, formal, athletic, party, beach")
            print(
                f"Otherwise, what do you think of these clothes? {random.choice(list(allClothes))}"
            )
            return
        # Valid occasion
        validClothes = set(clothes_by_occasion[occasion.lower()])
        print(
            f"You chose: '{occasion}', so why not wear this bad boy? {random.choice(list(validClothes))}"
        )
    # Arguments for both weather and occasion
    else:
        # Invalid weather
        if weather.lower() not in clothes_by_weather:
            print(f"Oopsie poopsie! :( '{weather}' isn't a weather!")
            print(f"Choose from: sunny, rainy, snowy, windy")
            print(
                f"Otherwise, what do you think of these clothes? {random.choice(list(allClothes))}"
            )
        # Invalid occasion
        if occasion.lower() not in clothes_by_occasion:
            print(f"Oopsie poopsie! :( '{occasion}' isn't a real occasion!")
            print(f"Choose from: casual, formal, athletic, party, beach")
            print(
                f"Otherwise, what do you think of these clothes? {random.choice(list(allClothes))}"
            )
        # If either is invalid, return early
        if (
            weather.lower() not in clothes_by_weather
            or occasion.lower() not in clothes_by_occasion
        ):
            return
        # Both valid weather and occasion
        validClothes = list(
            set(clothes_by_occasion[occasion.lower()])
            & set(clothes_by_weather[weather.lower()])
        )
        if validClothes:
            clothes = random.choice(validClothes)
            print(
                f"Good choice! For your weather {weather} and occasion {occasion}, try these clothes out! {clothes}"
            )
        # but they may not have clothes in common
        else:
            rand_weather = random.choice(clothes_by_weather[weather.lower()])
            rand_occasion = random.choice(clothes_by_occasion[occasion.lower()])
            print(
                f"Sorry but your weather and occasion didn't fit! But for {weather.lower()} weather, try on {rand_weather}"
            )
            print(
                f"For {occasion.lower()} occasion, why not give {rand_occasion} a shot?"
            )
    return


def pick_food(dietary_restriction: str = None) -> None:
    # Foods by restriction
    foods_by_restriction = {
        "halal": [
            "chicken biryani",
            "beef kebab plate",
            "shawarma bowl",
            "lentil dal with rice",
            "falafel wrap",
            "grilled salmon",
        ],
        "high_protein": [
            "grilled chicken breast with quinoa",
            "salmon with asparagus",
            "beef stir-fry",
            "lentil salad",
            "tofu and broccoli bowl",
            "turkey chili",
        ],
        "high_protein": [
            "grilled chicken breast with quinoa",
            "salmon with asparagus",
            "beef stir-fry",
            "lentil salad",
            "tofu and broccoli bowl",
            "turkey chili",
        ],
        "jain": [
            "vegetable khichdi",
            "paneer tikka (no onion/garlic)",
            "sabudana khichdi",
            "dal dhokli",
            "vegetable pulao",
            "coconut curry",
        ],
        "keto": [
            "zucchini noodles with pesto",
            "grilled salmon with avocado",
            "cauliflower rice stir-fry",
            "bunless burger with cheese and salad",
            "omelet with spinach and mushrooms",
            "chicken caesar salad (no croutons)",
        ],
        "kosher": [
            "bagel with lox",
            "matzo ball soup",
            "tuna salad",
            "grilled salmon with potatoes",
            "egg salad sandwich",
            "falafel plate",
        ],
        "low_carb": [
            "grilled chicken and veggies",
            "beef lettuce wraps",
            "zoodle bolognese",
            "egg omelet with avocado",
            "shrimp and broccoli stir-fry",
            "cauliflower crust pizza",
        ],
        "no_dairy": [
            "tom yum soup",
            "poke bowl",
            "chicken shawarma wrap (no yogurt sauce)",
            "vegan ramen",
            "tofu curry",
            "bibimbap (no egg)",
        ],
        "no_eggs": [
            "pasta primavera",
            "mushroom risotto",
            "vegetable stir-fry",
            "falafel wrap",
            "vegan curry",
            "tofu scramble",
        ],
        "no_gluten": [
            "rice bowl with chicken",
            "corn tacos",
            "pho",
            "sashimi platter",
            "thai green curry",
            "baked sweet potato",
        ],
        "no_nuts": [
            "margherita pizza",
            "spaghetti pomodoro",
            "fried rice",
            "beef tacos",
            "rotisserie chicken plate",
            "tomato soup & grilled cheese",
        ],
        "no_nuts": [
            "margherita pizza",
            "spaghetti pomodoro",
            "fried rice",
            "beef tacos",
            "rotisserie chicken plate",
            "tomato soup & grilled cheese",
        ],
        "no_soy": [
            "grilled chicken salad",
            "roasted veggie pasta",
            "eggplant parm",
            "mushroom risotto",
            "omelet with veggies",
            "lentil soup",
        ],
        "paleo": [
            "grilled steak with roasted veggies",
            "salmon with sweet potato mash",
            "zucchini noodles with tomato sauce",
            "chicken lettuce wraps",
            "baked cod with olive oil",
            "fruit and nut bowl",
        ],
        "pescatarian": [
            "salmon poke bowl",
            "shrimp tacos",
            "grilled cod with veggies",
            "tuna niçoise salad",
            "sushi combo",
            "miso-glazed salmon",
            "fish and chips (light batter)",
        ],
        "vegan": [
            "tofu stir-fry",
            "chickpea curry",
            "veggie sushi",
            "buddha bowl",
            "lentil bolognese",
            "quinoa salad",
        ],
        "vegetarian": [
            "margherita pizza",
            "mushroom risotto",
            "spinach ravioli",
            "caprese sandwich",
            "falafel bowl",
            "paneer tikka",
        ],
    }

    # Build full set of all foods
    allFoods = set()
    for foods in foods_by_restriction.values():
        allFoods.update(foods)

    # No restriction given — pick from all
    if dietary_restriction is None:
        print(f"How about: {random.choice(list(allFoods))}")
        return

    restriction = dietary_restriction.strip().lower()

    aliases_any = {
        "any", "anything", "whatever", "no", "none",
        "no restriction", "normal", "idk", "anything works"
    }
    if restriction in aliases_any:
        print(f"How about: {random.choice(list(allFoods))}")
        return


    if restriction not in foods_by_restriction:
        accepted = ", ".join(sorted(foods_by_restriction.keys()))
        print(f"Sorry, '{restriction}' is not a supported restriction.")
        print(f"Please choose from: {accepted}")
        print(f"In the meantime, try: {random.choice(list(allFoods))}")
        return
    

    choice = random.choice(foods_by_restriction[restriction])
    print(f"For a {restriction} diet, you could try: {choice}")


def pick_color(mood: str = None, season: str = None) -> None:
    winter = [
        "blue",
        "navy",
        "white",
        "silver",
        "black",
        "burgundy",
        "emerald green",
        "royal purple",
        "ice blue",
        "charcoal",
    ]
    fall = [
        "orange",
        "rust",
        "brown",
        "burgundy",
        "mustard yellow",
        "olive green",
        "burnt sienna",
        "copper",
        "maroon",
        "tan",
    ]
    summer = [
        "yellow",
        "coral",
        "turquoise",
        "hot pink",
        "lime green",
        "sky blue",
        "peach",
        "tangerine",
        "mint",
        "aqua",
    ]
    spring = [
        "pastel pink",
        "lavender",
        "mint",
        "baby blue",
        "lemon yellow",
        "peach",
        "soft coral",
        "light purple",
        "sage green",
        "cream",
    ]
    happy = [
        "yellow",
        "bright orange",
        "sunny gold",
        "lime green",
        "sky blue",
        "pink",
        "coral",
        "peach",
        "turquoise",
    ]
    sad = ["blue", "grey", "dark purple", "navy", "slate blue", "charcoal", "ice blue"]
    calm = [
        "light blue",
        "lavender",
        "sage green",
        "soft grey",
        "beige",
        "mint",
        "powder blue",
        "pale pink",
        "baby blue",
    ]
    energetic = [
        "red",
        "bright orange",
        "electric blue",
        "neon green",
        "hot pink",
        "vibrant yellow",
        "magenta",
        "lime green",
        "tangerine",
    ]
    angry = [
        "red",
        "crimson",
        "black",
        "dark orange",
        "blood red",
        "maroon",
        "dark grey",
        "burgundy",
    ]

    # Season and mood dictionaries for easy lookup
    seasonColors = {"winter": winter, "fall": fall, "summer": summer, "spring": spring}
    moodColors = {
        "happy": happy,
        "sad": sad,
        "calm": calm,
        "energetic": energetic,
        "angry": angry,
    }
    # Default color set
    allColors = set()
    for colors in seasonColors.values():
        allColors.update(colors)
    for colors in moodColors.values():
        allColors.update(colors)

    # No arguments - pick from default
    if mood is None and season is None:
        print(f"Here's a random color for you: {random.choice(list(allColors))}")
    # Only mood provided
    elif mood is not None and season is None:
        mood = mood.lower()
        if mood not in moodColors:
            print(
                f"Sorry, '{mood}' is not a supported mood. Here's the list of accepted moods: {', '.join(moodColors.keys())}"
            )
            print(
                f"Picking from default list instead: {random.choice(list(allColors))}"
            )
        else:
            color = random.choice(moodColors[mood])
            print(f"For your {mood} mood, try: {color}")
    # Only season provided
    elif season is not None and mood is None:
        season = season.lower()
        if season not in seasonColors:
            print(
                f"Sorry, '{season}' is not a valid season. Here's the list of accepted seasons: {', '.join(seasonColors.keys())}"
            )
            print(
                f"Picking from default list instead: {random.choice(list(allColors))}"
            )
        else:
            color = random.choice(seasonColors[season])
            print(f"For {season} season, try: {color}")
    # Both mood and season provided
    else:
        mood = mood.lower()
        season = season.lower()
        validMood = mood in moodColors
        validSeason = season in seasonColors
        # If both invalid, pick from default
        if not validMood and not validSeason:
            print(
                f"Sorry, '{mood}' is not a valid mood and '{season}' is not a valid season."
            )
            print(f"Here's the list of accepted moods: {', '.join(moodColors.keys())}")
            print(
                f"Here's the list of accepted seasons: {', '.join(seasonColors.keys())}"
            )
            print(
                f"Picking from default list instead: {random.choice(list(allColors))}"
            )
        # If only mood invalid, use season
        elif not validMood:
            print(
                f"Sorry, '{mood}' is not a valid mood. Try: {', '.join(moodColors.keys())}"
            )
            color = random.choice(seasonColors[season])
            print(f"Using just your {season} season instead, try: {color}")
        # If only season invalid, use mood
        elif not validSeason:
            print(
                f"Sorry, '{season}' is not a valid season. Try: {', '.join(seasonColors.keys())}"
            )
            color = random.choice(moodColors[mood])
            print(f"Using just your {mood} mood instead, try: {color}")
        # Both valid
        else:
            commonColors = list(set(moodColors[mood]) & set(seasonColors[season]))
            if commonColors:
                color = random.choice(commonColors)
                print(f"Perfect match! For {mood} mood in {season}: {color}")
            else:
                mood_color = random.choice(moodColors[mood])
                season_color = random.choice(seasonColors[season])
                print(
                    f"No perfect match, but try {mood} color: {mood_color} or {season} color: {season_color}"
                )


def pick_activity(weather: str = None, energy_level: str = None) -> None:
    # Activities by weather
    activities_by_weather = {
        "sunny": [
            "go for a walk",
            "read a book at the park",
            "explore a new part of the city",
            "go for a run",
            "go hiking",
            "bike around your neighborhood",
            "go to the beach",
        ],
        "cloudy": ["watch the clouds"],
        "rainy": ["dance in the rain"],
        "snowy": ["make snow angels", "build a snowman", "snowball fight"],
        "any": [
            "watch a movie or TV",
            "play a video game",
            "read a book indoors",
            "listen to a podcast",
            "listen to music",
            "write a journal entry",
            "call a friend",
            "play a board game",
            "solve a crossword",
            "clean your bedroom",
            "light exercise",
            "dance",
            "make a home-cooked meal",
            "arts & crafts",
            "yoga",
            "go to the gym",
            "go to the club",
            "go to a party",
            "clean the house",
            "painting",
            "go for a drive",
        ],
    }
    # Activities by energy level
    activities_by_energy_level = {
        "low": [
            "watch a movie or TV",
            "play a video game",
            "read a book indoors",
            "read a book at the park",
            "listen to a podcast",
            "listen to music",
            "write a journal entry",
            "call a friend",
            "play a board game",
            "solve a crossword",
            "watch the clouds",
            "painting",
        ],
        "medium": [
            "go for a walk",
            "clean your bedroom",
            "light exercise",
            "dance",
            "dance in the rain",
            "make a home-cooked meal",
            "arts & crafts",
            "yoga",
            "make snow angels",
            "build a snowman",
            "go to the beach",
            "go for a drive",
        ],
        "high": [
            "go to the gym",
            "go for a run",
            "go hiking",
            "bike around your neighborhood",
            "go to the club",
            "go to a party",
            "clean the house",
            "snowball fight",
            "explore a new part of the city",
        ],
    }
    # create set of all activities
    allActivities = set()
    for activities in activities_by_weather.values():
        allActivities.update(activities)
    for activities in activities_by_energy_level.values():
        allActivities.update(activities)

    # No arguments (pick random activity)
    if weather is None and energy_level is None:
        print(f"Try this activity: {random.choice(list(allActivities))}")
        return
    # No energy level argument (weather only)
    elif energy_level is None:
        # Invalid weather
        if weather.lower() not in activities_by_weather:
            accepted = ", ".join(sorted(activities_by_weather.keys()))
            print(f"Sorry, '{weather}' is not a supported weather type.")
            print(f"Please choose from: sunny, cloudy, rainy, snowy")
            print(
                f"In the meantime, try this activity: {random.choice(list(allActivities))}"
            )
            return
        # Valid weather
        validActivities = set(activities_by_weather[weather.lower()]) | set(
            activities_by_weather["any"]
        )
        print(f"Try this activity: {random.choice(list(validActivities))}")
        return
    # No weather argument (energy level only)
    elif weather is None:
        # Invalid energy level
        if energy_level.lower() not in activities_by_energy_level:
            print(f"Sorry, '{energy_level}' is not a supported energy level.")
            print(f"Please choose from: low, medium, high")
            print(
                f"In the meantime, try this activity: {random.choice(list(allActivities))}"
            )
            return
        # Valid energy level
        validActivities = set(activities_by_energy_level[energy_level.lower()])
        print(f"Try this activity: {random.choice(list(validActivities))}")
        return
    # Arguments for both weather and energy level
    else:
        # Invalid weather
        if weather.lower() not in activities_by_weather:
            accepted = ", ".join(sorted(activities_by_weather.keys()))
            print(f"Sorry, '{weather}' is not a supported weather type.")
            print(f"Please choose from: sunny, cloudy, rainy, snowy")
            print(
                f"In the meantime, try this activity: {random.choice(list(allActivities))}"
            )
            return
        # Invalid energy level
        if energy_level.lower() not in activities_by_energy_level:
            print(f"Sorry, '{energy_level}' is not a supported energy level.")
            print(f"Please choose from: low, medium, high")
            print(
                f"In the meantime, try this activity: {random.choice(list(allActivities))}"
            )
            return
        # Valid arguments
        # Valid arguments
        validActivities = (
            set(activities_by_weather[weather.lower()])
            | set(activities_by_weather["any"])
        ) & set(activities_by_energy_level[energy_level.lower()])

        if validActivities:
            print(f"Try this activity: {random.choice(list(validActivities))}")
        else:
            # No perfect match - suggest activities from default list
            print(
                f"Sorry, no perfect match! But for now try: {random.choice(list(allActivities))}"
            )
        return
