def run_menu():
    print("--- Welcome to the Flight Management System ---")
    print("Please choose your login type:")
    print("1. Admin")
    print("2. Passenger")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    print("Redirecting to Admin Portal")
    #מחכה לפונקצית מנהל
elif choice == "2":
    print("Where would you like to fly this time?")
    #מחכה לפונקצית נוסע
else:
    print("please choose 1 or 2 ")
   