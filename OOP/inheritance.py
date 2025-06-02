class Phone:
    def __init__(self,name,price,camera):
        print("inside Phone constructer")
        self.name = name
        self.price = price                          
        self.camera = camera

    def buy(self):
        print("inside phone buy")      

class Smartphone(Phone):
    
    def buy(self):
        print("inside smartphone buy")


if __name__ == "__main__":
    obj = Smartphone('Iphone',"300k","30mx")
    obj.buy()