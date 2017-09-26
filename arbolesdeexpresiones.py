
import re

patron1=re.compile('[-+*=/]') 
patron2=re.compile('\d+')
patron3=re.compile('[^A-Za-z0-9_]')
patron4=re.compile('[A-Za-z]')

diccionario = {}
listaTokens=[]
class Pila:

    def __init__(self):
        self.items = []

    def apilar(self, dato):
        self.items.append(dato)

    def desapilar(self):
        return self.items.pop()

    def pilaVacia(self):
        return self.items == []


class Nodo():

    def __init__(self, valor, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der


def evaluar(arbol):
   
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    return int(arbol.valor)


def armarArbol(pila):
    
    auxPila = Pila()
    izq, der, valor = None, None, ""
    while not len(pila) == 0:

        valor = pila.pop(0)
       
        if valor in "+-*/":
            der = auxPila.desapilar()
            izq = auxPila.desapilar()
            auxPila.apilar(Nodo(valor, izq, der))
            

        elif valor.isdigit() == False:
            if diccionario.has_key(valor):
                valor = diccionario[valor][0]
                auxPila.apilar(Nodo(valor))
                
            else:
                aux = pila.pop(0)
                
                if aux == "=":
                     diccionario[valor] = [evaluar(auxPila.desapilar())]

        else:
            auxPila.apilar(Nodo(valor))
            


#Capturar la linea y quedarse  
#5 2 2 * - 10 2 / + z ="
#l"5 2 2 * - 20 2 / + x ="
# "x z + r ="

            
linea= raw_input("Ingrese la cadena")
colaCad=linea.split(" ")
while linea != "s":
    pilaCad = linea.split(" ")
    if len(pilaCad) !=1:
        armarArbol(pilaCad)
    linea= raw_input("Ingrese la cadena")

print "----------DICCIONARIO DE VARIABLES-----------"
print diccionario 
print "\n"


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
        
print "----------LISTA DE TOKENS-----------"
for x in listaTokens:
    print x

