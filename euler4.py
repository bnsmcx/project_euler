# finding the largest 

def reverse(num):
    return(int(str(num)[::-1]))

def test_for_pali(numB):
    numA = 999
    while numA > 100:
        if (numB * numA) == reverse(numB * numA):
            palindromes.append(numB * numA)
            numA -= 1
            continue
        numA -= 1
            
palindromes = []            
numB = 999

while numB > 100:
    test_for_pali(numB)
    numB -= 1    

print(sorted(palindromes)[-1])
                    


