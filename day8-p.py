def add():
  a = int(input("enter the first number:\n"))
  b = int(input("Enter the second number:\n"))
  result = a + b
  print(result)
  o = input("Do you want to perform the operation again? If yes press y else press any key:\n")
  if (o) == "y" | o == "Y":
    print("Result: ",add())
  else:
      print("Operation terminated")
add()