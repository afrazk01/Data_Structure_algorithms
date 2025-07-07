# number of elements

numbers = [1,1,1,2,3,4,2,1,9,5,3,4,3,5]

hash_list = [0] * len(numbers)

for i in numbers:
    hash_list[i] += 1
print(hash_list)