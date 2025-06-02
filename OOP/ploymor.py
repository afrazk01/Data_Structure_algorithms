# method overriding : same method same parameter (child has parent one will be overrided)
# method overloading : 2 method with the same name but different implementation on the basis of input

class Shape:

    def area(self,radius):
        return 3.14 * radius * radius
    
    def area(self,l,b):
        return l * b
    

class XYZ:

    def abc(self):
        print("parent method")

class ABC(XYZ):

    def abc(self):
        print("child method")

if __name__ == "__main__":
    obj =ABC()
    obj.abc