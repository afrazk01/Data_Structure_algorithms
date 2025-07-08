n = [1,2,5,4,9,7,6,8]
x = len(n)
print(x)
for i in range(x-2,-1,-1):
    print("this is I",i)
    for j in range(0,i+1):
        print("this is J",j)
        if n[j] > n[j+1]:
            n[j], n[j+1] = n[j+1], n[j]

print(n)