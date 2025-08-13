def get_BMI(height, weight):
        return round(float(weight)/pow(float(height), 2))

while True:
    height = input("enter your height in m: ")
    weight = input("enter your weight in kg: ")

    print("Without them")
    BMI = float(weight)/(float(height) ** 2)
    print("Your BMI index is: {}".format(BMI))
    print("The type {type}".format(type=type(BMI)) )

    print("\nWith Function \"get_BMI()\"")
    print("Your BMI index is: {}".format(get_BMI(height, weight)))

    print("\nWith Round Function")
    BMI = round(float(weight)/(float(height) ** 2))
    print("Your BMI index is: {}".format(BMI))
    print("The type {type}".format(type=type(BMI)) )

    print("\nWith \"//\" - the floor division symbol")
    BMI = float(weight)//(float(height) ** 2)
    print("Your BMI index is: {}".format(BMI))
    print("The type {type}".format(type=type(BMI)) )
    print()