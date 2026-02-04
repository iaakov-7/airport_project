from  manager_functions import Return_file_credentials_in_list , is_admin_verification
def run_menu():
    print("--- Welcome to the Flight Management System ---")
    print("Please choose your login type:")
    print("1. Admin")
    print("2. Passenger")

    list_of_users = Return_file_credentials_in_list("credentials.csv")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("Redirecting to Admin Portal")
        user_name = input("Enter your user name")
        password = input("Enter a password")
        is_admin_verification(user_name , password , list_of_users) 
        
    elif choice == "2":
        print("Where would you like to fly this time?")
        #מחכה לפונקצית נוסע
    else:
        print("please choose 1 or 2 ")
   
