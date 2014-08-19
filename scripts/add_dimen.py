import os
import glob


FOTOS_DIR = "c:/Users/Heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/fotos/"

SITE_CODIGOS = "c:/Users/Heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/codigos/codigos.txt"

os.chdir(FOTOS_DIR)

DIMEN_DATA = "c:/Users/Heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/product_dimen.txt"

def add_dimen(codigo, dimen):
    try:
        if len(dimen) > 0:
            dimen_string = "({DIMEN} cm)".format(DIMEN=dimen.replace("x", " x ").replace(".", ","))
        else:
            dimen_string = ""
        #if not os.path.isfile("dimen_" + codigo + ".jpg"):
        if True:
            os.system('convert full_{CODIGO}.jpg -font Arial -pointsize 18 -background White label:"{CODIGO} {DIMEN_STR}" -gravity Center -append dimen_{CODIGO}.jpg'.format(CODIGO=codigo, DIMEN_STR=dimen_string));
        else:
            print("add dimen: skipping existing file " + codigo)
    except IOError:
        print("Error adding dimen");

def add_brand(codigo):
    try:
        #if not os.path.isfile("dimen_" + codigo + ".jpg"):
        if True:
            os.system('convert dimen_{CODIGO}.jpg -font Arial -pointsize 12 -background White -fill Red label:"PONTUAL IMPORT BRINDES" -gravity SouthEast -append dimen_{CODIGO}.jpg'.format(CODIGO=codigo));
        else:
            print("add brand: skipping existing file " + codigo)
    except IOError:
        print("Error adding brand");

def run_convert():
    with open(DIMEN_DATA) as dimen_data:
        for line in dimen_data:
            values = line.split(";")
            add_dimen(values[0], values[1].strip())
            add_brand(values[0])
            print(values[0])

def check_dimen_len():
    with open(DIMEN_DATA) as dimen_data:
        for line in dimen_data:
            values = line.split(";")
            if len(values[1].strip()) < 4:
                print(values[0])
                
