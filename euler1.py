#! /usr/bin/env python3
# Find the sum of all the multiples of 3 or 5 below 1000.

sum_of_multiples = 0
for number in range(1, 1000):
    print(number)
    if number % 3 == 0 or number % 5 == 0:
        sum_of_multiples += number

print(sum_of_multiples)

