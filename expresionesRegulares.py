import re

patron1=re.compile('[-+*=/]') 
patron2=re.compile('\d+')
patron3=re.compile('[^A-Za-z0-9_]')
patron4=re.compile('[A-Za-z]')

listaTokens=[]


linea="501 22 2312 * - 10 2 / + z10 1k0 a i anita_1 duvan{shu} ="


colaCad = linea.split(" ")
while len( colaCad)!=0:
    valor= colaCad.pop(0)
    if patron1.search(valor):
        listaTokens.append(("operador", valor))
    elif patron2.match(valor):
        if patron4.search(valor):
            listaTokens.append(("elemento no valido", valor))
        else:
            listaTokens.append(("digito", valor))
    elif patron3.search(valor):
        listaTokens.append(("elemento no valido", valor))
    else:
        listaTokens.append(("variable", valor))
for x in listaTokens:
    print x
