# import os
# file_path =r'C:\AIML\DAY-8\ourfiles\sample.txt'

# file=open(file_path,'w')
# content=input("Enter some text to write in file")
# file.write(content)
# file.close()

#---------------------------------------------------------------------------------------
# import os
# file_path =r'C:\AIML\DAY-8\ourfiles'
# filename=input("Enter file name to creeate file: \t")
# fullpath=os.path.join(file_path,filename)
# file=open(fullpath,'w')
# content=input("Enter some text to write in file")
# file.write(content)
# print(f'File {filename} created successfully at {file_path} and content save in the file')
# file.close()

#---------------------------------------------------------------------------------------
# import os
# file_path =r'C:\AIML\DAY-8\ourfiles'
# filepath=os.getcwd()
# filename=input("Enter file name to creeate file: \t")
# fullpath=os.path.join(file_path,filename)
# file=open(fullpath,'w')
# content=input("Enter some text to write in file")
# file.write(content)
# print(f'File {filename} created successfully at {file_path} and content save in the file')
# file.close()

#---------------------------------------------------------------------------------------
import os

file_path =r'C:\AIML\DAY-8\ourfiles'
filepath=os.getcwd()
filename=input("Enter file name to creeate file: \t")
fullpath=os.path.join(file_path,filename)
file=open(fullpath,'w')
content=input("Enter some text to write in file")
file.write(content)
print(f'File {filename} created successfully at {file_path} and content save in the file')
file.close()
