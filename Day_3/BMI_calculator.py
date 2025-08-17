def main():
    # Height Validation
    while True:
        height = input("Enter your height in meters: ")
        if height.count('.') <= 1 and all(char in "0123456789." for char in height):
            try:
                height = float(height)
                if height > 0:
                    break
                else:
                    print("Height must be a positive number!")
            except ValueError:
                print("Invalid number format!")
        else:
            print("Not a positive number!")

    # Weight Validation
    while True:
        weight = input("Enter your weight in kilograms: ")
        if weight.count('.') <= 1 and all(char in "0123456789." for char in weight):
            try:
                weight = float(weight)
                if weight > 0:
                    break
                else:
                    print("Weight must be a positive number!")
            except ValueError:
                print("Invalid number format!")
        else:
            print("Not a positive number!")

    # BMI Calculation
    BMI_value = round(weight / height**2, 1)

    # BMI Classification
    if BMI_value < 18.5:
        category = "underweight"
    elif BMI_value < 25:
        category = "normal weight"
    elif BMI_value < 30:
        category = "overweight"
    elif BMI_value < 35:
        category = "obese"
    else:
        category = "clinically obese! Hit the Gym!!"

    print(f"\nYour BMI is {BMI_value}, you are {category}.\n")

# Run once
main()