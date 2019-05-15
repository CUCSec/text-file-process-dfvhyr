import os
path=r'C:\Users\25073\Desktop\homework\text-file-process-ProgramLove7\log_files\201811123016.log' 
f=open(path,encoding='UTF-8')
list=f.read()
print(list.count('201811123016,'))