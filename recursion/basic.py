# function calling itself by a condition once reached condition it is completed is recursion two types head and tail
# head recursion (print(hello world four times))
# using global variable not a good approach though

def head_rec():
    global count
    if count == 4:
        return
    print("hello world")
    count += 1
    head_rec()

def tail_rec():
    global count
    if count == 4:
        return
    count +=1
    tail_rec()
    print("Hello World")
if __name__ == "__main__":
    count = 0
    tail_rec()