class Hello:
    pass

# class <class_name>:               #class
#     <operations or methods>        #method
    
# obj = <class_name>()               #object

class Hello:                         #class
    print("Hello World")             #operation

obj = Hello()                        #object

# def hello():
#     pass

class Hello:                         #class
    def hello(self):                  #method
        print("Hello World")             #operation

obj = Hello()
obj.hello()

class Hello:                         #class
    def hello(self):                  #method
        print("Hello World")             #operation

obj = Hello()
obj.hello()

class Hello:                         #class
    @staticmethod
    def hello():                  #method
        print("Hello World")             #operation

obj = Hello()
obj.hello()

class Hello:                         #class
    def hello(self,x,y):                  #method
        a = x*y             #operation
        print(a)
        
l = int(input("Enter l = "))
b = int(input("Enter b = "))
obj = Hello()
obj.hello(l,b)

class Hello:                         #class
    @staticmethod
    def hello(x,y):                  #method
        a = x*y             #operation
        print(a)
        
l = int(input("Enter l = "))
b = int(input("Enter b = "))
obj = Hello()
obj.hello(l,b)

class Area:
    def area(self,l,b):
        a = l*b
        print(a)

class Volume:
    def volume(self,l,b,h):
        v = l*b*h
        print(v)

l = int(input("Enter l = "))
b = int(input("Enter b = "))
h = int(input("Enter h = "))

obj1 = Area()
obj2 = Volume()
obj1.area(l,b)
obj2.volume(l,b,h)

print(print(1))

class Cal:
    def area(self,l,b):
        a = l*b
        print(a)

    def volume(self,l,b,h):
        v = l*b*h
        print(v)

l = int(input("Enter l = "))
b = int(input("Enter b = "))
h = int(input("Enter h = "))

obj = Cal()
obj.area(l,b)
obj.volume(l,b,h)