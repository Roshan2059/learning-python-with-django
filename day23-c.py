class A:
    pass

class B(A):
    pass

obj = B()


class Info:                             #parent class
    def __init__(self):
        self.name = "Ram"
        self.age= 78
        self.add = "Kathmandu"
    
        
class Data(Info):                         #child class
    def data(self):
        print(f"Hello I am {self.name}. I am from {self.add}. I am {self.age}")
        
obj = Data()
obj.data()

class Info:                             #parent class
    def __init__(self,name,age,add):
        self.name = name
        self.age= age
        self.add = add
        
class Data(Info):                         #child class
    def data(self):
        print(f"Hello I am {self.name}. I am from {self.add}. I am {self.age}")
        
obj = Data('Ram',34,'Kathmandu')
obj.data()