def wants_ticket():
    while True:
        response = input("Do you want a flight ticket? (yes/no): ").strip().lower()
        if response == "yes":
            return True
        elif response == "no":
            return False
        else:
            print("Please answer with 'yes' or 'no'.")