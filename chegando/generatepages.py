from __future__ import print_function

import os
from datetime import datetime
import odf2array as odsreader

# Run in Python 2.7.
# Uses odfpy https://pypi.python.org/pypi/odfpy
# and odf2array by marco83
# http://www.marco83.com/work/173/read-an-ods-file-with-python-and-odfpy/

os.chdir("c:/Users/Heitor/Desktop/emacs-24.3/bin/")
# chegando da fabrica
chegandofile = odsreader.ODSReader("N:/CHEGANDO.ods")
chegandotable = chegandofile.getSheet("Planilha1")
chegandohtml = open("pontual.github.io/chegando/chegando.html", 'w')

commonheader = """
<html>
<head>
<link rel="stylesheet" href="../css/main.css" type="text/css">
<link rel="stylesheet" href="../css/tablesorterblue/style.css" type="text/css">
<script type="text/javascript" src="../js/jquery.min.js"></script>
<script type="text/javascript" src="../js/jquery.tablesorter.min.js"></script>
</head>

<body>
<a href=".."><b>Voltar</b></a><br>
<div style="width:500px">
<div align="right">Atualizado: 
""" + datetime.now().strftime("%d/%m/%Y") + "</div>"

commonfooter = """
  </tbody>
</table>
</div>

<script>
  $(document).ready(function() {
    $("#myTable").tablesorter();
  });
</script>
"""

chegandoheader = commonheader + """
<table id="myTable" class="tablesorter">
  <thead>
    <tr>
      <th width="20%">Codigo</th>
      <th width="20%">Container</th>
      <th width="20%">Quantidade</th>
      <th width="20%">Ja reservado</th>
      <th width="20%">Disponivel</th>
    </tr>
  </thead>
  <tbody>
"""

chegandobody = ""

for row in chegandotable[1:]:
    chegandobody += """
    <tr>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    </tr>""" % tuple(row[1:])
    
print("%s %s %s" % (chegandoheader, chegandobody, commonfooter),
      file=chegandohtml)

chegandohtml.close()

# aguardando desistencia
aguardarfile = odsreader.ODSReader("N:/AGUARDAR DESISTENCIA E CONTAINER.ods")
aguardartable = aguardarfile.getSheet("Aguardar")
aguardarhtml = open("pontual.github.io/chegando/aguardar.html", 'w')

aguardarheader = commonheader + """
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
"""

aguardarbody = ""
lastcodigo = ""

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

    if len(row) == 6:
        lastcodigo = row[0]

print("%s %s %s" % (aguardarheader, aguardarbody, commonfooter),
      file=aguardarhtml)

aguardarhtml.close()
