#! /usr/bin/env python3
# finding the sum of all even fibonacci numbers below 4 million

sequence = [1, 2]

while sequence[-1] < 4_000_000:
    sequence.append(sequence[-1] + sequence[-2])

even_numbers = [n for n in sequence if n % 2 == 0]
print(sum(even_numbers))
