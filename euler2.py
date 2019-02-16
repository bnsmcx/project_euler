# finding the sum of all even fibonacci numbers below 4 million

fib_numbers = [2, 3]
even_fib = []
sum = 0

while fib_numbers[-1] < 4000000:
    number = fib_numbers[-1] + fib_numbers[-2]
    if number < 4000000:
        fib_numbers.append(number)
    elif number > 4000000:
        break
    else:
        continue
        
for n in fib_numbers:
    if n % 2 == 0:
        even_fib.append(n)
    else:
        continue

print(even_fib)
        
for n in even_fib:
    sum += n
    
print(sum)

