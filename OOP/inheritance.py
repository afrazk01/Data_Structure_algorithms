class Phone:
    def __init__(self,name,price,camera):
        print("inside Phone constructer")
        self.name = name
        self.price = price                          
        self.camera = camera

    def buy(self):
        print("inside phone buy")      

class Smartphone(Phone):
    def __init__(self, name, price, camera,):
        super().__init__(name, price, camera)
    
    def buy(self):
        print("now  i will call parent method via super")
        super().buy()
        print("inside smartphone buy")


if __name__ == "__main__":
    obj = Smartphone('Iphone',"300k","30mx")
    obj.buy()