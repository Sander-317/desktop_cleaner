import os 
import shutil

desktop_path = "/Users/sander/Desktop"

desktop_files = os.listdir(desktop_path)

def get_screenshots(search_term, dir_name):
    new_dir_path = os.path.join(desktop_path,dir_name)
    os.makedirs(new_dir_path, exist_ok="True")
    new_list = []
    for file in desktop_files:
        if search_term  in file:
            new_list.append(file)

    new_folder_path = os.path.join(desktop_path, dir_name)
    print("new folder",new_folder_path)

    os.chdir(desktop_path)
    for i in new_list:
        # print("working dir",os.getcwd())
        file = os.path.join(os.path.dirname(os.path.abspath(i)), i) 
        # print("file",file)
        shutil.move(file, new_folder_path)
    

get_screenshots("Screenshot" , "screenshots")
