import csv
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
                 
        
            





               
