import pytest
from dailyDecisionPackage.dailyDecision import pick_color, pick_activity, pick_clothes, pick_food


# Unit tests for pick_clothes function
class TestPickClothes:
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

    allClothes = set()
    for clothes in clothes_by_weather.values():
        allClothes.update(clothes)
    for clothes in clothes_by_occasion.values():
        allClothes.update(clothes)

    def test_no_arguments(self, capsys):
        pick_clothes()
        captured = capsys.readouterr()
        assert "Try these clothes! They look good on you: " in captured.out
        assert len(captured.out.strip()) > len(
            "Try these clothes! They look good on you: "
        )

    def test_all_supported_weather(self, capsys):
        supported_weather = ["sunny", "rainy", "snowy", "windy"]
        for weather in supported_weather:
            pick_clothes(weather=weather)
            captured = capsys.readouterr()
            assert (
                f"You chose: '{weather}', so why not wear this bad boy? "
                in captured.out
            )
            assert len(captured.out.strip()) > len(
                f"You chose: '{weather}', so why not wear this bad boy? "
            )
            assert any(
                clothes in captured.out for clothes in self.clothes_by_weather[weather]
            )

    def test_all_supported_occasion(self, capsys):
        supported_occasions = ["casual", "formal", "athletic", "party", "beach"]
        for occasion in supported_occasions:
            pick_clothes(occasion=occasion)
            captured = capsys.readouterr()
            assert (
                f"You chose: '{occasion}', so why not wear this bad boy? " in captured.out
            )
            assert len(captured.out.strip()) > len(
                f"You chose: '{occasion}', so why not wear this bad boy? "
            )
            assert any(
                clothes in captured.out for clothes in self.clothes_by_occasion[occasion]
            )

    def test_both_valid_weather_and_occasion(self, capsys):
        pick_clothes(weather="sunny", occasion="casual")
        captured = capsys.readouterr()
        assert (
            "Good choice! For your weather" in captured.out
            or "Sorry but your weather and occasion didn't fit!" in captured.out
        )

    def test_invalid_weather(self, capsys):
        pick_clothes(weather="invalid")
        captured = capsys.readouterr()
        assert "Oopsie poopsie! :( 'invalid' isn't a weather!" in captured.out
        assert "Choose from: sunny, rainy, snowy, windy" in captured.out
        assert "Otherwise, what do you think of these clothes? " in captured.out

    def test_invalid_occasion(self, capsys):
        pick_clothes(occasion="invalid")
        captured = capsys.readouterr()
        assert "Oopsie poopsie! :( 'invalid' isn't a real occasion!" in captured.out
        assert "Choose from: casual, formal, athletic, party, beach" in captured.out
        assert "Otherwise, what do you think of these clothes? " in captured.out

    def test_invalid_weather_valid_occasion(self, capsys):
        supported_occasions = ["casual", "formal", "athletic", "party", "beach"]
        for occasion in supported_occasions:
            pick_clothes(weather="invalid", occasion=occasion)
            captured = capsys.readouterr()
            assert "Oopsie poopsie! :( 'invalid' isn't a weather!" in captured.out
            assert "Choose from: sunny, rainy, snowy, windy" in captured.out
            assert "Otherwise, what do you think of these clothes? " in captured.out

    def test_valid_weather_invalid_occasion(self, capsys):
        supported_weather = ["sunny", "rainy", "snowy", "windy"]
        for weather in supported_weather:
            pick_clothes(weather=weather, occasion="invalid")
            captured = capsys.readouterr()
            assert "Oopsie poopsie! :( 'invalid' isn't a real occasion!" in captured.out
            assert "Choose from: casual, formal, athletic, party, beach" in captured.out
            assert "Otherwise, what do you think of these clothes? " in captured.out

    def test_both_invalid(self, capsys):
        pick_clothes(weather="invalid", occasion="invalid")
        captured = capsys.readouterr()
        assert "Oopsie poopsie! :( 'invalid' isn't a weather!" in captured.out
        assert "Choose from: sunny, rainy, snowy, windy" in captured.out
        assert "Oopsie poopsie! :( 'invalid' isn't a real occasion!" in captured.out
        assert "Choose from: casual, formal, athletic, party, beach" in captured.out
        assert "Otherwise, what do you think of these clothes? " in captured.out

