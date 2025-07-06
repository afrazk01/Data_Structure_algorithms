# check if the number is palindrome reverse and original are same 
# extract the last digit multiply it by 10 1221 , 1 * 10 = 10 , then take division 112 remains , then take the  last and add it with 1
number = 1221
reverse = 0
n = number
def palind_check(n):
    while n > 0:
        last = n % 10 
        reverse = reverse * 10 + last
        n = n // 10 

    if reverse == number:
        return True
    else:
        return False
