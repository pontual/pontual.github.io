import shutil

BASE_DIR = "c:/Users/heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/"

FOTOS_SEM_COD_DIR = "c:/Users/heitor/Desktop/fotos sem codigos/"

FOTOS_FILTERED_DIR = "c:/Users/heitor/Desktop/fotos sem codigos/filtered/"

with open(BASE_DIR + "product_names.txt") as f:
    for line in f:
        values = line.split(";");
        print(FOTOS_SEM_COD_DIR + values[0] + ".jpg")
        shutil.copy(FOTOS_SEM_COD_DIR + values[0] + ".jpg", FOTOS_FILTERED_DIR + values[0] + ".jpg")
