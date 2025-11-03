import pytest
from dailyDecisionPackage.dailyDecision import pick_color, pick_activity

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
            "go for a walk", "read a book at the park", "explore a new part of the city", "go for a run",
            "go hiking", "bike around your neighborhood", "go to the beach"
        ],
        "cloudy": [
            "watch the clouds"
        ],
        "rainy": [
            "dance in the rain"
        ],
        "snowy": [
            "make snow angels", "build a snowman", "snowball fight"
        ],
        "any": [
            "watch a movie or TV", "play a video game", "read a book indoors", "listen to a podcast",
            "listen to music", "write a journal entry", "call a friend", "play a board game",
            "solve a crossword", "clean your bedroom", "light exercise", "dance", "make a home-cooked meal",
            "arts & crafts", "yoga", "go to the gym", "go to the club", "go to a party", "clean the house",
            "painting", "go for a drive"
        ]
    }
    energy_activities = {
        "low": [
            "watch a movie or TV", "play a video game", "read a book indoors", "read a book at the park",
            "listen to a podcast", "listen to music", "write a journal entry", "call a friend",
            "play a board game", "solve a crossword", "watch the clouds", "painting"
        ],
        "medium": [
            "go for a walk", "clean your bedroom", "light exercise", "dance", "dance in the rain",
            "make a home-cooked meal", "arts & crafts", "yoga", "make snow angels", "build a snowman",
            "go to the beach", "go for a drive"
        ],
        "high": [
            "go to the gym", "go for a run", "go hiking", "bike around your neighborhood", "go to the club",
            "go to a party", "clean the house", "snowball fight", "explore a new part of the city"
        ]
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
            assert any(activity in captured.out for activity in (
                set(self.weather_activities[weather]) | set(self.weather_activities["any"])
            ))

    def test_all_supported_energy(self, capsys):
        supported_energy = ["low", "medium", "high"]
        for energy in supported_energy:
            pick_activity(energy_level=energy)
            captured = capsys.readouterr()
            assert "Try this activity: " in captured.out
            assert len(captured.out.strip()) > len("Try this activity: ")
            assert any(activity in captured.out for activity in self.energy_activities[energy])
    
    def test_all_valid_weather_energy_combos(self, capsys):
        supported_weather = ["sunny", "cloudy", "rainy", "snowy"]
        supported_energy = ["low", "medium", "high"]
        for weather in supported_weather:
            for energy in supported_energy:
                pick_activity(weather=weather, energy_level=energy)
                captured = capsys.readouterr()
                assert "Try this activity: " in captured.out
                assert len(captured.out.strip()) > len("Try this activity: ")
                assert any(activity in captured.out for activity in self.energy_activities[energy])
                assert any(activity in captured.out for activity in (
                set(self.weather_activities[weather]) | set(self.weather_activities["any"])
                ))
    
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