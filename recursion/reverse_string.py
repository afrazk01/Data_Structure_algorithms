val = "abb1"
reversed_str = ""
# start , step , end

for i in range(len(val)-1,-1,-1):

    reversed_str += val[i]
print(reversed_str)