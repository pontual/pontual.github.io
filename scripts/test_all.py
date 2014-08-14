import os
import glob

# Run compilecodigos.py first

SITE_DIR = "c:/Users/Heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/codigos/"

FOTOS_DIR = "c:/Users/Heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/fotos/"

SITE_CODIGOS = "c:/Users/Heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/codigos/codigos.txt"

names_file = "c:/Users/Heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/product_names.txt"
                  
dimen_file = "c:/Users/Heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/product_dimen.txt"


os.chdir(FOTOS_DIR)

codigos = set()

with open(SITE_CODIGOS) as codigos_file:
    for line in codigos_file:
        codigos.add(line.strip())

missing_fotos = 0

for codigo in codigos:
    # check fotos
    if os.path.isfile("full_" + codigo + ".jpg") and os.path.isfile("thumb_" + codigo + ".jpg") and os.path.isfile("dimen_" + codigo + ".jpg"):
        pass
    else:
        print("Missing foto: " + codigo)
        missing_fotos += 1

print("Missing fotos: " + str(missing_fotos))

names_codigos = set()
with open(names_file) as NAMES:
    for line in NAMES:
        names_codigos.add(line.split(";")[0])
print("Missing names: " + str(list(codigos.difference(names_codigos))))

dimen_codigos = set()
with open(dimen_file) as DIMEN:
    for line in DIMEN:
        dimen_codigos.add(line.split(";")[0])
print("Missing dimen: " + str(list(codigos.difference(dimen_codigos))))
