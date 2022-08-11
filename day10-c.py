# day10

# list = "sita gita nita babita sita  ranjita namita sunita sangita anita asmita anjita".casefold()
# search = input("Enter the value to search:\n")
# if search in list:
#     print(f"The word {search} is found {list.count(search)} times")
# else:
#     print("The word you searched for is not here")

# Python collection:
# list
# tuple
# dictionary
# set

# list:
# -Multiple value
# -Indexed
# -Ordered
# -Mutable

# a = ["apple", "ball","cat","dog"]
# print(a)
# b = [1,2,3,4,5]
# print(b)

# a = ["apple","ball", "cat", "dog"]
# print(a[0:4])
# print(a[0:4:3])


# a = ["apple", "ball", "cat"]
# b = ["hello", 'world']
# print(a+b)
# print(b+a)

#different functions in python list
# a = []
# n = int(input("Enter the value of n:"))
# for i in range(n):
#   x = int(input("Enter x = "))
#   a = a + [x]
# print(a)
# print("The max value is: ", max(a))
# print("The smallest value is: ", min(a))
# print("The sum value is: ",sum(a))
# print("The average is:", sum(a)/n)
# a.sort()
# print(a)
# a.reverse()
# print(a)

a = ["Ram", "Ramesh", "shyam", "hari", "sheetal"]
if "ram" in a:
  print("Yes! it is in the list")
else:
  print("No! it is not in the list")

#WAP to make search case insensitive