#! /usr/bin/env python3
# What is the largest prime factor of the number 600851475143 ?

def is_prime(number: int) -> bool:
    """tell me if a number is prime or not"""
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def decompose(number: int) -> (int, int):
    """return the first prime factor and its counterpart"""
    for i in range(2, number):
        if is_prime(i) and number % i == 0:
            return i, int(number / i)
            

if __name__ == '__main__':
    factors = [600851475143]
    prime_factors = []

    while factors:
        factor = factors.pop()
        if is_prime(factor):
            prime_factors.append(factor)
        else:
            for i in decompose(factor):
                factors.append(i)

    print(sorted(prime_factors)[-1])

