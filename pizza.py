####################################################################################################################

# Program: Pizza Area Calculator
# Author: Jayce Johnson
# Date: October 9th, 2024
# Description: Calculates the area of each pizza slice according to the diameter of the whole pizza

####################################################################################################################

# Adds the ability to exit the program by pressing 0
exitbutton = input("Welcome to pizza calculator.\nPress enter to start, or 0 to quit.")

# Prompts the user for pizza size and stores in diameter variable
diameter = input("Please enter the diameter of your pizza (in inches). Press 0 to end the program. ")

# While loop for easier validation
while exitbutton != "0":

# Once again ends the program if 0 is pressed
    if diameter == "0":
        print("Shutting down...")
        exit()

# Checks to see that user input is a number
    elif diameter.isalpha():
        print("Input must be numeric")

# Checks that the pizza is not over 24 inches
    elif float(diameter) > 24:
        print("Pizza is too big!")
        diameter = input("Please enter the diameter of your pizza (in inches). Press 0 to end the program. ")

# Checks that the pizza is not less than 8 inches
    elif float(diameter) < 8:
        print("Pizza is too small!")
        diameter = input("Please enter the diameter of your pizza (in inches). Press 0 to end the program. ")









# NEED TO ADD FUNCTIONALITY. THIS JUST PRINTS
# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# Hopefully the screaming reminds me to go back and fix.
    elif float(diameter) >= 8 and float(diameter) < 12:
        print("6 slices")
        break

    elif float(diameter) >= 12 and float(diameter) < 14:
        print("6-8 slices")
        break

    elif float(diameter) >= 14 and float(diameter) < 16:
        print("6, 8, or 10 slices")
        break

    elif float(diameter) >= 16 and float(diameter) < 20:
        print("6, 8, 10, or 12")
        break

    elif float(diameter) >= 20 and float(diameter) <= 24:
        print("6, 8, 10, 12, or 16")
        break









# Exits the loop if proper input is given
    else:
        break
