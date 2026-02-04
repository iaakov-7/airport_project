import menu
from files_management import check_file
def Main_operation():
    files = check_file("airport_entry_fee.csv" , "budget.txt" , "available_lines.json",  "credentials.csv")
    if files == False:
     return
    menu.run_menu()  
Main_operation()    