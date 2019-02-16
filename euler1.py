# finding the sum of all numbers divisivle by 3 or 5 between 1 and 1000

naturals = []
sum = 0

for n in range(1,1000):
    if n%3 == 0:
        naturals.append(n)
    elif n%5 == 0:
        naturals.append(n)
    else:
        continue
        
for n in naturals:    
    sum += n
    
print(sum)
