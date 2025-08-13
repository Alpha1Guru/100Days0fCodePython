while True:
    year = int(input("Which year do you want to check? "))
    leap_year = False
    if year%4 == 0:
        leap_year = True
    if year%100 == 0:
        leap_year = False
    if year%400 == 0:
        leap_year = True
    print(f"It is a {leap_year} assumption")
    print(f"")
#Trying to combine the logic
    leap_year = False
    if (year%4 == 0) and ((year%100 != 0) or (year%400 == 0)):
        leap_year = True
    print(f"The Second Says it is a {leap_year} assumption")