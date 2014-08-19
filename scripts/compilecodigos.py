import os

os.chdir("c:/Users/Heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/codigos/")

codigos_set = set()

categories = open("categories.txt")

for line in categories:
    if not line[0] == "#":
        line_components = line.split(";")
        with open(line_components[0] + ".txt") as category:
            for codigo in category:
                codigos_set.add(codigo)

categories.close()

codigos_file = open("codigos.txt", "w")

codigos = sorted(list(codigos_set))

for codigo in codigos:
    print(codigo, end='', file=codigos_file)

codigos_file.close()
    
