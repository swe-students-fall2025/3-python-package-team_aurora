import pytest
from dailyDecisionPackage.dailyDecision import pick_color

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
