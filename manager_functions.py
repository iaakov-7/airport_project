import csv
import json

def Return_file_credentials_in_list(name_file):
    with open(name_file, 'r',encoding = "utf-8") as file:
        reader = csv.reader(file)
        all_data = list(reader)
    return all_data            

def num_budget():
    with open("budget.txt","r") as f:
        num = f.read()
    return num

def is_admin_verification(username,password,file_content):
    for i, line in enumerate(file_content):
        if i != 0:
          if username == line[0] and password == line[1]:
            return True
    return False


def add_flight_line():
    while True:
        with open("airport_entry_fee.csv", 'r',encoding = "utf-8") as file:
            reader = csv.reader(file)
            all_data = list(reader)

            code1 = input("Enter the first code: ")
            code2 = input("Enter the second code: ")

            tast_code1 = False
            tast_code2 = False
            cost_code1 = 0
            cost_code2 = 0

            for i, line in enumerate(all_data):
                if i != 0:
                    if line[0] == code1:
                        tast_code1 = True
                        cost_code1 = int(line[5])
                    elif line[0] == code2:
                        tast_code2 = True
                        cost_code2 = int(line[5])

            if tast_code1 == False or tast_code2 == False:
                print("Airports not supported, please try again.")
                continue
            if tast_code1 == True and tast_code2 == True:

                final_price = cost_code1 + cost_code2
                Current_balance = int(num_budget())
                if Current_balance < final_price:
                    print("Not enough money in the budget")
                    break
                else:
                    # "עדכון היתרה"
                    Current_balance -= final_price
                    with open("budget.txt", "w") as f:
                        f.write(str(Current_balance))
                    # "החזרת קודי שדות התעופה כמילון"   
                    new_airports_dict = {"origin_airport":code1, "destination_airport":code2}
                    return new_airports_dict

def add_new_line_to_json(new_line):
    with open("available_lines.json","r") as f:
       data =  json.load(f) 
       data["available_lines"].append(new_line)
    with open("available_lines.json","w") as f:
        json.dump(data,f)  
      



