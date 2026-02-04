import menu
from files_management import check_file

check_file("airport_entry_fee.csv" , "budget.txt" , "available_lines.json" , "credentials.csv")

menu.run_menu()