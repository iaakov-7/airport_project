import os

def check_file(file_name1 ,file_name2 , file_name3 , file_name4 , file_name5 ):
   if os.path.exists(file_name1) and os.path.exists(file_name2) and os.path.exists(file_name3) and os.path.exists(file_name4) and os.path.exists(file_name5):
        return True
   else:
        return False