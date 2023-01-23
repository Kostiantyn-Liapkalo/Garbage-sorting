import os
import shutil
import re


path = input("Enter your path: ")
folder_name = ['images', 'videos', 'documents',
               'music', 'archives', 'unknown']
for folder in folder_name:
    print(os.path.join(path, folder))
    if not os.path.exists(os.path.join(path, folder)):
        os.makedirs(os.path.join(path, folder))

MUSIC = "music"
ARCHIVES = "archives"
IMAGE = "image"
VIDEO = "video"
DOCUMENTS = "documents"
UNKNOWN = "unknown"


extensions = {
    "ogg": MUSIC,
    "wav": MUSIC,
    "amr": MUSIC,
    "mp3": MUSIC,
    "zip": ARCHIVES,
    "tar": ARCHIVES,
    "gz": ARCHIVES,
    "png": IMAGE,
    "jpeg": IMAGE,
    "svg": IMAGE,
    "jpg": IMAGE,
    "mov": VIDEO,
    "avi": VIDEO,
    "mkv": VIDEO,
    "mp4": VIDEO,
    "doc": DOCUMENTS,
    "gnp": DOCUMENTS,
    "pptx": DOCUMENTS,
    "xlsx": DOCUMENTS,
    "txt": DOCUMENTS,
    "docx": DOCUMENTS,
    "pdf": DOCUMENTS
}

            
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r",
               "s", "t", "u", "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def normalize(file_name):
    m = re.match(r"^(.+)\.([\w\d]{2,4})$", file_name)
    file_name = m.group(1)
    extension = m.group(2)
    

    translated_name = ""

    for let in file_name:
        if TRANS.get(ord(let)):
            translated_name += TRANS[ord(let)]
        else:
            translated_name += let
    translated_name = re.sub(r"[^\w\d]", "_", translated_name)
    return f"{translated_name}.{extension}"

    
            
 
files = os.listdir(path)
print(files)
for file_item in files:
    if not os.path.isdir(file_item):
        extension = re.match(r".+\.([\w\d]{2,4})$", file_item)
        if extension:
            target_path = extensions.get(extension.group(1), UNKNOWN)
            shutil.move(os.path.join(path, file_item), os.path.join(path, f"{target_path}/{normalize(file_item)}"))       
            

# /home/koss/test
