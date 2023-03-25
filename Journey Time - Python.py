print("Welcome to the distance calculator.")

double_km = False
double_miles = False
test = True

while test == True:

    try:
        mesurements = str(input("Would you like to calculate miles or kilometers?: "))
        mesurements = mesurements.lower()

        if mesurements == "km" or mesurements == "kilometers" or mesurements == "k":
            while True:
                try:
                    double_check = str(input("You entered in kilometers is this corect?: "))
                    double_check = double_check.lower()

                    if double_check == "ye" or double_check == "yes" or double_check == "y" or double_check == "ys":
                        print("kilometers recorded.")
                        double_km = True
                        double_miles = False
                        test = False
                        break

                    elif double_check == "n" or double_check == "no" or double_check == "nah" or double_check == "nope":
                        print("kilometers were not recorded but miles were.")
                        double_miles = True
                        double_km = False
                        test = False
                        break

                except ValueError:
                    print("Make sure you enter in letters not number.")
                    print("Try again")

        elif mesurements == "m" or mesurements == "miles" or mesurements == "miles":

            while True:
                try:
                    double_check = str(input("You entered in miles is this corect?: "))
                    double_check = double_check.lower()

                    if double_check == "ye" or double_check == "yes" or double_check == "y" or double_check == "ys":
                        print("Miles recorded.")
                        double_miles = True
                        double_km = False
                        test = False
                        break

                    elif double_check == "n" or double_check == "no" or double_check == "nah" or double_check == "nope":
                        print("Miles were not recorded but kilometers were.")
                        double_miles = False
                        double_km = True
                        test = False
                        break

                except ValueError:
                    print("Make sure you enter in letters not number.")
                    print("Try again")

    except ValueError:
        print("You need to input the mesurements in letters not numbers.")
        print("Try again")

if double_miles == True:
    while double_miles == True:
        try:
            distance = float(input("Input the distance you will be traveling in miles: "))
            break
        except ValueError:
            print("Please input the distance in number form. You can use a decimal place if required.")
            print("Try again below.")

    while double_miles == True:
        try:
            speed = float(input("Input the speed you will traveling in mph: "))
            break
        except ValueError:
            print("Please input the speed in number form. You can use a decimal place if required.")
            print("Try again below.")

    miles_time = distance / speed

    print(f"Your journey will take {miles_time:.2f} hours")
    print("")
    print("In kilometers you would be traveling " + str(int(distance * 1.609)) + " kilometers.")
    print("Your average speed in kilomiters an hour would be " + str(int(speed * 1.609)) + "kmh.")
else:
    while double_km == True:
        try:
            distance = float(input("Input the distance you will be traveling in kilometers: "))
            break
        except ValueError:
            print("Please input the distance in number form. You can use a decimal place if required.")
            print("Try again below.")

    while double_km == True:
        try:
            speed = float(input("Input the speed you will traveling in kmh: "))
            break
        except ValueError:
            print("Please input the speed in number form. You can use a decimal place if required.")
            print("Try again below.")

    km_time = distance / speed

    print(f"Your journey will take {km_time:.2f} hours")
    print("")
    print("In kilometers you would be traveling " + str(int(distance / 1.609)) + " miles.")
    print("Your average speed in kilomiters an hour would be " + str(int(speed / 1.609)) + "mph.")
print("")
print("Hopefully this is useful.")
print("Enjoy your journey!")
