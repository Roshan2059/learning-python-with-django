# Write a program to create a billing system.
# Take user input for the product's name, price, and quantity.
# Total = price * quantity.
# The output should be in string format.

# indtotal = 0
# total = 0
# n = int(input("How many different products did you buy? :"))
# for i in range(1,n+1):
#  name = input("Enter the product's name: \n")
#  price = int(input("Enter the price: \n"))
#  quantity = int(input("Enter the quantity\n"))
#  indtotal = (price * quantity)
#  print("You bought " + str(quantity) + " " + name + " which is Rs." + str(indtotal))
#  total = total + indtotal
 
# print("Please pay Rs."+str(total)+" in the counter")

# In the normal bill format
indtotal = 0
total = 0
n = int(input("How many different products did you buy? :\n"))
for i in range(1,n+1):
    name = input("Enter the product's name: \n")
    price = int(input("Enter the price: \n"))
    quantity = int(input("Enter the quantity\n"))
    indtotal = indtotal + (price * quantity)
    total = total + indtotal
print("particulars" + "  " + "quantity" + "  " + "rate" + "  total") 
for i in range(1, n+1):
    print(name + "          " + str(quantity) +"       "+ str(price) +"     "+ str(indtotal) + "\n" )
print("Grand total:" + "                 " + str(total))