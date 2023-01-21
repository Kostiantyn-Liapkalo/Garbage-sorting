import os
import sys
# from pathlib import Path



# for currentpath, folders, files in os.walk('.'):
#     print(currentpath, folders, files)


# path1 = os.getcwd()
# print(path1)



dir_name = '/home/koss/Motlox'
# Get list of all files in a given directory sorted by name
list_of_files = sorted(filter(lambda x: os.path.isfile(os.path.join(dir_name, x)), os.listdir(dir_name)))
for file_name in list_of_files:
    print(file_name)



# suf_files = path.split(".")[-1]
# print(suf_files)
# print(os.listdir(path))


# path = '/home/koss/Motlox'
# def files_bypass(path,level=1):
#     print('Level=',level,'Content:',os.listdir(path))
#     for i in os.listdir(path):
#         if os.path.isdir(path+'//'+i):
#             print('Going down',path+'//'+i)
#             files_bypass(path+'//'+i.level+1)
#             print('We return to',path)


# files_bypass(path)



# # for currentpath, folders, files in os.walk('.'):
# #     print(currentpath, folders, files)


 
# # for currentpath, folders, files in os.walk('.'):
# #     for file in files:
# #         print(os.path.join(currentpath, file))   




