# import counter from collection
from collections import Counter

# initialize empty list
list_1 = []

# Try this
try:
    # while true
    while True:
        # collect input from user
        item = input("").upper()
        # put the user input to my list
        list_1.append(item)
        list_1.sort()
# Exept EOFError
except EOFError:
    counter_dic = Counter(list_1)
    for item_dic, count_no in counter_dic.items():
        print(f"{count_no} {item_dic}")
