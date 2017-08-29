class Pila:
    def __init__(self):
        self.items=[]

    def apilar(self,dato):
        self.items.append(dato)

    def desapilar(self):
        return self.items.pop()

    def pilaVacia(self):
        return self.items == []


class Nodo():
    def __init__(self,valor,izq=None,der=None):
        self.valor=valor
        self.izq=izq
        self.der=der

def evaluar(arbol):
    if arbol.valor=="+":
        return evaluar(arbol.izq)+evaluar(arbol.der)
    if arbol.valor=="-":
        return evaluar(arbol.izq)-evaluar(arbol.der)
    if arbol.valor=="*":
        return evaluar(arbol.izq)*evaluar(arbol.der)
    if arbol.valor=="/":
        return evaluar(arbol.izq)/ evaluar(arbol.der)
    


def armarArbol(pila):
   
    auxPila=Pila()
    izq, der, valor=None,None,""
    while not len (pila)==0:
       
        valor=pila.pop(0)
        if valor in "+-*/":
            der=auxPila.desapilar()
            izq=auxPila.desapilar()
            auxPila.apilar(Nodo(valor,izq,der))
        elif valor.isdigit()==false:
            der=auxPila.desapilar()
            izq=valor
            auxPila.apilar(Nodo(pila.pop(0),izq,der))
            else:
                auxPila.apilar(Nodo(valor))
   
    return auxPila.desapilar()
                


    pilaCad=linea.split(" ")
    print evaluar(armarArbol(pilaCad))

