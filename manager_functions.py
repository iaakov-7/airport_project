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

def add_new_line_to_json(new_line):
    with open("available_lines.json","r") as f:
       data =  json.load(f) 
       data["available_lines"].append(new_line)
    with open("available_lines.json","w") as f:
        json.dump(data,f)  
      



