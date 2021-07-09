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

#Funcion que realiza el calculo porcentual
def calculoSecuencia(dicc):

    elementos = dicc
    contadorJB = 0
    contadorCal = 0
    contadorSud = 0
    id_persona = 0
    cadena = 0
    try:
        for i in range(len(elementos)):
            cadena = 0
            cadena = elementos[i]['cadena']
            id_persona = 0
            contadorJB = 0
            contadorCal = 0
            contadorSud = 0
            for secuencia,valor in elementos[i].items():
                id_persona = elementos[i]['id_persona']
                #print(f'{secuencia}: {valor}')
                if(type(valor)!=type(cadena)):
                    for estado in range(len(valor)):
                        if(valor[estado]=='Sudafrica'):
                            contadorSud+=1
                            #print(f'Estado: {valor[estado]}')
                        if(valor[estado]=='California'):
                            contadorCal+=1
                            #print(f'Estado: {valor[estado]}')
                        if(valor[estado]=='JaponBrasil'):
                            contadorJB+=1
                            #print(f'Estado: {valor[estado]}')
                
            #calculo
            resultadoJB = int((contadorJB / cadena)*100)
            resultadoCal = int((contadorCal / cadena)*100)
            resuladoSud = int((contadorSud / cadena)*100)
            print(f'Persona {id_persona}: Variante JB: {resultadoJB}%\t Variante Cal: {resultadoCal}%\t Variante Sud: {resuladoSud}%')
    
    except Exception as e:
        print(f'[!] ERROR: {e} [!]\n')
