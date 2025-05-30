class User:

    def __init__(self,name,id,address):
        self.name = name
        self.id = id
        self.address = address

    def info(self):
        return f"{self.name}, {self.id} has address {self.address.address()}"
    
    def __str__(self):
        print("first this is called")
        return f"{self.name} {self.id}{self.address}"
    


class Address:

    def __init__(self,city,street,postal_address):
        self.city = city
        self.street = street
        self.postal_address = postal_address

    def address(self):
        print("at last this is called")
        return f" {self.city} , {self.street} , {self.postal_address}"
    
    def __str__(self):
        print("then this is called")
        return self.address()
        

if __name__ == "__main__":
    address_obj = Address("Karachi","Niazi Street",2340)
    obj = User("afraz",0,address_obj)
    print(obj)