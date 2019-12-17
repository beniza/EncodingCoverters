import os
import re
import unicodedata

kuvi_folder = "C:\My Paratext 8 Projects\KUVI"

bible_files = [fn for fn in os.listdir(kuvi_folder) if re.match(r'[0-9]+.*\.SFM', fn)]

# bible_text = [book for book in os.path.join(kuvi_folder, bible_files)]
bible_text = ""

for book in bible_files:
    f = open(os.path.join(kuvi_folder, book), 'r', encoding="utf-8")
    bible_text += f.read()

#bible_text = re.sub("\\\\[A-Za-z0-9]*?\\\\s", "", bible_text)
bible_text = re.sub("\\\\id .*\n", "", bible_text)
bible_text = re.sub("\\\\[A-Za-z0-9]*?\s", "", bible_text)
bible_text = re.sub("[A-Za-z0-9]", "", bible_text)
bible_text = re.sub("\n", "", bible_text)

char_inventory = {}

for char in bible_text:
    try:
        char_inventory[char] += 1
    except:
        char_inventory[char] = 1
o = open("kuvi.tab", mode='w', encoding='utf-8')
for key, value in char_inventory.items():
    try:
        o.write(key + "\t" + unicodedata.name(key) +  "\t" + hex(ord(key)) + "\n")
    except:
        o.write(key + "\t" + "Unknown" +  "\t" + unicodedata.decimal(key)  + "\n")
o.close()

o = open("kuvi.txt", mode='w', encoding='utf-8')
o.write(bible_text)
o.close()
