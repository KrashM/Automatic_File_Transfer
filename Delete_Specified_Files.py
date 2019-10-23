import os
import shutil

files_to_seek = input()
while True:
    files = os.listdir()
    for file in files:
        if files_to_seek in file:
            os.unlink(os.path.join(os.getcwd(), file))
    print("Do you want to delete anything else?(y:n)")
    yes_no = input()
    if yes_no == 'n':
        break
    files_to_seek = input()
