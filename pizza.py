####################################################################################################################

# Program: Pizza Area Calculator
# Author: Jayce Johnson
# Date: October 9th, 2024
# Description: Calculates the area of each pizza slice according to the diameter of the whole pizza

####################################################################################################################

# Setting the value for pi as a constant
PI = 3.141592653589793238462643383

# Prompts the user for pizza size and stores in diameter variable
diameter = input("PLease enter the diameter of your pizza (in inches). Press 0 to end the program")

# Ends the program if 0 is pressed
if diameter == 0:
    exit()

# Using try to catch errors, checks that input is within the 8-24 inch range.
try:

    if float(diameter) < 0:
        print("Please enter a positive number.")

    elif float(diameter) > 24:
        print("Pizza is too big!")

    elif float(diameter) < 8:
        print("Pizza is too small!")

    # Diameter between 8 and <12 = 6 slices
    elif float(diameter) >= 8 and float(diameter) < 12:

        # Finding the radius to make it easier for us to calculate area
        radius = float(diameter) / 2

        # Setting the value for radius squared so I don't have to calculate that either
        radius_squared = float(radius) * float(radius)

        # Finding the area of the pizza based on the above calculations
        pizza_area = radius_squared * PI

        # Calculating the size of each slice
        # 6 Slices
        slices_6 = round((pizza_area / 6), 2)

        # 8 Slices
        slices_8 = round((pizza_area / 8), 2)

        # 10 Slices
        slices_10 = round((pizza_area / 10), 2)

        # 12 Slices
        slices_12 = round((pizza_area / 12), 2)

        # 16 Slices
        slices_16 = round((pizza_area / 16), 2)

        print(f"\nA {diameter} inch pizza can be cut into 6 slices. Each slice would be {slices_6} inches.\n")

    # Diameter between 12 and <14 = 6 or 8 slices
    elif float(diameter) >= 12 and float(diameter) < 14:

        # Finding the radius to make it easier for us to calculate area
        radius = float(diameter) / 2

        # Setting the value for radius squared so I don't have to calculate that either
        radius_squared = float(radius) * float(radius)

        # Finding the area of the pizza based on the above calculations
        pizza_area = radius_squared * PI

        # Calculating the size of each slice
        # 6 Slices
        slices_6 = round((pizza_area / 6), 2)

        # 8 Slices
        slices_8 = round((pizza_area / 8), 2)

        # 10 Slices
        slices_10 = round((pizza_area / 10), 2)

        # 12 Slices
        slices_12 = round((pizza_area / 12), 2)

        # 16 Slices
        slices_16 = round((pizza_area / 16), 2)

        print(f"""\

A {diameter} inch pizza can be cut into 6 or 8 slices.
If cut into 6 slices, each slice will be {slices_6} inches.
If cut into 8 slices, each slice will be {slices_8} inches.\n""")


    # Diameter between 14 and <16 = 6, 8, or 10 slices
    elif float(diameter) >= 14 and float(diameter) < 16:

        # Finding the radius to make it easier for us to calculate area
        radius = float(diameter) / 2

        # Setting the value for radius squared so I don't have to calculate that either
        radius_squared = float(radius) * float(radius)

        # Finding the area of the pizza based on the above calculations
        pizza_area = radius_squared * PI

        # Calculating the size of each slice
        # 6 Slices
        slices_6 = round((pizza_area / 6), 2)

        # 8 Slices
        slices_8 = round((pizza_area / 8), 2)

        # 10 Slices
        slices_10 = round((pizza_area / 10), 2)

        # 12 Slices
        slices_12 = round((pizza_area / 12), 2)

        # 16 Slices
        slices_16 = round((pizza_area / 16), 2)

        print(f"""\

A {diameter} inch pizza can be cut into 6, 8, or 10 slices.
If cut into 6 slices, each slice will be {slices_6} inches.
If cut into 8 slices, each slice will be {slices_8} inches.
If cut into 10 slices, each slice will be {slices_10} inches.\n""")

# Diameter between 16 and <20 = 6, 8, 10, or 12 slices
    elif float(diameter) >= 16 and float(diameter) < 20:

        # Finding the radius to make it easier for us to calculate area
        radius = float(diameter) / 2

        # Setting the value for radius squared so I don't have to calculate that either
        radius_squared = float(radius) * float(radius)

        # Finding the area of the pizza based on the above calculations
        pizza_area = radius_squared * PI

        # Calculating the size of each slice
        # 6 Slices
        slices_6 = round((pizza_area / 6), 2)

        # 8 Slices
        slices_8 = round((pizza_area / 8), 2)

        # 10 Slices
        slices_10 = round((pizza_area / 10), 2)

        # 12 Slices
        slices_12 = round((pizza_area / 12), 2)

        # 16 Slices
        slices_16 = round((pizza_area / 16), 2)

        print(f"""\

A {diameter} inch pizza can be cut into 6, 8, 10, or 12 slices.
If cut into 6 slices, each slice will be {slices_6} inches.
If cut into 8 slices, each slice will be {slices_8} inches.
If cut into 10 slices, each slice will be {slices_10} inches.
If cut into 12 slices, each slice will be {slices_12} inches.\n""")

    # Diameter between 20 and 24 = 6, 8, 10, 12, or 16 slices
    elif float(diameter) >= 20 and float(diameter) <= 24:

        # Finding the radius to make it easier for us to calculate area
        radius = float(diameter) / 2

        # Setting the value for radius squared so I don't have to calculate that either
        radius_squared = float(radius) * float(radius)

        # Finding the area of the pizza based on the above calculations
        pizza_area = radius_squared * PI

        # Calculating the size of each slice
        # 6 Slices
        slices_6 = round((pizza_area / 6), 2)

        # 8 Slices
        slices_8 = round((pizza_area / 8), 2)

        # 10 Slices
        slices_10 = round((pizza_area / 10), 2)

        # 12 Slices
        slices_12 = round((pizza_area / 12), 2)

        # 16 Slices
        slices_16 = round((pizza_area / 16), 2)

        print(f"""\

A {diameter} inch pizza can be cut into 6, 8, 10, 12, or 16 slices.
If cut into 6 slices, each slice will be {slices_6} inches.
If cut into 8 slices, each slice will be {slices_8} inches.
If cut into 10 slices, each slice will be {slices_10} inches.
If cut into 12 slices, each slice will be {slices_12} inches.
If cut into 16 slices, each slice will be {slices_16} inches.\n""")

except ValueError:
    print("Input must be numeric.")