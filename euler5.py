# find the smallest number evenly divisible by all numbers between 1 and 20

factors = list(range(1, 21))
var = 1
product = 1


def test(product):
    for factor in factors:
        if product % factor != 0:
            return(False)
    return(True)

while not test(product):
    product = factors[-1] * var
    var += 1

print(product)
