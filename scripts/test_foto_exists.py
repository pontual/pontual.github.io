import os
import glob

SITE_DIR = "c:/Users/Heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/codigos/"

FOTOS_DIR = "c:/Users/Heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/fotos/"

SITE_CODIGOS = "c:/Users/Heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/codigos/codigos.txt"

os.chdir(FOTOS_DIR)

count = 0
not_found = 0

with open(SITE_CODIGOS) as cat:
    for line in cat:
        codigo = line.strip()
        if os.path.isfile("full_" + codigo + ".jpg") and os.path.isfile("thumb_" + codigo + ".jpg") and os.path.isfile("dimen_" + codigo + ".jpg"):
            print("Found pictures for " + codigo)
            count += 1
        else:
            not_found += 1

print("Total codigos found: " + str(count))
print("Not found: " + str(not_found))
