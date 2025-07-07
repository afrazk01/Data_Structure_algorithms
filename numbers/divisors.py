# return the number of divisor of a number in a string 
# Brute force solutions 
from math import sqrt
def diviors(number):
    for i in range(1,number+1):
        if number % i == 0:
            result.append(i)
    return result

# another solution
def div(n):
    for i in range(1, n//2):
        if n % i == 0:
            result.append(i)
    result.append(number)
    return 

# another best solution

def best_div(n):
    for i in range(1, int(sqrt(n))+1):
        if number % i == 0:
            result.append(i)
            if number // i != i:
                result.append(number//i)
    result.sort()
    print(result)

if __name__ == "__main__":
    number = 36
    result = []
    best_div(number)

