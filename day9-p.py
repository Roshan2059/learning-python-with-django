list = "Roshan hari sita gita ram shyam ram nita babita ranjita namita sunita sangita anita"
search = input("Enter the value to search")

if search.casefold() in list.casefold():
    print(f"The word {search} is found {list.count(search)} times")
else:
    print("The word you searched for is not here")
               