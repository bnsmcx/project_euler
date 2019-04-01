# ~ Find the difference between the sum of the squares of the first 
# ~ one hundred natural numbers and the square of the sum

var = 100

numbers = list(range(1, var + 1))
sum_squares = sum([x**2 for x in numbers])
square_of_sum = sum(numbers)**2    
    
print(square_of_sum - sum_squares)
