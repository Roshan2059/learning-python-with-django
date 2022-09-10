# Public members
class Info:
    def __init__(self,name,age,add):
        self.name = name
        self.age = age
        self.add = add
        
obj = Info("Ram",34,'Kathmandu')

print(obj.name)
print(obj.age)
print(obj.add)

# Protected members
class Info:
    def __init__(self,name,age,add):
        self._name = name
        self._age = age
        self._add = add
        
obj = Info("Ram",34,'Kathmandu')

print(obj._name)
print(obj._age)
print(obj._add)

# Private members
class Info:
    def __init__(self,name,age,add):
        self.__name = name
        self.__age = age
        self.__add = add
        
obj = Info("Ram",34,'Kathmandu')

print(obj.__name)
print(obj.__age)
print(obj.__add)

# Private members
class Info:
    def __init__(self,name,age,add):
        self.__name = name
        self.__age = age
        self.__add = add
        
obj = Info("Ram",34,'Kathmandu')

print(obj._Info__name)
print(obj._Info__age)
print(obj._Info__add)

class Info:                             #parent class
    def __init__(self):
        self.name = "Ram"
        self.age= 78
        self.__add = "Kathmandu"
    
        
class Data(Info):                         #child class
    def data(self):
        print(f"Hello I am {self.name}. I am from {self.__add}. I am {self.age}")
        
obj = Data()
obj.data()

class Info:                             #parent class
    def __init__(self):
        self.name = "Ram"
        self.age= 78
        self.__add = "Kathmandu"
    
        
class Data(Info):                         #child class
    def data(self):
        print(f"Hello I am {self.name}. I am from {self._Info__add}. I am {self.age}")
        
obj = Data()
obj.data()

class Info:                             #parent class
    def __init__(self):
        self.name = "Ram"
        self.__age= 78
        self._add = "Kathmandu"
    def my_age(self):
        print(f"Hello my age is {self.__age}")
        
class Data(Info):                         #child class
    def data(self):
        print(f"Hello I am {self.name}. I am from {self._add}.")
        
obj = Data()
obj.data()
obj.my_age()

class Info:                             #parent class
    def __init__(self):
        self.name = "Ram"
        self.__age= 78
        self._add = "Kathmandu"
    def my_age(self):
        print(f"Hello my age is {self.__age}")
        
class Data(Info):                         #child class
    def data(self):
        print(f"Hello I am {self.name}. I am from {self._add}.")
        super().my_age()
        
        
obj = Data()
obj.data()
# obj.my_age()

class Info:                             #parent class
    def __init__(self):
        self.name = "Ram"
        self.__age= 78
        self._add = "Kathmandu"
    def my_age(self):
        return f"Hello my age is {self.__age}"
        
class Data(Info):                         #child class
    def data(self):
        print(f"Hello I am {self.name}. I am from {self._add}. I am {super().my_age()}")
        
        
        
obj = Data()
obj.data()
# obj.my_age()

class Info:                             #parent class
    def __init__(self):
        self.name = "Ram"
        self.__age= 78
        self._add = "Kathmandu"
    def __my_age(self):
        return f"Hello my age is {self.__age}"
        
class Data(Info):                         #child class
    def data(self):
        print(f"Hello I am {self.name}. I am from {self._add}. I am {super().__my_age()}")
        
        
        
obj = Data()
obj.data()
# obj.my_age()