class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__balance = 0

    def __str__(self):
        return str(self.get_balance())

    def set_balance(self, balance):
        self.__balance = balance
    
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age
    
    def get_balance(self):
        return self.__balance

if __name__ == "__main__":
    p = Person("afraz", 24)
    print(p.get_balance()) 
    p.set_balance(100)
    print(p) 
