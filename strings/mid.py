# length of the string

def custom_len(input_str):
    count = 0
    if type(input_str) == str:
        for char in input_str:
            count +=1
    else:
        return "invalid type"
    return count

if __name__ == "__main__":
    var_a = 2
    print(custom_len(var_a))

