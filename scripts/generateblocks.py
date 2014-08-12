# Copyright 2014 Heitor Chang <heitorchang@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# To build:
# F5 run-python
# Alt-Enter 
# type "generate_site()" into Python shell

# To update:
# Check produtos/codigos/categories.txt
# Open produtos/codigos/{{ CATEGORY_NAME }}.txt
# Update produtos/product_names.txt

# To update photos:
# Run compilecodigos.py
# Run shrinkfoto.py
# Run createthumbs.py

import os

TELEFONES = "(11) 3228-1113 / 3227-4026 / 3313-7704"
# EMAIL = "contato@pontualimportbrindes.com.br"
EMAIL = ""

def generate_site():
    category_ids = []
    categories_file = open("c:/Users/heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/codigos/categories.txt")
    
    for line in categories_file:
        if not line[0] == "#":
            category_data = line.split(";")
            category_ids.append(category_data[0])
    categories_file.close()

    # generate category pages and corresponding printable pages
    os.chdir("c:/Users/heitor/Desktop/emacs-24.3/bin/pontual.github.io/")
    for category in category_ids:
        category_html = open("pr_{category}.html".format(category=category), "w")
        print(generate_category_page(category), file=category_html)
        category_html.close()
        category_printable_html = open("pr_{category}_impr.html".format(category=category), "w")
        print(generate_category_page_printable(category),
              file=category_printable_html)
        category_printable_html.close()


    # generate index
    index_html = open("index.html", "w")
    print(generate_index("""

    <div class="carousel_container">
    
      <div class="carousel">
        <div class="carousel_item"><a href="pr_squeezes.html"><img src="img/showroom/squeeze.jpg"></a></div>
        <div class="carousel_item"><a href="pr_canecas.html"><img src="img/showroom/caneca.jpg"></a></div>
        <div class="carousel_item"><a href="pr_kitchurrasco.html"><img src="img/showroom/kitchurrasco.jpg"></a></div>
      </div>

    </div>
    
    """), file=index_html)
    index_html.close()

    # define mapa content html
    mapa_content = """
       <div class="map_block">

		<!-- MAPA -->
		<h2>
	Direções
		</h2>
		<h3>Localização perto do Estádio do Canindé da Portuguesa</h3>

    <hr>
		<h3>Vindo da Marginal Tietê sentido Ayrton Senna:</h3>
		
		Siga a Marginal até chegar ao Estádio do Canindé<br><br>

		Passando o estádio, vire à direita na quarta rua <b>(Iturama)</b> <br><br>

		Vire à direita na segunda rua <b>(Antônio de Andrade)</b><br><br>


    <hr>
		<h3>Vindo da Marginal Tietê sentido Castelo Branco:</h3>

		Entre na Ponte Vila Guilherme para atravessar a Marginal<br><br>

		Vire à direita na <b>Av. Bom Jardim</b><br><br>

		Passando a lombada eletrônica, vire à direita na segunda rua <b>(Iturama)</b><br><br>

		Vire à esquerda na primeira rua <b>(Antônio de Andrade)</b>
    <br><br>
		
    
        <a href="https://www.google.com.br/maps/place/R.+Antonio+de+Andrade,+109+-+Pari/" target="_blank">
        <img src="img/mapa_static.png">
        </a>
        </div>
    """          

    # generate mapa
    mapa_html = open("mapa.html", "w")
    print(generate_custom("""<br>
    <div style="float:right; margin-right:10px;"><i><a href="mapa_impr.html">Página para impressão</a></i></div>
    <br>

    {mapa}
    
    """.format(mapa=mapa_content)), file=mapa_html)
    mapa_html.close()

    # generate mapa printable
    mapa_impr_html = open("mapa_impr.html", "w")
    print(generate_custom_page_printable("""
    {mapa}
    """.format(mapa=mapa_content)), file=mapa_impr_html)
    mapa_impr_html.close()
        
def generate_sidebar():
    """return a string containing only <li> items"""
    sidebar = []

    categories_file = open("c:/Users/heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/codigos/categories.txt")
    for line in categories_file:
        if not line[0] == "#":
            category_data = line.split(";")
            category_name = category_data[1].strip()
            sidebar.append('<!-- {name} --><li><a href="pr_{id}.html">{name}</a></li>'.
                           format(name=category_name,
                                  id=category_data[0]))
    categories_file.close()
    return "\n".join(sorted(sidebar))

def generate_gallery(category_id):
    """return a string containing <li> items"""
    product_db = load_product_names()
    gallery = ""

    codigos_file=open("c:/Users/heitor/Desktop/emacs-24.3/bin/pontual.github.io/produtos/codigos/{id}.txt".format(id=category_id))
    for codigo in codigos_file:
        codigo = codigo.strip()
        gallery += ('<li><a class="product_group" href="produtos/fotos/full_{codigo}.jpg" title="{desc} - {codigo}"><img src="produtos/fotos/thumb_{codigo}.jpg"><br>{codigo}<br>{desc}</a></li>\n'.
                    format(codigo=codigo, desc=product_db.get(codigo, "")))
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
	<title>Pontual Import Brindes</title>
	<link rel="stylesheet" href="produtos/css/produtos.css">
	<link rel="stylesheet" href="css/main.css" type="text/css">
	<link rel="stylesheet" href="css/slick.css" type="text/css">
	<link rel="stylesheet" href="css/colorbox.css" type="text/css">
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
PONTUAL IMPORT BRINDES
</span><br>
<i>Brindes e Presentes Promocionais</i><br>
</a>
<span class="telefones">
{telefones}<br>
<a href="mailto:{email}">{email}</a>
</span>
<br>
		</div>
	  <div class="site_address">
