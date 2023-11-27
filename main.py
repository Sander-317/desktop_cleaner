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
        # print(i)
        # print(f"{os.path.dirname(os.path.abspath(i))}/{i}")
        print("working dir",os.getcwd())
        file = os.path.join(os.path.dirname(os.path.abspath(i)), i) 
        print("file",file)
        
        shutil.move(file, new_folder_path)
        # print(file)
    # [print(i) for i in new_list]
    # return new_list

get_screenshots("Screenshot" , "screenshots")
# [print(i) for i in get_screenshots("testfile")]
# def move_screenshots():
    # screenshots = get_screenshots("testfile","testfiles")
    # for i in screenshots:
    #     print(i)
    #     print(os.path.dirname(os.path.abspath(i)))
    
    # print(screenshots)
    # [print(i) for i in screenshots]

# move_screenshots()