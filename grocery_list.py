grocery_list = []

more_items = True
while more_items:
    grocery_item = input("Please enter a grocery item: ")
    grocery_list.append(grocery_item)

    keep_adding_items = (input("Do you want more items? (y or n) ")).lower()
    if keep_adding_items != "y":
        more_items = False

print("Grocery list is: ")
for item in grocery_list:
    print(item)

