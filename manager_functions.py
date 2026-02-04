import csv

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
    for line in file_content:
        if username == line[0] and password == line[1]:
            return True
    return False


