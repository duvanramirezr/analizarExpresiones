diccionario = {}
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
#linea = "5 2 2 * - 10 2 / + z ="
#linea2 = "5 2 2 * - 20 2 / + x ="
#linea3 = "x z + r ="

            
linea= raw_input("Ingrese la cadena")

while linea != "s":
    pilaCad = linea.split(" ")
    if len(pilaCad) !=1:
        armarArbol(pilaCad)
    linea= raw_input("Ingrese la cadena")


print diccionario
