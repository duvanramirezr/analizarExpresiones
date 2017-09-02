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
    print arbol.valor
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
            
    #return diccionario


linea = "5 2 2 * - 10 2 / + z ="
linea2 = "5 2 2 * - 20 2 / + x ="
linea3 = "x z + r ="
pilaCad = linea.split(" ")
armarArbol(pilaCad)
pilaCad = linea2.split(" ")
armarArbol(pilaCad)
pilaCad = linea3.split(" ")
armarArbol(pilaCad)
