import os

def check_file(file_name):
   if os.path.exists(file_name):
        return True
   else:
        return False