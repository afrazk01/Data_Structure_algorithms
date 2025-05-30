class Person:
    def __init__(self,name,age):
        self.name = ''
        self.age = 0
        self.__balance = 0

    def set_balance(self,balance):
        self.__balance = balance

    def get_balance(self):
        balance = self.__balance
        return balance
    
if __name__ == "__main__":
    p = Person("afraz",24)
    print(p.get_balance  )  