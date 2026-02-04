def num_budget():
    with open("budget.txt","r") as f:
        num = f.read()
    return num
print(num_budget())