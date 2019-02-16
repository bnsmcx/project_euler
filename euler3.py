# finding the largest prime factor of a given number

def is_prime(number):
    if number <= 2:
        return(True)
    else:
        for n in range(2, number):
            if number % n == 0:
                return(False)
        return(True)

primes = []

for i in range(3, 776001, 2): 
	if is_prime(i):
		primes.append(i)

test_number = 600851475143

for n in reversed(primes):
	if test_number % n == 0:
		print(n)
		break



