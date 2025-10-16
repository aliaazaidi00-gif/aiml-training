# import os
# import inspect
# print('Current Directory:',os.getcwd())
# print("Login Name:",os.getlogin())

# functions = inspect.getmembers(os, inspect.isbuiltin) 

# print('All functions in os module:\t')
# for n, func in functions:
#     print(n)

#create a folder inside current directory using python

# import os
# cdir=os.getcwd()
# folder_name=input('Enter folder name to create: \t')
# folder_path=os.path.join(cdir,folder_name)
# if(os.path.exists(folder_path)):
#     print('Folder Already Exist')
# else:
#     os.makedirs(folder_path,exist_ok=True)
#     print(f'{folder_name} created at {folder_path}')

# os.rename(folder_name,"renamed_folder")

#rename a folder
#   os.rmdir("renamed_folder")
#write code to rename a folder
#you will take folderName from user
#if it exist, you will ask new name and rename it
import os
cdir=os.getcwd()
old_folder_name=input('enter the existing folder to rename\t:')
if(os.path.exists(old_folder_name)):
    new_folder_name=input("Enter new folder name\t:\t")
    os.rename(old_folder_name,new_folder_name)
    print(f"folder renamed as: ",{new_folder_name})
else:
    print('Folder does not exists')
