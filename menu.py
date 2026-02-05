import manager_functions
from  manager_functions import Return_file_credentials_in_list , is_admin_verification
import manager_functions
import passenger_functions
def run_menu():
    print(" ")
    print("--- Welcome to the Flight Management System ---")
    print("        Please choose your login type:")
    print("                  1. Admin")
    print("                  2. Passenger")
    print(" ")

    list_of_users = Return_file_credentials_in_list("credentials.csv")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("Redirecting to Admin Portal")
        user_name = input("Enter your user name: ")
        password = input("Enter a password:")
        if is_admin_verification(user_name , password , list_of_users):
            choice = input("Enter your choice: 1 = Add Flight :")
            if choice == "1":
                Purchasing_ability_test = manager_functions.add_flight_line()
                manager_functions.add_new_line_to_json(Purchasing_ability_test)

        
    elif choice == "2":
        Show_Available = passenger_functions.Show_Available()
        codes = passenger_functions.Origin_and_destination_verification(Show_Available)
        base_ticket_price = passenger_functions.base_ticket_price(codes[0],codes[1])
        continents_ticket_price = passenger_functions.continents_ticket_priec(codes[0],codes[1])
        final_price = passenger_functions.Final_ticket_price(base_ticket_price,continents_ticket_price)
        if passenger_functions.wants_ticket():
            passenger_functions.balance_update(final_price)
            passenger_functions.Card_printing(final_price,codes)
        else:
            print("by by!")
            return

    else:
        print("please choose 1 or 2 ")
   
