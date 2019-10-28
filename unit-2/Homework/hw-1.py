total = 0
for num in range(1000, 10001):
    if num % 2 == 0:
        total = total + num

print(f"The sum of even numbers between 1000 and 10,000 is {total}")

total = 0
for num in range(1000, 10001):
    if num % 2 == 0:
        total += num

print(f"The sum of even numbers between 1000 and 10,000 is {total}")