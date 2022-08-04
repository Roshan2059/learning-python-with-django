for i in range(5):
    print(i, "Hello world")

for i in range(1, 5):
    print(i, "hello world")

for i in range(1, 10, 3):
    print(i, "hello world")

n = int(input("Enter n = "))
for i in range(1, 11):
    print(n * i)

n = int(input("Enter n = "))
for i in range(1, 11):
    print(n, "*", i, "=", n * i)

s = 0
n = int(input("ENter n ="))
for i in range(n):
    a = int(input("Enter X ="))
    s = s + a
    print(s)

s = 0
n = int(input("Enter n ="))
for i in range(n):
    a = int(input("Enter X ="))
    s = s + a

print(s)

stradd = ""
n = int(input("Enter number of the words: \n"))
for i in range(n):
  name = input("Enter the words:")
  stradd = stradd + name

print(stradd)

stradd = ""
n = int(input("Enter number of the words: \n"))
for i in range(n):
  name = input("Enter the words:\n")
  phone = input("Enter phone nunber:\n")
  stradd = stradd + name + "" + phone + "\n"

print(stradd)

fac = 1
n = int(input("Enter n = "))
for i in range(1, n+1):
  fac = fac * i

print(fac)