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

# #A new way to calculate 
# def get_two_digit():
#     digits = input("Give me a tow digit number: ")
#     if (len(digits) != 2 or digits.isdigit() == False):
#         print("Not a two digit number!".upper())
#         return get_two_digit()
#     else:
#         return digits

# #Copilot
# def get_two_digits():
#     while True:
#         digits = input("Give me a two-digit number (can be negative): ").strip()

#         # Remove leading minus sign for validation
#         cleaned_digits = digits.lstrip('-')

#         # Check if it's numeric and exactly two digits
#         if cleaned_digits.isdigit() and len(cleaned_digits) == 2:
#             return digits
#         else:
#             print("❌ INVALID INPUT: Please enter a valid two-digit number (e.g., 23, -45, 09).")

# def add_digits(number_str):
#     # Remove minus sign if present
#     is_negative = number_str.startswith('-')
#     digits_only = number_str.lstrip('-')

#     # Convert characters to integers and sum them
#     digit_sum = sum(int(d) for d in digits_only)

#     # Optionally, reflect negativity in output (if needed)
#     return -digit_sum if is_negative else digit_sum

# # Main execution
# two_digit_number = get_two_digits()
# addition_of_two_digits = add_digits(two_digit_number)

# print(f"✅ The addition of digits in {two_digit_number} is: {addition_of_two_digits}")



two_digit_number = get_two_digit()

addition_of_two_digits = int(two_digit_number[0]) + int(two_digit_number[1])
print(f"The addition: {addition_of_two_digits}")