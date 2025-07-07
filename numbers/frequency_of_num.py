# given an string return the frequency of each number in the list
# ok way

def check_f(number):
    fre = dict()
    for i in range(0,len(number)):
        if number[i] in fre:
            fre[number[i]] +=1
        else:
            fre[number[i]] = 1
    print(fre)

# best way
def freq(number):
    f = {}
    for i in range(0, len(number)):
        f[number[i]] = f.get(number[i],0)+1

    print(f)

if __name__ == '__main__':
    number=[1,1,1,1,2,2,2,2,3,4,5]
    check_f(number)