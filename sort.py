#!/usr/bin/python3
# -- coding: UTF-8 --

import cgi, cgitb
import random

form = cgi.FieldStorage()

numInicio = int(form.getvalue("inicio"))
numFinal = int(form.getvalue("final"))
qtdNums = int(form.getvalue("qnt"))

result="" #resultado

if(numInicio > numFinal):
    result='O numero inicial nao pode ser maior que o numero final'
elif(qtdNums > (numFinal - numInicio)):
    result='Operacao nao permitida'
else:
    sorteio = random.sample(range(numInicio, numFinal), qtdNums)

    nums = (sorted(sorteio))
    nums = str(nums).strip("[]")
    result = "".join(nums)

print("Content-Type:text/html\n\n")
print("<html>")
print("<head>")
print("<title>Sorteador</title>")
print("</head>")
print("<body>")
print("<h2>SORTEADO: %s</h2>" %result)
print("</body>")
print("</html")
