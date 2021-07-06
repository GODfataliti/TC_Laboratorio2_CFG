#Clase Pila
class Pila:
    def __init__(self):
        self.items= []

    def apilar(self, x):
        self.items.append(x)

    def desapilar(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")
    
    def mostrar(self):
        return self.items


def imprimirPilaArr():
    pass

#Funcion para leer archivos
def leerArchivo(doc):
    try:
        f = open(doc,'r')
        lineas = list(f.readlines())
        #print(lineas)
        f.close()
        return lineas
    
    except Exception as e:
        print(f'[!] ERROR: {e} [!]\n')
