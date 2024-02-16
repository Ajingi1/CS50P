amount_due = 50
inserted_amount = 0

while inserted_amount < amount_due:
    insert_coin = int(input("Insert Coin:"))
    match insert_coin:
        case 5 | 10 | 25:
            inserted_amount = inserted_amount + insert_coin
        case _:
            inserted_amount = inserted_amount
    if inserted_amount < amount_due:
        print("Amount Due:", amount_due - inserted_amount)
print("Change Owed:", inserted_amount - amount_due)
