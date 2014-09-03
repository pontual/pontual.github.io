BASE_DIR = "c:/Users/heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/"

codigos = {}
dimens = {}

with open(BASE_DIR + "product_names.txt") as f:
    for line in f:
        values = line.split(";");
        codigos[values[0]] = values[1].strip()
        dimens[values[0]] = ""

with open(BASE_DIR + "product_dimen.txt") as f:
    for line in f:
        values = line.split(";");
        dimens[values[0]] = values[1].strip()
        
for codigo in codigos:
    print("INSERT INTO `produto` (`codigo`, `descricao`, `dimensoes`, `preco`) VALUES")
    print("('{0}', '{1}', '{2}', '');".format(codigo, codigos[codigo], dimens[codigo]))
    
