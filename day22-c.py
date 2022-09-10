class Cal():
    def __init__(this,l,b,h):
        this.l = l
        this.b = b
        this.h = h
        
    def area(self):
        a = self.l*self.b
        print(a)

    def volume(self):
        v = self.l*self.b*self.h
        print(v)

l = int(input("Enter l = "))
b = int(input("Enter b = "))
h = int(input("Enter h = "))

obj = Cal(l,b,h)
obj.area()
obj.volume()
print(obj.l)
print(obj.b)
print(obj.h)

class Cal():
    def __init__(this,l,b):
        this.l = l
        this.b = b
        
        
    def area(self):
        a = self.l*self.b
        print(a)

    def volume(self,h):
        v = self.l*self.b*h
        print(v)

l = int(input("Enter l = "))
b = int(input("Enter b = "))
h = int(input("Enter h = "))

obj = Cal(l,b)
obj.area()
obj.volume(h)
print(obj.l)
print(obj.b)
print(obj.h)

class Info:
    def __init__(self,name,age,add):
        self.name = name
        self.age = age
        self.add = add
    
    def __str__(self):
        return self.name
    
obj = Info("Ram",34,"Kathmandu")
print(obj)
print(obj.__str__())
print(str(obj))

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

        
p1 = Point(2,3)
p2 = Point(-1,2)

p1 + p2

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x},{self.y}"

    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)

p1 = Point(2,3)
p2 = Point(-1,2)
print(p1 + p2)

class Point:
    def __init__(self, x = 0):
        self.x = x
        print("This is init method",self.x)

    def __str__(self):
        print("This is str method",self.x)
        return f"{self.x}"

    def __add__(self,other):
        x = self.x + other.x
        print("This is add method",x)
        return Point(x)

p1 = Point(2000)
p2 = Point(3000)
p3 = Point(1500)
print(p1+p2+p3)