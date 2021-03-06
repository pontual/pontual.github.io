import os
from os.path import isfile

os.chdir("c:/Users/Heitor/Desktop/fotos sem codigos/")

# run compilecodigos.py first

DEST_DIR = "c:/Users/Heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/fotos/"

codigos_file = open("c:/Users/Heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/codigos/codigos.txt")

for line in codigos_file:
    codigo = line.strip() + ".jpg"
    if not isfile("full_" + codigo):
        try:
            os.system("convert " + codigo + " -resize 640x " + DEST_DIR + "full_" + codigo)
        except IOError:
            print("Warning: " + codigo + " not converted")

codigos_file.close()
