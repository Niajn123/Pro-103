import os 
import shutil 
from_dir="/Users/niajain/Downloads"
to_dir="/Users/niajain/Desktop"
list_of_files=os.listdir(from_dir)
for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    if extension=="":
        continue
    if extension in [ '.txt', '.doc', '.docx', '.pdf']:
        path1=from_dir + "/" + file_name
        path2=to_dir + "/" + "document_folder"
        path3=to_dir + "/" + "document_folder" + "/" + file_name
        if os.path.exists(path2):
            print("Moving" + file_name)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving" + file_name)
            shutil.move(path1,path3)