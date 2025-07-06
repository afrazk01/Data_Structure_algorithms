# if the number that is given and taken square by the length of the number result in the same number 
# then it is armstrong number 153 = 1 root 3 + 5 root 3 + 3 root 3 
# my jugaro method
number = 153
result = 0

n = number
power = len(str(number))
while n > 0:
    last = n % 10
    result += last ** power
    n = n // 10

if result == number:
    print("this is armstrong number")
