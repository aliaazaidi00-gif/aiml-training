import os

file_path =r'C:\AIML\DAY-8\ourfiles'
filepath=os.getcwd()
filename=input("Enter file name to update file: \t")
fullpath=os.path.join(filepath,filename)
if(os.path.exists(fullpath)):
    file=open(fullpath,'a')
    content=input("Enter text to add in file: \t")
    file.write(content)
    print(f'File {filename} updated')
    file.close()
else:
    print(f'no such file {filename} exists')

#---------------------------------------------------------------------------------------

