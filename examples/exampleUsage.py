from dailyDecisionPackage import dailyDecision

print("=" * 70)
print("DAILY DECISION PACKAGE - EXAMPLE USAGE")
print("=" * 70)
print()

# PICK COLOR FUNCTION
print("\n" + "=" * 70)
print("1. pick_color(mood, season) - Get color suggestions based on mood and/or season")
print("=" * 70)
print()

print("Example 1.1: No arguments - random color")
print("-" * 70)
dailyDecision.pick_color()
print()

print("Example 1.2: Only mood provided")
print("-" * 70)
dailyDecision.pick_color(mood="happy")
print()

print("Example 1.3: Only season provided")
print("-" * 70)
dailyDecision.pick_color(season="summer")
print()

print("Example 1.4: Both mood and season provided")
print("-" * 70)
dailyDecision.pick_color(mood="happy", season="summer")
print()

print("Example 1.5: Invalid mood")
print("-" * 70)
dailyDecision.pick_color(mood="upset")
print()

print("Example 1.6: Invalid season")
print("-" * 70)
dailyDecision.pick_color(season="test")
print()

print("Example 1.7: Valid season but invalid mood")
print("-" * 70)
dailyDecision.pick_color(season="summer", mood="upset")
print()

print("Example 1.8: Valid mood but invalid season")
print("-" * 70)
dailyDecision.pick_color(season="test", mood="energetic")
print()

print("Example 1.9: Both invalid")
print("-" * 70)
dailyDecision.pick_color(season="test", mood="upset")
print()

# PICK CLOTHES FUNCTION
print("\n" + "=" * 70)
print(
    "2. pick_clothes(weather, occasion) - Get clothing suggestions based on weather and/or occasion"
)
print("=" * 70)
print()

print("Example 2.1: No arguments - random clothing")
print("-" * 70)
dailyDecision.pick_clothes()
print()

print("Example 2.2: Only weather provided")
print("-" * 70)
dailyDecision.pick_clothes(weather="sunny")
print()

print("Example 2.3: Only occasion provided")
print("-" * 70)
dailyDecision.pick_clothes(occasion="casual")
print()

print("Example 2.4: Both weather and occasion provided")
print("-" * 70)
dailyDecision.pick_clothes(weather="rainy", occasion="formal")
print()

print("Example 2.5: Invalid weather")
print("-" * 70)
dailyDecision.pick_clothes(weather="invalid")
print()

print("Example 2.6: Invalid occasion")
print("-" * 70)
dailyDecision.pick_clothes(occasion="invalid")


# PICK FOOD FUNCTION
print("\n" + "=" * 70)
print(
    "3. pick_food(dietary_restriction) - Get food suggestions based on dietary restrictions"
)
print("=" * 70)
print()

print("Example 3.1: No restriction - random food")
print("-" * 70)
dailyDecision.pick_food()
print()

print("Example 3.2: dietary_restriction provided")
print("-" * 70)
dailyDecision.pick_food("vegetarian")
print()

print("Example 3.3: Unsupported restriction")
print("-" * 70)
dailyDecision.pick_food("invalid")
print()

# PICK ACTIVITY FUNCTION
print("\n" + "=" * 70)
print(
    "4. pick_activity(weather, energy_level) - Get activity suggestions based on weather and/or energy level"
)
print("=" * 70)
print()

print("Example 4.1: No arguments - random activity")
print("-" * 70)
dailyDecision.pick_activity()
print()

print("Example 4.2: Only weather provided")
print("-" * 70)
dailyDecision.pick_activity(weather="sunny")
print()

print("Example 4.3: Only energy level provided")
print("-" * 70)
dailyDecision.pick_activity(energy_level="high")
print()

print("Example 4.4: Both weather and energy level provided")
print("-" * 70)
dailyDecision.pick_activity(weather="snowy", energy_level="low")
print()

print("Example 4.5: Invalid weather")
print("-" * 70)
dailyDecision.pick_activity(weather="invalid")
print()

print("Example 4.6: Invalid energy level")
print("-" * 70)
dailyDecision.pick_activity(energy_level="invalid")
print()

