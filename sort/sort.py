# import os
# import sys
# # from pathlib import Path



# # for currentpath, folders, files in os.walk('.'):
# #     print(currentpath, folders, files)


# # path1 = os.getcwd()
# # print(path1)



# dir_name = '/home/koss/Motlox'
# # Get list of all files in a given directory sorted by name
# list_of_files = sorted(filter(lambda x: os.path.isfile(os.path.join(dir_name, x)), os.listdir(dir_name)))
# for file_name in list_of_files:
#     print(file_name)



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


# for extension, folder_name in extensions.items():
#     files = glob.glob(os.path.join(path, f"*.{extension}"))
#     print(f"[*] Найдено {len(files)} файлов с расширением {extension}.")
#     if not os.path.isdir(os.path.join(path, folder_name)) and files:
#         os.mkdir(os.path.join(path, folder_name))
#         print(f"[+] Создана папка {folder_name}.")

#     for file_f in files:
#         basename = os.path.basename(file_f)
#         dst = os.path.join(path, folder_name, basename)
#         print(f"[*] Перенесен файл {file_f} в {dst}")
#         shutil.move(file_f, dst)
