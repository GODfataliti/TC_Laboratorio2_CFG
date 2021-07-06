from japonbrasil import JapanBrasil
from sudafrica import Sudafrica
from california import California
from funciones import leerArchivo
import json


def calculoSecuencia(dicc):
    pass



#Funcion que crea las clases.
def variante(arr):

    personas = []
    lista = []
    for persona in range(len(arr)):
        for indice in range(len(arr)):
            clase1 = Sudafrica(arr[persona][indice])
            clase2 = JapanBrasil(arr[persona][indice])
            clase3 = California(arr[persona][indice])

            result1 = clase1.q0()
            result2 = clase2.q0()
            result3 = clase3.q0()

            if(result1==None):
                result1 = ''
            if(result2==None):
                result2=''
            if(result3==None):
                result3=''
            lista.append(result1)
            lista.append(result2)
            lista.append(result3)
            #print(lista)
            
        dic = dict(id_persona=persona, secuencia=lista)
        personas.append(dic)
        lista = []
    
    print(json.dumps(personas, sort_keys=False, indent=4))
    return personas


#Menu main.
def main():

    #MENU
    try:
        print('1.Ingresar Archivo\n2.Escribir texto.\n OPC: ', end="")
        opc= str(input())
        if(opc=='1'):
            print('Nombre del Archivo: ', end="")
            archivo = input()
            doc = leerArchivo(archivo)
            lineas = []
            for i in range(len(doc)):
                lineas.append(doc[i].split())
            
            print(lineas)
            variante(lineas)
        
        elif(opc=='2'):
            print("Escriba la secuencia: ", end="")
            secuencia = input()
            secuencia = secuencia.split()
            print(secuencia)
            variante(secuencia)

        else:
            print("Opcion incorrecta.")
    except Exception as e:
        print(f'[!] ERROR: {e} [!]')



if '__main__' == __name__:
    main()