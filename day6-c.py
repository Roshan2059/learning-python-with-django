# day6

i = 1
while i < 11:
  print(i)
  i += 1

s = 0
i = 0
n = int(input("Enter n = \n"))
while i < n:
    name = input("enter name:\n")
    phone = input("enter phone:\n")
    data = name + " " + phone + "\n"
    s = s + data
    i = i + 1
print(s)

n = int(input("enter n = \n"))
i = 1
fact = 1
while i <= n:
  fact = fact * i
  i = i + 1
print(fact)

a = "python"
print(a[1])

i = 0
a = "python"
l = len(a)
while i < l:
  print(a[i])
  i = i+1

i = 0
a = "Hello world"
l = len(a)
while i<l:
  if a[i] != ' ':
    print(a[i],end = "")
  i += 1

i = 0
a = "Hello world"
l = len(a)
while i<l:
  if a[i] == ' ':
    break
  print(a[i],end = "")
  i += 1

i = 0
a = "Hello world"
l = len(a)
while i < l:
    if a[i] == ' ':
        i = i + 1
        continue
    print(a[i], end="")
    i += 1