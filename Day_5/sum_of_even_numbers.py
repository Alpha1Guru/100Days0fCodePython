print("First Attempt")
for i in range(0, 101, 2):
    print(i)
print()

print("Second Attempt")
for i in range(1, 101):
    if i%2 != 0:
        continue
    else:
        print(i)
print()

print("Third Attempt")
total = 0
for i in range(1, 51):
    print(i * 2)
    total += i * 2
print(f"The total even numbers from 1 to 100 are: {total}")