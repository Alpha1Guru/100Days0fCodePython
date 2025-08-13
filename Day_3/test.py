import timeit
import random

# This script compares the performance of two methods for checking if a number is even or odd:
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
# Generate a dataset of 1,000,000 random large numbers
numbers = [random.randint(10**12, 10**13) for _ in range(1000000)]

# mod_check applied across the dataset
def batch_mod_check():
    for number in numbers:
        mod_check(number)

# string_check applied across the dataset (with direct string conversion)
def batch_string_check():
    for number in numbers:
        string_check(str(number))

# Time them
mod_time = timeit.timeit(batch_mod_check, number=1)
string_time = timeit.timeit(batch_string_check, number=1)

print(f"mod_check total time: {mod_time:.4f} seconds")
print(f"string_check total time: {string_time:.4f} seconds")
