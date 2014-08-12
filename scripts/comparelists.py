import os
import glob

ZIP_DIR = "c:/Users/Heitor/Desktop/imagens/"

SITE_DIR = "c:/Users/Heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/codigos/"

SITE_CATEGORIES = "c:/Users/Heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/codigos/categories.txt"

os.chdir(ZIP_DIR)
zip_folders = glob.glob("*")

zip_codes = set()
site_codes = set()

# compile codigos from zip files
for zip_folder in zip_folders:
    if os.path.isdir(ZIP_DIR + zip_folder):
        os.chdir(ZIP_DIR + zip_folder)
        for file in glob.glob("*"):
            zip_codes.add(file[:-4])

# compile codigos from site
os.chdir(SITE_DIR)
categories = open(SITE_CATEGORIES)

for line in categories:
    if not line[0] == "#":
        line_components = line.split(";")
        with open(line_components[0] + ".txt") as category:
            for codigo in category:
                site_codes.add(codigo.strip())

categories.close()

print(zip_codes.difference(site_codes))
