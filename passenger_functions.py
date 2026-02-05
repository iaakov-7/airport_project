import manager_functions
# "מקבלת כפרטמר את הסכום של עלות הרכטיס"
def balance_update(final_price):
    Current_balance = int(manager_functions.num_budget())
    # "חישוב היתרה החדשה"
    Current_balance += final_price
    # "עדכון היתרה"
    with open("budget.txt", "w") as f:
        f.write(str(Current_balance))



def Origin_and_destination_verification():
    while True:
        # "בקשת שני קודים של מוצא ויעד"
        destination_country = input("Enter destination country: ")
        origin_country = input("Enter origin country: ")
        # "בדיקה שהקודים אינם זהים"
        if destination_country == origin_country:
            print("Destination country cannot be the same as origin country")
        elif destination_country != origin_country:
            List_of_available_destinations = Show_Available()
            # " בדיקה הקודים קיימים ברשימת הקודים הזמינים"
            for line in List_of_available_destinations:
                if line[0] == destination_country and line[1] == origin_country:
                    # "הכנסת הקודים לרשימה"
                    selected_destinations = [line[0], line[1]]
                    # "החזרת הרשימה"
                    return selected_destinations
                    break
            else:
                print("Destination country or origin country are not available")
                # "חזרה ללולאה"
                continue

    
