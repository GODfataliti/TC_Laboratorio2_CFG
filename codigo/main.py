from japonbrasil import JapanBrasil
from sudafrica import Sudafrica
from california import California
from funciones import leerArchivo
import json


def calculoSecuencia(dicc):
    variantes = ['Sudafrica','California','JaponBrasil']

    elementos = dicc
    contadorJB = 0
    contadorCal = 0
    contadorSud = 0
    cadena = 0
    try:

        for i in range(len(elementos)):
            cadena = elementos[i]['cadena']
            print(f'cantidad cadena: {cadena}')
            for secuencia,valor in elementos[i].items():

                print(f'{secuencia}: {valor}')
                #Estan malos los if....
                if(valor=='Sudafrica'):
                    contadorSud+=1
                if(valor=='California'):
                    contadorCal+=1
                if(valor=='JaponBrasil'):
                    contadorJB+=1
                
            #calculo
            resultadoJB = int((contadorJB / cadena)*100)
            resultadoCal = int((contadorCal / cadena)*100)
            resuladoSud = int((contadorSud / cadena)*100)
            print(f'Variante JB: {resultadoJB}\t Variante Cal: {resultadoCal}\t Variante Sud: {resuladoSud}')
    
    except Exception as e:
        print(f'[!] ERROR: {e} [!]')

    
    

            




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
            
        dic = dict(id_persona=persona, secuencia=lista,cadena=(len(arr)))
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
            resultado = variante(lineas)
            calculoSecuencia(resultado)
        
        elif(opc=='2'):
            print("Escriba la secuencia: ", end="")
            secuencia = input()
            secuencia = secuencia.split()
            print(secuencia)
            resultado = variante(lineas)
            calculoSecuencia(resultado)

        else:
            print("Opcion incorrecta.")
    except Exception as e:
        print(f'[!] ERROR: {e} [!]')



if '__main__' == __name__:
    main()