<a href="mapa.html">
Rua Antônio de Andrade, 109<br>
Canindé<br>
Sao Paulo, SP, CEP 03034-080<br>
<u><b>Como chegar</b></u>
</a>
	  </div>
	</div>
""".format(telefones=TELEFONES, email=EMAIL)

site_footer = """
<div class="back_to_top">
<a href="#top">
Voltar ao topo <!-- <img src="img/uparrow.png" style="vertical-align:top;"> -->
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
{sidebar}
		</ul>
		<br>
		<div class="site_footer">
		  (C) 2014
		</div>
	  </div>
          <div class="site_content">
    <br>
        <div style="float:right; margin-right:10px;"><i><a href="pr_{id}_impr.html">Página para impressão</a></i></div>
    <br>
		<div class="site_gallery">
		  <span class="category_name">{name}</span>
		  <div class="container" id="gallery_container"> 
			<div id="links">
			  <ul class="products">
{gallery}
			  </ul>
			</div>			
		  </div>
		</div>
	  </div>
	</div>
	<!-- http://jsfiddle.net/9Wg3T/3/ -->
	<script type="text/javascript" src="js/jquery.min.js"></script>
        <script type="text/javascript" src="js/jquery.colorbox-min.js"></script>
	<script type="text/javascript" src="js/setup_colorbox.js"></script>
    {footer}
    </body>
    </html>""".format(sidebar=generate_sidebar(),
                      name=category_name,
                      gallery=generate_gallery(category_id),
                      id=category_id,
                      footer=site_footer)
    return output


def generate_custom(content):
    output = site_header + """
	<div class="site_body_container">
	  <div class="site_sidebar">
		<ul>
{sidebar}
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
{content}
	  </div>
	</div>

    {footer}

	<!-- http://jsfiddle.net/9Wg3T/3/ -->
	<script type="text/javascript" src="js/jquery.min.js"></script>
    </body>
    </html>""".format(sidebar=generate_sidebar(), content=content,
                      footer=site_footer)
    return output

def generate_index(content):
    output = site_header + """
	<div class="site_body_container">
	  <div class="site_sidebar">
		<ul>
{sidebar}
		</ul>
		<br>
		<div class="site_footer">
		  (C) 2014
		</div>
	  </div>
          <div class="site_content">
{content}
	  </div>
	</div>

    {footer}

	<!-- http://jsfiddle.net/9Wg3T/3/ -->
	<script type="text/javascript" src="js/jquery.min.js"></script>
    <script type="text/javascript" src="js/slick.min.js"></script>
    <script type="text/javascript" src="js/setup_slick.js"></script>
    </body>
    </html>""".format(sidebar=generate_sidebar(), content=content,
                      footer=site_footer)
    return output


printable_header = """
<div class="printable_header">
<b>PONTUAL IMPORT BRINDES</b><br>
R. Antônio de Andrade, 109 - Canindé - São Paulo, SP, CEP 03034-080<br>
{telefones}
</div>
""".format(telefones=TELEFONES)
    
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
	<title>Pontual Import Brindes</title>
	<link rel="stylesheet" href="produtos/css/produtos.css">
	<link rel="stylesheet" href="css/main.css" type="text/css">
    	<link rel="stylesheet" href="css/colorbox.css" type="text/css">
  </head>
  <body>
    <a href="pr_{id}.html">Voltar</a><br>
{printable_header}
<hr>
    <div class="site_content">
		<div class="site_gallery">
		  <span class="category_name">{name}</span>
		  <div class="container" id="gallery_container"> 
			<div id="links">
			  <ul class="products">
{gallery}
			  </ul>
			</div>			
		  </div>
		</div>
	  </div>
	</div>
	<!-- http://jsfiddle.net/9Wg3T/3/ -->
	<script type="text/javascript" src="js/jquery.min.js"></script>
    	<script type="text/javascript" src="js/jquery.colorbox-min.js"></script>
	<script type="text/javascript" src="js/setup_colorbox.js"></script>
    </body>
    </html>""".format(id=category_id,
                      name=category_name,
                      gallery=generate_gallery(category_id),
                      printable_header=printable_header)
    return output

def generate_custom_page_printable(content):
    output = """
<html>
  <head>
        <meta charset="utf-8">
        <title>Pontual Import Brindes</title>
        <link rel="stylesheet" href="produtos/css/produtos.css">
        <link rel="stylesheet" href="css/main.css" type="text/css">
  </head>
  <body>
        <a href="index.html">Voltar</a><br>
{printable_header}    
<hr>
        <div class="site_content">
{content}
        </div>
        <!-- http://jsfiddle.net/9Wg3T/3/ -->
        <script type="text/javascript" src="js/jquery.min.js"></script>
        </body>
</html>""".format(content=content, printable_header=printable_header)
    return output