class TestPickFood:
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
    def test_default_pick(self, capsys):
        pick_food()
        out = capsys.readouterr().out.lower()
        assert "how about:" in out

    def test_valid_restriction(self, capsys):
        pick_food("vegan")
        out = capsys.readouterr().out.lower()
        assert "for a vegan diet" in out
        assert "try" in out

    def test_invalid_restriction(self, capsys):
        pick_food("carnivore")
        out = capsys.readouterr().out.lower()
        assert "sorry" in out or "not a supported restriction" in out
        assert "choose from" in out

    def test_case_insensitive(self, capsys):
        pick_food("VeGeTaRiAn")
        out = capsys.readouterr().out.lower()
        assert "for a vegetarian diet" in out

    def test_alias_anything(self, capsys):
        pick_food("anything")
        out = capsys.readouterr().out.lower()
        assert "how about:" in out

# Unit tests for pick_color function
class TestPickColor:
    happy_colors = [
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
    summer_colors = [
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
    energetic_colors = [
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

    def test_no_arguments(self, capsys):
        pick_color()
        captured = capsys.readouterr()
        assert "Here's a random color for you:" in captured.out
        assert len(captured.out.strip()) > len("Here's a random color for you:")

    def test_all_supported_moods(self, capsys):
        supported_moods = ["happy", "sad", "calm", "energetic", "angry"]
        for mood in supported_moods:
            pick_color(mood=mood)
            captured = capsys.readouterr()
            assert f"For your {mood} mood, try:" in captured.out

    def test_all_supported_seasons(self, capsys):
        supported_seasons = ["winter", "fall", "summer", "spring"]
        for season in supported_seasons:
            pick_color(season=season)
            captured = capsys.readouterr()
            assert f"For {season} season, try:" in captured.out

    def test_mood_happy(self, capsys):
        pick_color(mood="happy")
        captured = capsys.readouterr()
        assert "For your happy mood, try:" in captured.out
        assert any(color in captured.out for color in self.happy_colors)

    def test_invalid_mood(self, capsys):
        pick_color(mood="confused")
        captured = capsys.readouterr()
        assert "Sorry, 'confused' is not a supported mood" in captured.out
        assert "Picking from default list instead:" in captured.out

    def test_season_summer(self, capsys):
        pick_color(season="summer")
        captured = capsys.readouterr()
        assert "For summer season, try:" in captured.out
        assert any(color in captured.out for color in self.summer_colors)

    def test_invalid_season(self, capsys):
        pick_color(season="temp")
        captured = capsys.readouterr()
        assert "Sorry, 'temp' is not a valid season" in captured.out
        assert "Picking from default list instead:" in captured.out

    def test_both_valid_mood_and_season(self, capsys):
        pick_color(mood="calm", season="spring")
        captured = capsys.readouterr()
        assert "Perfect match!" in captured.out or "No perfect match" in captured.out

    def test_both_invalid(self, capsys):
        pick_color(mood="sleepy", season="temp")
        captured = capsys.readouterr()
        assert (
            "Sorry, 'sleepy' is not a valid mood and 'temp' is not a valid season"
            in captured.out
        )
        assert "Picking from default list instead:" in captured.out

    def test_invalid_mood_valid_season(self, capsys):
        pick_color(mood="confused", season="summer")
        captured = capsys.readouterr()
        assert "Sorry, 'confused' is not a valid mood" in captured.out
        assert "Using just your summer season instead, try:" in captured.out
        assert any(color in captured.out for color in self.summer_colors)

    def test_valid_mood_invalid_season(self, capsys):
        pick_color(mood="energetic", season="temp")
        captured = capsys.readouterr()
        assert "Sorry, 'temp' is not a valid season" in captured.out
        assert "Using just your energetic mood instead, try:" in captured.out
        assert any(color in captured.out for color in self.energetic_colors)


# Unit tests for pick_activity function
class TestPickActivity:
    weather_activities = {
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
    energy_activities = {
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

    all_activities = set()
    for activities in energy_activities.values():
        all_activities.update(activities)

    def test_no_arguments(self, capsys):
        pick_activity()
        captured = capsys.readouterr()
        assert "Try this activity: " in captured.out
        assert len(captured.out.strip()) > len("Try this activity: ")

    def test_all_supported_weather(self, capsys):
        supported_weather = ["sunny", "cloudy", "rainy", "snowy"]
        for weather in supported_weather:
            pick_activity(weather=weather)
            captured = capsys.readouterr()
            assert "Try this activity: " in captured.out
            assert len(captured.out.strip()) > len("Try this activity: ")
            assert any(
                activity in captured.out
                for activity in (
                    set(self.weather_activities[weather])
                    | set(self.weather_activities["any"])
                )
            )

    def test_all_supported_energy(self, capsys):
        supported_energy = ["low", "medium", "high"]
        for energy in supported_energy:
            pick_activity(energy_level=energy)
            captured = capsys.readouterr()
            assert "Try this activity: " in captured.out
            assert len(captured.out.strip()) > len("Try this activity: ")
            assert any(
                activity in captured.out for activity in self.energy_activities[energy]
            )

    def test_all_valid_weather_energy_combos(self, capsys):
        supported_weather = ["sunny", "cloudy", "rainy", "snowy"]
        supported_energy = ["low", "medium", "high"]
        for weather in supported_weather:
            for energy in supported_energy:
                pick_activity(weather=weather, energy_level=energy)
                captured = capsys.readouterr()
                assert "Try this activity: " in captured.out
                assert len(captured.out.strip()) > len("Try this activity: ")
                assert any(
                    activity in captured.out
                    for activity in self.energy_activities[energy]
                )
                assert any(
                    activity in captured.out
                    for activity in (
                        set(self.weather_activities[weather])
                        | set(self.weather_activities["any"])
                    )
                )

    def test_invalid_weather(self, capsys):
        pick_activity(weather="invalid")
        captured = capsys.readouterr()
        assert "Sorry, 'invalid' is not a supported weather type." in captured.out
        assert "Please choose from: sunny, cloudy, rainy, snowy" in captured.out
        assert "In the meantime, try this activity: " in captured.out

    def test_invalid_energy(self, capsys):
        pick_activity(energy_level="invalid")
        captured = capsys.readouterr()
        assert "Sorry, 'invalid' is not a supported energy level." in captured.out
        assert "Please choose from: low, medium, high" in captured.out
        assert "In the meantime, try this activity: " in captured.out

    def test_invalid_weather_valid_energy(self, capsys):
        pick_activity(weather="invalid", energy_level="low")
        captured = capsys.readouterr()
        assert "Sorry, 'invalid' is not a supported weather type." in captured.out
        assert "Please choose from: sunny, cloudy, rainy, snowy" in captured.out
        assert "In the meantime, try this activity: " in captured.out

    def test_valid_weather_invalid_energy(self, capsys):
        pick_activity(weather="sunny", energy_level="invalid")
        captured = capsys.readouterr()
        assert "Sorry, 'invalid' is not a supported energy level." in captured.out
        assert "Please choose from: low, medium, high" in captured.out
        assert "In the meantime, try this activity: " in captured.out

    def test_invalid_weather_invalid_energy(self, capsys):
        pick_activity(weather="invalid", energy_level="invalid")
        captured = capsys.readouterr()
        assert "Sorry, 'invalid' is not a supported weather type." in captured.out
        assert "Please choose from: sunny, cloudy, rainy, snowy" in captured.out
        assert "In the meantime, try this activity: " in captured.out
