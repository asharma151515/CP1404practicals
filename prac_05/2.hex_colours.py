"""
CP1404/CP5632 Practical
Hexadecimal colour codes dictionary
"""

# Dictionary mapping color names to hexadecimal color codes
COLORS = {
    "Absolute Zero": "#0048BA",
    "Acid Green": "#B0BF1A",
    "Byzantine": "#BD33A4",
    "Candy Pink": "#E4717A",
    "Dark Brown": "#654321",
    "Indigo": "#4B0082",
    "Jasmine": "#F8de7e"

}

# User input for color name
color_name = input("Enter a color name: ").title()

# Check if the color name is in the dictionary and print the corresponding hexadecimal color code
if color_name in COLORS:
    print(f"The hexadecimal color code for {color_name} is {COLORS[color_name]}")
else:
    print("Color not found in the dictionary.")