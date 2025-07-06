# if modulus of a num is taken with 10 it gives last num
# then divide the number and last one is removed absolute

num = 8990
n = num
result = ''
while n > 0 :
    last_digit = n % 10
    result += str(last_digit)
    n = n // 10

print(result)

