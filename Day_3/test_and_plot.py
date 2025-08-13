import timeit
import random
import matplotlib.pyplot as plt

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

#To Record their time for ploting
mod_times = []
string_times = []

# Time them
i = 0
while i < 100:  # Or any number of cycles
    mod_time = timeit.timeit(batch_mod_check, number=1)
    string_time = timeit.timeit(batch_string_check, number=1)
    mod_times.append(mod_time)
    string_times.append(string_time)

    print(f"No.{i+1}")
    print("Mod Was First")
    print(f"mod_check total time: {mod_time:.4f} seconds")
    print(f"string_check total time: {string_time:.4f} seconds")
    i += 1

#Plot Graph
plt.plot(mod_times, label='mod_check')
plt.plot(string_times, label='string_check')
plt.xlabel('Run #')
plt.ylabel('Time (s)')
plt.legend()
plt.title('Performance Over Iterations')
plt.show()

#Print Average
print(f"Average mod_check time: {sum(mod_times)/len(mod_times):.4f} seconds")
print(f"Average string_check time: {sum(string_times)/len(string_times):.4f} seconds")