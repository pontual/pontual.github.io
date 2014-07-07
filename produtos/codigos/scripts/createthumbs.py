import os
from os.path import isfile

os.chdir("c:/Users/Heitor/Desktop/fotos sem codigos/")

codigos_file = open("c:/Users/Heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/codigos/codigos.txt")

for line in codigos_file:
    codigo = line.strip() + ".jpg"
    if not isfile("thumb_" + codigo):
        try:
            os.system("convert " + codigo + " -resize 200x thumb_" + codigo)
        except IOError:
            print("Warning: " + codigo + " not converted")

