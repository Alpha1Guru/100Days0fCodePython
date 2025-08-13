def get_two_digit():
    digits = input("Give me a two digit number: ")
    if (len(digits) != 2 
        or digits[0] not in "0123456789"
        or digits[1] not in "0123456789"
        ):
        print("Not a two digit number!".upper())
        return get_two_digit()
    else:
        return digits

two_digit_number = get_two_digit()

addition_of_two_digits = int(two_digit_number[0]) + int(two_digit_number[1])
print(f"The addition: {addition_of_two_digits}")