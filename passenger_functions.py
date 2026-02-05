import json
import csv
import manager_functions
import random
import string

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

# "הדפסת כרטיס לנוסע"
def Card_printing(final_price,selected_destinations):
    print("destination country",selected_destinations[0])
    print("origin country",selected_destinations[1])
    print("final price",final_price)
    print("ID: ", "".join(random.choices(string.ascii_uppercase + string.digits, k=8)))

# פונקצייה שמחזירה סכום בסיס של כרטיס
def base_ticket_price(code1,code2):
    with open("airport_entry_fee.csv","r") as f:
        csv_reader = csv.reader(f)
        all_data = list(csv_reader)
        base_price = 0
        for line in all_data:
            if line[0] == code1:
                base_price += int(line[5])
            elif line[0] == code2:
                base_price += int(line[5])
        return base_price / 400 

# פונקצייה שמחזירה סכום של טווח יבשות של כרטיס
def continents_ticket_priec(code1,code2):
    origin_continent = ""
    destination_contient = ""
    price = 0
    with open("airport_entry_fee.csv","r")  as f:
        csv_reader = csv.reader(f)
        all_data_airports = list(csv_reader)
        for line in all_data_airports:
            if line[0] == code1:
                origin_continent  += line[4]
            elif line[0] == code2:
                destination_contient += line[4]
    with open("continents_pricing.csv","r")  as f:
            csv_reader = csv.reader(f)
            all_data_contients = list(csv_reader)
            for line in all_data_contients:
                if line[0] == origin_continent and line[1] == destination_contient:
                    price += int(line[2]) 
    return price / 400

def Show_Available():
    with open("available_lines.json", "r") as file:
        data = json.load(file)
        routes_list = []
        print("Available Flight Routes:")
        
        
        for i, line in enumerate(data["available_lines"], start=1):
            origin = line["origin_airport"]
            destination = line["destination_airport"]
            
            
            routes_list.append([origin, destination])
            
       
            print(f"[{i}] {origin} -> {destination}")
            
        return routes_list

def wants_ticket():
    while True:
        response = input("Do you want a flight ticket? (yes/no): ").strip().lower()
        if response == "yes":
            return True
        elif response == "no":
            return False
        else:
            print("Please answer with 'yes' or 'no'.")

def Final_ticket_price(result1, result2):
    return result1 + result2

