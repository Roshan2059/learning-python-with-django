# day5

total = 0
n = int(input("How many different products did you buy? :"))
for i in range(1, n + 1):
    name = input("Enter the product's name: \n")
    price = int(input("Enter the price: \n"))
    quantity = int(input("Enter the quantity\n"))
    total = total + (price * quantity)
    bill = name + " " + str(price) + " " + str(quantity)
print("particulars" + " " + "price" + " " + "quantity" + " " + "total")
print("Please pay Rs." + str(total) + " in the counter")

a = "python"
for i in a:
  print(i)
# string is a sequence of characters

a = "python"
for i in a:
  print(i, "hello")

a = "hello  world\n"
for i in a:
  if i != " ":
    print(i, end = "")

# end is just a keyword in python
a = "hello  world\n"
print("The letters are:")
for i in a:
  if i != " ":
    print(i, end = ",")

a = "hello  world."
for i in a:
  if i != " " and i !=".":
    print(i, end = "")

# control statement:
# break
# continue
# pass

# break statement:
for i in range(1,10):
  if i == 5:
    break
  print(i)

a = "hello  world."
for i in a:
    if i == " ":
        break
    print(i, end="")

# continue statement:
for i in range(1,5):
    if i == 3:
      continue
    print(i)

a = "hello  world\n"
print("The letters are:")
for i in a:
  if i == " ":
    continue
  print(i, end = "")