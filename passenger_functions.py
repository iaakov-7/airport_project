import manager_functions

def balance_update(final_price):
    Current_balance = int(manager_functions.num_budget())
    Current_balance -= final_price

    with open("budget.txt", "w") as f:
        f.write(str(Current_balance))



def Origin_and_destination_verification():
    while True:
        destination_country = input("Enter destination country: ")
        origin_country = input("Enter origin country: ")
        if destination_country == origin_country:
            print("Destination country cannot be the same as origin country")
        elif destination_country != origin_country:
            List_of_available_destinations = Show_Available()
            for line in List_of_available_destinations:
                if line[0] == destination_country and line[1] == origin_country:
                    selected_destinations = [line[0], line[1]]
                    return selected_destinations
                    break
            else:
                print("Destination country or origin country are not available")
                continue

    
