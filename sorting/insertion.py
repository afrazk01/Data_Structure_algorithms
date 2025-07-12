num = [1,5,6,7,4,3,2,9,8]
n = len(num)
for i in range(1,n):
    an = num[i]
    j = i - 1
    print("this is J",j,"and this is number j",num[j],"and this is key",an)
    while j>=0 and num[j] > an:
        num[j+1] = num[j]
        j -= 1
    num[j+1] = an
print(num)