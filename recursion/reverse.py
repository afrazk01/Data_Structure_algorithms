number = [1,2,3,4,5,6]
left = 0
right = len(number) -1
def reverse_list(N, left, right):
    if left >= right:
        return N
    N[left], N[right] = N[right] , N[left]
    return reverse_list(N, left+1, right-1 )

done = reverse_list(number,left,right)
print("original_list",done)
