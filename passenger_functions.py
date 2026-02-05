
import json

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

