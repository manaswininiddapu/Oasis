while True:
    try:
        # Taking user input
        Height = float(input("Please enter your height in inches: "))
        Weight = float(input("Please enter your weight in pound: "))
    except ValueError:
        # Validation error.
        print("Please provide valid input.")
        continue  # Return to the start of the loop.
    else:
        if Height <= 0 or Weight <= 0:
            print("Your input must not be zero or less.")
            continue
        else:
            # Calculate BMI
            BMIIndex = round(Weight / (Height * Height) * 703, 2)

            # Print the output
            print("Your Body Mass Index is: ", BMIIndex)

            if BMIIndex < 18.5:
                print("Underweight.")
            elif BMIIndex <= 24.9:
                print("Normal.")
            elif BMIIndex <= 29.9:
                print("Overweight.")
            else:
                print("Obese.")
        break
