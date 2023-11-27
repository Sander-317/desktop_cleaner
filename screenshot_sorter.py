import os 
import shutil
import datetime

to_sort_path = "/Users/sander/Desktop/screenshots"

to_sort_files = os.listdir(to_sort_path)

# [print(i[10:21]) for i in to_sort_files]
os.chdir(to_sort_path)
for i in to_sort_files:
    print("working dir",os.getcwd())
    raw_date = i[10:21].split("-")
    date = datetime.date(int(raw_date[0]), int(raw_date[1]), int(raw_date[2]))
    new_path = os.path.join(to_sort_path,str(date.year),date.strftime("%B"))
    print(new_path)
    os.makedirs(new_path, exist_ok="True")
    file = os.path.join(os.path.dirname(os.path.abspath(i)), i)
    print(file)
    shutil.move(file, new_path)

    
    
    # print(date.strftime("%A %dth of %B %Y "))
    # print(date.strftime("%B"))
    # print(type(date.strftime("%B")))
    # print(date.year)
   