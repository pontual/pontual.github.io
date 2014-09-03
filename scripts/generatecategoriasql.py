BASE_DIR = "c:/Users/heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/"

categories = {}

categories_file = open(BASE_DIR + "codigos/categories.txt")

for line in categories_file:
    if not line[0] == "#":
        category_data = line.split(";")
        categories[category_data[0]] = category_data[1]
        
categories_file.close()

for category in categories:
    print("INSERT INTO `categoria` (`nome`, `lista`) VALUES");
    print("('" + categories[category].strip() + "', '", end="");

    with open(BASE_DIR + "codigos/" + category + ".txt") as lista_file:
        for line in lista_file:
            if not line[0] == "#":
                print(line.strip(), end=r'\r\n');
    print("');");
