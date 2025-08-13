def main():
    height = ""
    while not height.isdigit():
        height = input("enter your height in m: ")
    height = float(input("enter your height in m: ") )
    weight = ""
    while not weight.isdigit():
        height = input("enter your height in m: ")
    weight = float(input("enter your weight in kg: "))

    BMI_value = float(round(weight/height**2, 1))

    if BMI_value <= 18.5:
        print(f"You BMI is {BMI_value}, you are underweight.")
    elif BMI_value <= 25:
        print(f"Your BMI is {BMI_value}, you have a normal weight.")
    elif BMI_value <= 30:
        print(f"Your BMI is {BMI_value}, you are overweight.")
    elif BMI_value <= 35:
        print(f"Your BMI is {BMI_value}, you are obese.")
    else:
        print(f"Your BMI is {BMI_value}, you are clinically obese! Hit the Gym!!")
    print()
while True:
    main()