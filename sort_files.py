import os
import glob
import shutil


extensions = {
    "ogg": "music",
    "wav": "music",
    "amr": "music",
    "mp3": "music",
    "zip": "archives",
    "tar": "archives",
    "gz": "archives",
    "png": "image",
    "jpeg": "image",
    "svg": "image",
    "jpg": "image",
    "mov": "video",
    "avi": "video",
    "mkv": "video",
    "mp4": "video",
    "doc": "documents",
    "gnp": "documents",
    "pptx": "documents",
    "xlsx": "documents",
    "txt": "documents",
    "docx": "documents",
    "png": "image"
}

path = "/home/koss/Motlox"


for extension, folder_name in extensions.items():
    files = glob.glob(os.path.join(path, f"*.{extension}"))
    print(f"[*] Найдено {len(files)} файлов с расширением {extension}.")
    if not os.path.isdir(os.path.join(path, folder_name)) and files:
        os.mkdir(os.path.join(path, folder_name))
        print(f"[+] Создана папка {folder_name}.")
        
    for file in files:
        basename = os.path.basename(file)
        dst = os.path.join(path, folder_name, basename)
        print(f"[*] Перенесен файл {file} в {dst}")
        shutil.move(file, dst)
        
        




# ./music[] ['file2.ogg', 'file3.wav', 'file4.amr', 'file1.mp3']
# ./archives[] ['file1.zip', 'file3.tar', 'file2.gz']
# ./image[] ['file2.png', 'file1.jpeg', 'file4.svg', 'file3.jpg']
# ./video[] ['file3.mov', 'file1.avi', 'file4.mkv', 'file2.mp4']
# ./documents[] ['file1.doc', 'file4.pdf', 'file6.pptx', 'file5.xlsx', 'file3.txt', 'file2.docx']
# ./unknown [] ['file4.gvc', 'file2.gnp', 'file1.gepj', 'file3.gpj']
