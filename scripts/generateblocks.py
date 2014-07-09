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

    index_html = open("index.html", "w")

    print(generate_index("""

    <center>
    <h1>
    Bem-vindos ao nosso site!
    </h1>

    <div class="carousel_container">
    
      <div class="carousel">
        <div class="carousel_item"><a href="pr_chaveiros.html"><img src="carousel/placeholder_chaveiros.png"></a></div>
        <div class="carousel_item"><a href="pr_canecas.html"><img src="carousel/placeholder_canecas.png"></a></div>
        <div class="carousel_item"><a href="pr_squeezes.html"><img src="carousel/placeholder_squeezes.png"></a></div>
      </div>

    </div>
    </center>
    
    """), file=index_html)
    index_html.close()

    mapa_html = open("mapa.html", "w")

    print(generate_custom("""
    <div class="map_block">
    <br>
    <!-- MAPA -->
    <h2>
    <a href="https://www.google.com.br/maps/place/R.+Antonio+de+Andrade,+109+-+Pari/" target="_blank">Direções</a>
    </h2>
    <div class="map_address">

    Rua Antônio de Andrade, 109<br>
    Sao Paulo, SP, CEP ?????-??? XXXX<br>

    <br>
    Tels. (11) 3228-1113 / 3227-4026 / 3313-7704
    </div>
    <br>
    <a href="https://www.google.com.br/maps/place/R.+Antonio+de+Andrade,+109+-+Pari/" target="_blank">
    <img src="img/mapa_static.png">
    </a>
    </div>
    """), file=mapa_html)
    mapa_html.close()
        
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
                    format(codigo, product_db.get(codigo, "")))
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

site_header = """
<html>
  <head>
	<meta charset="utf-8">
	<title>Pontual Exportação e Importação</title>
	<link rel="stylesheet" href="css/blueimp-gallery.min.css">
	<link rel="stylesheet" href="produtos/css/produtos.css">
	<link rel="stylesheet" href="css/main.css" type="text/css">
	<link rel="stylesheet" href="css/slick.css" type="text/css">
<!-- Site built by Heitor Chang -->
  </head>
  <body>
	<div class="site_header">
<a name="top">&nbsp;</a>
	  <a href="index.html">
		<div class="site_logo">
		  <img src="img/logo_transp.png" style="vertical-align: top;">
		</div>
</a>
		<div class="site_banner">
<a href="index.html">
<span class="banner_company_name">
PONTUAL EXPORTAÇÃO E IMPORTAÇÃO
</span><br>
<i>Brindes e Presentes Promocionais</i><br>
</a>
<span class="telefones">
(11) 3228-1113 / 3227-4026 / 3313-7704<br>
<a href="mailto:heitorpontual@gmail.com">contato@pontualexportacao.com.br</a>
</span>
<br>
		</div>
	  <div class="site_address">
<a href="mapa.html">
Rua Antônio de Andrade, 109<br>
Canindé<br>
Sao Paulo, SP, CEP ?????-??? XXXX<br>
<u><b>Como chegar</b></u>
</a>
	  </div>
	</div>
"""

site_footer = """
<div class="back_to_top">
<a href="#top">
Voltar ao topo <img src="img/uparrow.png" style="vertical-align:top;">
</a>
</div>
"""

def generate_category_page(category_id):
    # find category's full name
    category_name = ""
    categories_file = open("c:/Users/heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/codigos/categories.txt")
    for line in categories_file:
        if not line[0] == "#":
            category_data = line.split(";")
            if category_id == category_data[0]:
                category_name = category_data[1].strip()
    categories_file.close()
    output = site_header + """
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
    <br>
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
	<script type="text/javascript" src="js/jquery.min.js"></script>
	<script type="text/javascript" src="js/bootstrap.min.js"></script>
	<script type="text/javascript" src="js/blueimp-gallery.min.js"></script>
	<script type="text/javascript" src="js/setup_blueimp.js"></script>
    {4}
    </body>
</html>""".format(generate_sidebar(), category_name, generate_gallery(category_id), category_id, site_footer)
    return output


def generate_custom(content):
    output = site_header + """
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
    <!--
		  <span class="category_name">INDEX</span>
    -->
{1}
	  </div>
	</div>

    {2}

	<!-- http://jsfiddle.net/9Wg3T/3/ -->
	<script type="text/javascript" src="js/jquery.min.js"></script>
	<script type="text/javascript" src="js/bootstrap.min.js"></script>
    </body>
</html>""".format(generate_sidebar(), content, site_footer)
    return output

def generate_index(content):
    output = site_header + """
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
    <!--
		  <span class="category_name">INDEX</span>
    -->
{1}
	  </div>
	</div>

    {2}

	<!-- http://jsfiddle.net/9Wg3T/3/ -->
	<script type="text/javascript" src="js/jquery.min.js"></script>
	<script type="text/javascript" src="js/bootstrap.min.js"></script>
    <script type="text/javascript" src="js/slick.min.js"></script>
    <script type="text/javascript" src="js/setup_slick.js"></script>
    </body>
</html>""".format(generate_sidebar(), content, site_footer)
    return output

    
def generate_category_page_printable(category_id):
    # find category's full name
    category_name = ""
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
	<script type="text/javascript" src="js/jquery.min.js"></script>
	<script type="text/javascript" src="js/bootstrap.min.js"></script>
	<script type="text/javascript" src="js/blueimp-gallery.min.js"></script>
	<script type="text/javascript" src="js/setup_blueimp.js"></script>    
    </body>
</html>""".format(generate_sidebar(), category_name, generate_gallery(category_id))
    return output
