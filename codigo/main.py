from japonbrasil import JapanBrasil
from sudafrica import Sudafrica
from california import California


#Funcion para leer archivos
def leerArchivo(doc):
	try:
		f = open(doc,'r')
		lineas = list(f.readlines())
		#Mandar a la 2da funcion que separe el archivo.
		f.close()
		return lineas
	except Exception as e:
		print(f'[!] ERROR: {e} [!]\n')

#Clase Pila.
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

#Funcion que crea las clases.
def variante(arr):

    lista = []

    for indice in range(len(arr)):
        clase1 = Sudafrica(arr[indice])
        clase2 = JapanBrasil(arr[indice])
        clase3 = California(arr[indice])

        result1 = clase1.q0()
        result2 = clase2.q0()
        result3 = clase3.q0()

        lista.append(result1)
        lista.append(result2)
        lista.append(result3)
        print(lista)
        lista = []


#Menu main.
def main():

    #MENU
    print('1.Ingresar Archivo\n2.Escribir texto.\n OPC: ', end="")
    opc= str(input())
    if(opc=='1'):
        print('Nombre del Archivo: ', end="")
        archivo = input()
        doc = leerArchivo(archivo)
        doc = doc[0].split()
        print(doc)
        variante(doc)
    
    elif(opc=='2'):
        print("Escriba la secuencia: ", end="")
        secuencia = input()
        secuencia = secuencia.split()
        print(secuencia)
        variante(secuencia)

    else:
        print("Opcion incorrecta.")



if '__main__' == __name__:
    main()