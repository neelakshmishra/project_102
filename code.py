import os
import shutil

source="D:/Downloads/new"
destination="newFolder"
list_of_files=os.listdir(source)
print(list_of_files)

for i in list_of_files:
    name,ext = os.path.splitext(i)
    if ext=="":
        continue
    if ext in ['.txt', '.pdf', '.doc', '.docx']:
        path1=source+"/"+i
        path2= destination + "/" + "Document_Files"
        path3 = destination + '/' +"Document_Files"+ "/" + i
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
    