from memory_profiler import profile
import random

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

numbers = [random.randint(10**12, 10**13) for _ in range(1000000)]

@profile
def batch_mod_check():
    for number in numbers:
        mod_check(number)

@profile
def batch_string_check():
    for number in numbers:
        string_check(str(number))

if __name__ == "__main__":
    batch_mod_check()
    batch_string_check()
