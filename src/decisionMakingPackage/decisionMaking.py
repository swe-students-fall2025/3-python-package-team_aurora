# This is where we will write our actual functions for the package
import random


def pick_food(dietary_restriction: str = None) -> None:
    restrictions = ["kosher",
        "halal",
        "jain",
        "vegetarian",
        "vegan", 
        "no_gluten",
        "no_soy",
        "no_nuts",
        "no_dairy",
        "no_eggs",
    ]
    # Default color set
    allFoods = set()
    for foods in restrictions.values():
        allFoods.update(foods)

    print("temp, replace with actual print statement")


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
    print("")


pick_color("calm", "Summer")
