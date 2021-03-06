from __future__ import print_function

import os
from datetime import datetime
import odf2array as odsreader

# Run in Python 2.7.
# Uses odfpy https://pypi.python.org/pypi/odfpy
# and odf2array by marco83
# http://www.marco83.com/work/173/read-an-ods-file-with-python-and-odfpy/

os.chdir("c:/Users/Heitor/Desktop/emacs-24.3/bin/")

commonheader = """
<html>
<head>
<link rel="stylesheet" href="../css/main.css" type="text/css">
<link rel="stylesheet" href="../css/tablesorterblue/style.css" type="text/css">
<script type="text/javascript" src="../js/jquery.min.js"></script>
<script type="text/javascript" src="../js/jquery.tablesorter.min.js"></script>
<title>Pontual Listas</title>
</head>

<body>
<center>
<a href=".."><b>Voltar</b></a><br>
<div style="width:500px">
<div align="right">Atualizado: 
""" + datetime.now().strftime("%d/%m/%Y") + "</div>"

commonfooter = """
  </tbody>
</table>
</div>
</center>
"""

aguardarfooter = commonfooter + """
<script>
  $(document).ready(function() {
    $("#myTable").tablesorter({ sortList: [[0,0]] });
  });
</script>
"""

chegandofooter = commonfooter + """
<script> 
  $(document).ready(function() {
    $("#myTable").tablesorter({ sortList: [[0,0]] });
  });
</script>
"""

chegandoheader = commonheader + '''
<h2><a href="aguardar.html">Clique aqui para ver a lista de pedidos de clientes
aguardando chegada de container ou desistencia</a></h2>
<br><br>
<h1>PRODUTOS ENCOMENDADOS DA FABRICA</h1>
O numero seguido de '+' indica que chegara num container deste numero ou maior.
<br><br>
Clique na palavra "Container" abaixo para classificar os produtos pelo
container.
<table id="myTable" class="tablesorter">
  <thead>
    <tr>
      <th width="20%">Codigo</th>
      <th width="20%">Container</th>
      <th width="20%">Disponivel</th>
      <th width="20%">Total</th>
      <th width="20%">Ja reservado</th>
    </tr>
  </thead>
  <tbody>
'''

aguardarheader = commonheader + '''
<h2><a href="chegando.html">Clique aqui para ver a lista de produtos chegando
em futuros containers</a></h2>
<br><br>
<h1>PEDIDOS DE CLIENTES AGUARDANDO CONTAINER OU DESISTENCIA</h1>
<table id="myTable" class="tablesorter">
  <thead>
    <tr>
      <th width="15%">Codigo</th>
      <th width="35%">Numero do<br>container</th>
      <th width="25%">Qtde. total<br>do pedido</th>
      <th width="25%">Qtde. ja separada<br>p/ esse pedido</th>
    </tr>
  </thead>
  <tbody>
'''

chegandobody = ""
aguardarbody = ""




# aguardando desistencia
aguardarfile = odsreader.ODSReader("N:/AGUARDAR DESISTENCIA E CONTAINER.ods")
aguardartable = aguardarfile.getSheet("Aguardar")
aguardarhtml = open("pontual.github.io/chegando/aguardar.html", 'w')

lastcodigo = ""

reservadocontainer = {}

for row in aguardartable[1:]:
    # extrapolate missing columns

    # missing codigo and ja resv
    if len(row) == 4:
        row.insert(0, lastcodigo)
        row.append(0)

    # could be missing either codigo or ja resv
    # check if second-to-last value is a number
    if len(row) == 5:
        if row[3].isdigit():  # missing codigo
            row.insert(0, lastcodigo)
        else:
            row.append(0)

    aguardarbody += """
    <tr>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    </tr>""" % (row[0], row[3], row[4], row[5])

    # add to reservadocontainer for column in chegando
    codigo = row[0]
    place = row[3]
    qty = int(row[4])

    # account for jaseparado
    jaseparado = int(row[5])
    qty = qty - jaseparado
    
    if place != "Desistencia":
        if codigo not in reservadocontainer:
            reservadocontainer[codigo] = qty
        else:
            reservadocontainer[codigo] += qty

    if len(row) == 6:
        lastcodigo = row[0]

print("%s %s %s" % (aguardarheader, aguardarbody, aguardarfooter),
      file=aguardarhtml)

aguardarhtml.close()


# chegando da fabrica
chegandofile = odsreader.ODSReader("N:/CHEGANDO.ods")
chegandotable = chegandofile.getSheet("Planilha1")
chegandohtml = open("pontual.github.io/chegando/chegando.html", 'w')

for row in chegandotable[1:]:
    codigo = row[1]
    chegandoqty = int(row[3])
    if codigo in reservadocontainer:
        chegandoreservado = reservadocontainer[codigo]
    else:
        chegandoreservado = 0
    if chegandoreservado > chegandoqty:
        rowreservado = chegandoqty
    else:
        rowreservado = chegandoreservado
    if codigo in reservadocontainer:
        reservadocontainer[codigo] -= rowreservado

    chegandobody += """
    <tr>
    <td>%s</td>
    <td>%s</td>
    <td>%d</td>
    <td>%s</td>
    <td>%d</td>
    </tr>""" % (row[1], row[2], (chegandoqty - rowreservado), row[3], rowreservado)

    # OLD ORDER % (tuple(row[1:]) + (rowreservado, (chegandoqty - rowreservado)))

print("%s %s %s" % (chegandoheader, chegandobody, chegandofooter),
      file=chegandohtml)

chegandohtml.close()

