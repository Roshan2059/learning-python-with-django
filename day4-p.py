# Write a program to create a billing system.
# Take user input for the product's name, price, and quantity.
# Total = price * quantity.
# The output should be in string format.

total = 0
n = int(input("How many different products did you buy? :"))
for i in range(1,n+1):
 name = input("Enter the product's name: \n")
 price = int(input("Enter the price: \n"))
 quantity = int(input("Enter the quantity\n"))
 total = total + (price * quantity)
print("Please pay Rs."+str(total)+" in the counter")