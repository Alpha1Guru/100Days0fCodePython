print("Welcome to the tip Calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, 15? "))
number_of_people_paying = int(input("How many people to split the bill? "))

bill_with_tip = total_bill * (1 + tip_percentage/100)
bill_for_each_person = round(bill_with_tip / number_of_people_paying, 2)
print("Each person should pay: ${bill}".format(bill=bill_for_each_person))