# given an input integer you have to count the number of integers 

number = 12345

result = 0

n = number

while n > 0:
    count = n % 10
    if count:
        result += 1
    n = n // 10
print(result)