# Ask the user for their birth year and store it in the variable 'year'.
year = int(input("Enter your birth year: "))

# Validate the birth year.
# If birth year is less than 1900, print an error message and exit the program.
if year < 1900:
    print("Invalid Year, it should not be earlier than 1900")
    exit()

else:
    # The Chinese Zodiac repeats every 12 years, with 1900 being the baseline
    # year and the Year of the Rat.
    zodiac_index = (year - 1900) % 12

    # Store the zodiac signs in their correct order.
    zodiac_signs = [
        "Rat (鼠 / Shǔ)",
        "Ox (牛 / Niú)",
        "Tiger (虎 / Hǔ)",
        "Rabbit (兔 / Tù)",
        "Dragon (龙 / Lóng)",
        "Snake (蛇 / Shé)",
        "Horse (马 / Mǎ)",
        "Goat (羊 / Yáng)",
        "Monkey (猴 / Hóu)",
        "Rooster (鸡 / Jī)",
        "Dog (狗 / Gǒu)",
        "Pig (猪 / Zhū)"
    ]

    # Use the calculated index to determine the user's Chinese Zodiac sign.
    zodiac = zodiac_signs[zodiac_index]

    # Display the result.
    print("Your Chinese Zodiac Sign is:", zodiac)