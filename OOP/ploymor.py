# method overriding : same method same parameter (child has parent one will be overrided)
# method overloading : 2 method with the same name but different implementation on the basis of input

class Shape:

    # def area(self,radius):
    #     return 3.14 * radius * radius
    
    # def area(self,l,b):
    #     return l * b
    # The above piece of code does not work in python function overloading but in other languages it work 
    # however the same can be achieved through a single function how?

    def area(self,a,b=0):
        if b == 0:
            return 3.14 * a * a
        else:
            return a * b

class XYZ:

    def abc(self):
        print("parent method")

class ABC(XYZ):

    def abc(self):
        print("child method")

if __name__ == "__main__":
    obj =ABC()
    obj.abc