def mod_check(number):
    if number % 2 == 0:
        return f"{number} is an even number."
    else:
        return f"{number} is an odd number."

def string_check(number_str):
    if str(number_str)[-1] in "02468":
        return f"{number_str} is an even number."
    else:
        return f"{number_str} is an odd number."
