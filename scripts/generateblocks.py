import os

def generate_site():
    category_ids = []
    categories_file = open("c:/Users/heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/codigos/categories.txt")
    for line in categories_file:
        if not line[0] == "#":
            category_data = line.split(";")
            category_ids.append(category_data[0])
    categories_file.close()
    os.chdir("c:/Users/heitor/Desktop/emacs-24.3/bin/pontual.github.io/")
    for category in category_ids:
        category_html = open("pr_{0}.html".format(category), "w")
        print(generate_category_page(category), file=category_html)
        category_html.close()
        category_printable_html = open("pr_{0}_impr.html".format(category), "w")
        print(generate_category_page_printable(category),
              file=category_printable_html)
        category_printable_html.close()
        
def generate_sidebar():
    """return a string containing only <li> items"""
    sidebar = []
    categories_file = open("c:/Users/heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/codigos/categories.txt")
    for line in categories_file:
        if not line[0] == "#":
            category_data = line.split(";")
            category_name = category_data[1].strip()
            sidebar.append('<!-- {0} --><li><a href="pr_{1}.html">{0}</a></li>'.
                           format(category_name,
                                  category_data[0]))
    categories_file.close()
    return "\n".join(sorted(sidebar))

def generate_gallery(category_id):
    """return a string containing <li> items"""
    product_db = load_product_names()
    gallery = ""
    codigos_file=open("c:/Users/heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/codigos/{0}.txt".format(category_id))
    for codigo in codigos_file:
        codigo = codigo.strip()
        gallery += ('<li><a href="produtos/fotos/full_{0}.jpg" title="{1} - {0}"><img src="produtos/fotos/thumb_{0}.jpg"><br>{0}</a></li>\n'.
                    format(codigo, product_db.get(codigo, "sem nome")))
    codigos_file.close()
    return gallery

def load_product_names():
    product_name_db = {}
    product_name_file = open('c:/Users/heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/product_names.txt')
    for line in product_name_file:
        codigo, description = line.split(";")
        product_name_db[codigo] = description.strip()
    product_name_file.close()
    return product_name_db

def generate_category_page(category_id):
    # find category's full name
    category_name = "sem nome"
    categories_file = open("c:/Users/heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/codigos/categories.txt")
    for line in categories_file:
        if not line[0] == "#":
            category_data = line.split(";")
            if category_id == category_data[0]:
                category_name = category_data[1].strip()
    categories_file.close()
    output = """
<html>
  <head>
	<meta charset="utf-8">
	<title>Pontual Exportação e Importação</title>
	<link rel="stylesheet" href="css/blueimp-gallery.min.css">
	<link rel="stylesheet" href="produtos/css/produtos.css">
	<link rel="stylesheet" href="css/main.css" type="text/css">
  </head>
  <body>
	<div class="site_header">
	  <a href="index.html">
		<div class="site_logo">
		  <img src="img/logo_transp.png" style="vertical-align: top;">
		</div>
		<div class="site_banner">
		  PONTUAL EXPORTAÇÃO E IMPORTAÇÃO<br>
		  BANNER MESSAGE
		</div>
	  </a>
	  <div class="site_address">
		Rua Antônio de Andrade, 109<br>
		Sao Paulo, SP, CEP ?????-??? XXXX<br>
		(11) 3228-1113 / 3227-4026 / 3313-7704<br>
		<a href="mapa.html"><i>XXXX LINK<u>ver mapa</u></i></a>
	  </div>
	</div>
	<div class="site_body_container">
	  <div class="site_sidebar">
		<ul>
{0}
		</ul>
		<br>
		<div class="site_footer">
		  (C) 2014
		</div>
	  </div>
          <div class="site_content">
        <div style="float:right;"><i><a href="pr_{3}_impr.html">Página para impressão</a></i></div>
    <br>
		<div class="site_gallery">
		  <span class="category_name">{1}</span>
		  <div class="container" id="gallery_container"> 
			<div id="links">
			  <ul class="products">
{2}
			  </ul>
			</div>			
		  </div>
		</div>
	  </div>
	</div>
          <div id="blueimp-gallery" class="blueimp-gallery blueimp-gallery-controls">
		<div class="slides"></div>
		<h3 class="title"></h3>
		<a class="prev">‹</a>	  
		<a class="next">›</a>
		<a class="close">×</a>
		<a class="play-pause"></a>
		<ol class="indicator"></ol>
	  </div>
	<!-- http://jsfiddle.net/9Wg3T/3/ -->
	<script src="js/jquery.min.js"></script>
	<script src="js/bootstrap.min.js"></script>
	<script src="js/blueimp-gallery.min.js"></script>
	<script src="js/setup_blueimp.js"></script>    
    </body>
</html>""".format(generate_sidebar(), category_name, generate_gallery(category_id), category_id)
    return output

def generate_category_page_printable(category_id):
    # find category's full name
    category_name = "sem nome"
    categories_file = open("c:/Users/heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/codigos/categories.txt")
    for line in categories_file:
        if not line[0] == "#":
            category_data = line.split(";")
            if category_id == category_data[0]:
                category_name = category_data[1].strip()
    categories_file.close()
    output = """
<html>
  <head>
	<meta charset="utf-8">
	<title>Pontual Exportação e Importação</title>
	<link rel="stylesheet" href="css/blueimp-gallery.min.css">
	<link rel="stylesheet" href="produtos/css/produtos.css">
	<link rel="stylesheet" href="css/main.css" type="text/css">
  </head>
  <body>
    <a href="index.html">Voltar</a><br>
    <center>PONTUAL EXPORTAÇÃO E IMPORTAÇÃO</center>
<hr>
    <div class="site_content">
		<div class="site_gallery">
		  <span class="category_name">{1}</span>
		  <div class="container" id="gallery_container"> 
			<div id="links">
			  <ul class="products">
{2}
			  </ul>
			</div>			
		  </div>
		</div>
	  </div>
	</div>
          <div id="blueimp-gallery" class="blueimp-gallery blueimp-gallery-controls">
		<div class="slides"></div>
		<h3 class="title"></h3>
		<a class="prev">‹</a>	  
		<a class="next">›</a>
		<a class="close">×</a>
		<a class="play-pause"></a>
		<ol class="indicator"></ol>
	  </div>
	<!-- http://jsfiddle.net/9Wg3T/3/ -->
	<script src="js/jquery.min.js"></script>
	<script src="js/bootstrap.min.js"></script>
	<script src="js/blueimp-gallery.min.js"></script>
	<script src="js/setup_blueimp.js"></script>    
    </body>
</html>""".format(generate_sidebar(), category_name, generate_gallery(category_id))
    return output
