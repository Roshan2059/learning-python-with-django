# day10

a = "Hello world"
print(a)
print(type(a))

a = "hello"
b = " world"
c = a+b
print(c)

a = "Hello world\n"
print(a * 2)

a = input("Enter the value of a:\n")
b = input("Enter the value of b:\n")
c = a + b
print(c)

a = "hello world"
print(a[1])
print(a[0:5])
print(a[6:11])
print(a[0:])
print(a[::2])
print(a[::-1])
print(a[-1])

# slicing
a = "hello world"
b = a[0:5]
c = a[5:]
print(b)
print(c)

name = "Roshan"
age = 20
add = "Kathmandu"
info = "Hello world I am " + name + ". I am from " + add + " I am " + str(age)
print(info)

# string formatting
name = "Roshan"
age = 20
add = "Kathmandu"
info = f"Hello world I am {name}. I am {age} year old and I am from {add}"
print(info)

a = "Ram shyam hari sita gita nita sangita babita ranjita"
if "sita" in a:
  print("hello")

a = "Ram shyam hari sita gita nita sangita babita ranjita"
search = input("Enter the value to search")
if search in a:
  print("hello")
else:
  print("The value you searched for is not here")

a = "Ram shyam hari sita gita nita sangita babita ranjita"
search = input("Enter the value to search")
if search in a:
  print(f"Is occured {a.count(search)} times")
else:
  print("The value you searched for is not here")

# replace
a = "Ram shyam hari nita gita sita rita"
print(a.replace("hari","laskdsa"))
print(a)

# remove
a = "Ram shyam hari gita sita babita"
print(a.replace("hari", ""))
print(a)