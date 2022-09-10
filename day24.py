class Info:                             #parent class
    def __init__(self,add):
        self.add = add
        
class Data(Info):                         #child class
    def __init__(self,name,age,add):
        self.name = name
        self.age = age
        Info.__init__(self,add)
        
    def data(self):
        print(f"Hello I am {self.name}. I am from {self.add}. I am {self.age}")
        
obj = Data('Ram',34,'Kathmandu')
obj.data()

class Add:                             #parent class
    def __init__(self,add):
        self.add = add
        
class Age:
    def __init__(self,age):
        self.age = age
        
class Data(Add,Age):                         #child class
    def __init__(self,name,age,add):
        self.name = name
        Add.__init__(self,add)
        Age.__init__(self,age)
        
    def data(self):
        print(f"Hello I am {self.name}. I am from {self.add}. I am {self.age}")
        
obj = Data('Ram',34,'Kathmandu')
obj.data()

class Add:                             #parent class
    def __init__(self):
        self.add = input("Enter add = ")
        
class Age:
    def __init__(self):
        self.age = int(input("Enter age = "))
        
class Data(Add,Age):                         #child class
    def __init__(self):
        self.name = input("Enter name = ")
        Add.__init__(self)
        Age.__init__(self)
        
    def data(self):
        print(f"Hello I am {self.name}. I am from {self.add}. I am {self.age}")
        
obj = Data()
obj.data()

class A:
    pass
class B(A):
    pass
class C(B):
    pass

obj = C()

class Add:                             #parent class
    def __init__(self,add):
        self.add = add
        
class Age(Add):
    def __init__(self,age,add):
        self.age = age
        Add.__init__(self,add)
        
class Data(Age):                         #child class
    def __init__(self,name,age,add):
        self.name = name
        Age.__init__(self,age,add)
        
    def data(self):
        print(f"Hello I am {self.name}. I am from {self.add}. I am {self.age}")
        
obj = Data('Ram',34,'Kathmandu')
obj.data()