# dictionary of my items
items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
# inp = input("items")
# for i in items:
#     if inp == i:
#         print(items[i])

#  total variable
total = 0

# while my logic is true
while True:
    #  try this
    try:
        # store my input in to item
        item = input("Item:")
        # iterate in to my dictionary
        for it in items:
            # if item lowercase is equal to my dictionary key
            if item.casefold() == it.casefold():
                # put the price of the item in to my total
                total = total + items[it]
        # when ever I put input print my Total with 2 decimal point
        print(f"${total:.2f}")
    # cach error when i click ctrl + d
    except EOFError:
        # print new line
        print()
        # break my code
        break
