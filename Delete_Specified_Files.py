import os
import shutil

file_extention = input()
while True:
    files = os.listdir()
    for file in files:
        if file_extention in file:
            os.unlink(os.path.join(os.getcwd(), file))
    print("Do you want to delete anything else?(y:n)")
    yes_no = input()
    if yes_no == 'n':
        break
    file_extention = input()
os.unlink(os.path.join(os.getcwd(), "Delete_Specified_Files.py"))
