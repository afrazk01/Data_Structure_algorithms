# selecting sort descending order
n = [1,2,4,8,3,9,7,5]

# for i in range(0,len(n)):
#     max_i = i
#     for j in range(i+1,len(n)):
#         if n[max_i] < n[j]:
#             max_i = j
#     n[i], n[max_i] = n[max_i], n[i]

# ascending order 
for i in range(0,len(n)):
    min_i = i
    for j in range(i+1,len(n)):
        if n[min_i] > n[j]:
            min_i = j
    n[i], n[min_i] = n[min_i], n[i]
print(n)