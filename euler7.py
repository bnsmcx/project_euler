# ~ What is the 10 001st prime number

from sympy import isprime

counter = 0
n = 1

while True:
    if isprime(n):
        counter += 1
        if counter == 10001:
            break
    n += 1

print(counter)
print(n)
