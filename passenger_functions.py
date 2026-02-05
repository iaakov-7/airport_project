import manager_functions

def balance_update(final_price):
    Current_balance = int(manager_functions.num_budget())
    Current_balance -= final_price

    with open("budget.txt", "w") as f:
        f.write(str(Current_balance))


