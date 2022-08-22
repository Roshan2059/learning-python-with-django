# # WAP to add list values in dictionary:
# d = {"name":[], "age":[], "address":[]}
# n = int(input("Enter n = "))
# for i in range(n):
#     name = input("Enter name = ")
#     age = input("Enter age = ")
#     address = input("Enter address = ")
#     d["name"].append(name)
#     d["age"].append(age)
#     d["address"].append(address)
# print(d)

# d = {"a": "Apple", "b": "Ball", "c": "Cat"}
# print(d.values())

# WAP to add some keys and values in dictionary:
# d = {"a": "Apple", "b": "Ball", "c": "Cat"}
# n = int(input("Enter n = "))
# for i in range(n):
#     key = input("Enter the key = ")
#     value = input("Enter the value = ")
#     d[key] = value
# print(d)
# print(d.keys())
# print(d.values())
# print(d.items())

# write a program to get radius of circle as input and print the given radius and area in dictionary.
# d = {}
# n = int(input("Enter n = "))
# for i in range(n):
#     r = int(input("Enter the radius = "))
#     area = 3.14 * r * r
#     d[r] = area
# print(d)

# write a program to get radius of circle as input and print the area and perimeter in the list as values and given radius as key.
d = {"areas":[]}
n = int(input("Enter the n = "))
for i in range(n):
    r = int(input("Enter the radius:"))
    area = 3.14 * r * r
    d["areas"].append(area)
print(d)