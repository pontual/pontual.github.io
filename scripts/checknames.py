BASE_DIR = "c:/Users/heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/"

codigos = set()
names = set()

with open(BASE_DIR + "codigos/codigos.txt") as f:
    for line in f:
        codigos.add(line.strip())

with open(BASE_DIR + "product_names.txt") as f:
    for line in f:
        values = line.split(";");
        names.add(values[0])

print(names.difference(codigos))
