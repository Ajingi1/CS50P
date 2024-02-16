# Items dictionary
items ={
    "Apple": 130,
    "Avocado": 50,
    "Banana": 110,
    "Cantaloupe": 50,
    "Grapefruit": 60,
    "Grapes": 90,
    "Honeydew Melon": 50,
    "Kiwifruit": 90,
    "Lemon": 15,
    "Lime": 20,
    "Nectarine": 60,
    "Orange": 80,
    "Peach": 60,
    "Pear": 100,
    "Pineapple": 50,
    "Plums": 70,
    "Strawberries": 50,
    "Sweet Cherries": 100,
    "Watermelon": 80
}

# user input
item_input = input("Item:")

# iterate each item by key
for each in items:
    # lower(convert each key and input ) the compare them
    if each.lower() == item_input.lower():
        # if item and key are the same then print the
        # value of key
        print(items[each])
