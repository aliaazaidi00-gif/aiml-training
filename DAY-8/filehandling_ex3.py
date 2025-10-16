import os

# file_path =r'C:\AIML\DAY-8\ourfiles'
filepath=os.getcwd()
filename=input("Enter file name to create file:\t")
fullpath=os.path.join(filepath,filename)
if(os.path.exists(fullpath)):
    file=open(fullpath,'r')
    content=file.read()
    print('File Content as follows')
    print(content)
    file.close()
else:
    print(f'no such file {filename} exists')
