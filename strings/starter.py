# return the length of the string provided as input without using built in len()

def length():
    count = 0
    string = input("enter the string: ")
    for i in string:
        count +=1

    return count

# Extract the user name from the email given as input username@gmail.com

def user_name():
    email = input("Please enter an email: ")
    user,other = email.split('@')
    print('this is user',user,"this is other part",other)

# count the frequency of a word in a string 
def freq_char():
    string = input("Enter the String: ")
    char = input("Enter the char for count: ")
    count = 0
    for i in string:
        if i.upper() == char.upper():
            count +=1
    print(f"{char} is {count} times in the string")
    return count

# write a program which can remove a specific character from a string

def remove_it():
    string = input("Enter the String: ")
    char = input("Enter the char to remove")
    new_str = ''
    for i in string:
        if i.upper() == char.upper():
            print("founded")
            continue
        else:
            new_str += i
    print(new_str)

# Check if a string is palindrome or not 

def check_palind():
    string = input("Enter a string:  ")
    is_palindrome = True
    for i in range(0,len(string)//2):
        if string[i] != string[len(string)- i - 1 ]:
            is_palindrome = False
    if is_palindrome:
        return "Palindrome"
    else:
        return "Not Palindrome"
if __name__ == "__main__":
    print(check_palind())