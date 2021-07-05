#Lector de Archivo.

def leerArchivo(doc):
	try:
		f = open(doc,'r')
		lineas = f.readlines()
		#Mandar a la 2da funcion que separe el archivo.
		f.close()
		return lineas
	except Exception as e:
		print(f'[!] ERROR: {e} [!]\n')






#Crear clase Pila
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


#Clase Automata Sudafrica.
class Sudafrica:

    def __init__(self,arr):
        self.pila = Pila()
        self.arr = list(arr)
        #e: no cambia la cadena, desapila.

    
    def q0(self):
        #Si esta vacio, apilo una Z.
        if(len(self.pila.items)==0):
            self.pila.apilar('Z')
            return self.q1()
    
    def q1(self):
        
        print(f'Arr: {self.arr}')
        print(f'Pila: {self.pila.mostrar()}')
        if(len(self.arr)>0):
            #Si hay un A en el arr y una Z en la pila, apilo una A.
            if(self.arr[0].upper()=='A' and self.pila.items[-1].upper()=='Z'):
                self.arr.pop(0) #Borra el elemento visto del arr
                self.pila.apilar('A') #Agrega el elemento visto en el arr
                return self.q1()

            #Si hay un A en el arr y una A en la pila, apilo una A.
            elif(self.arr[0].upper()=='A' and self.pila.items[-1].upper()=='A'):
                self.arr.pop(0) #Borra el elemento visto del arr
                self.pila.apilar('A') #Agrega el elemento visto en el arr
                return self.q1()
        
            #Si hay un C en el arr y una A en la pila, apilo una C.
            elif(self.arr[0].upper()=='C' and self.pila.items[-1].upper()=='A'):
                self.arr.pop(0) #Borra el elemento visto del arr
                self.pila.apilar('C') #Agrega el elemento visto en el arr
                return self.q2()

    
    def q2(self):

        print(f'Arr: {self.arr}')
        print(f'Pila: {self.pila.mostrar()}')
        
        #Si hay un C en el arr y una C en la pila, apilo una C.
        if(self.arr[0].upper()=='C' and self.pila.items[-1].upper()=='C'):
            self.arr.pop(0)
            self.pila.apilar('C')
            return self.q2()
        
        #Si hay un U en el arr y una C en la pila, desapila.
        elif(self.arr[0].upper()=='U' and self.pila.items[-1].upper()=='C'):
            self.arr.pop(0)
            self.pila.desapilar()
            return self.q3()
        
        #Si hay un G en el arr y una A en la pila, desapila.
        elif(self.arr[0].upper()=='G' and self.pila.items[-1].upper()=='A'):
            self.arr.pop(0)
            self.pila.desapilar()
            return self.q4()
    
    def q3(self):

        print(f'Arr: {self.arr}')
        print(f'Pila: {self.pila.mostrar()}')
        
        #No se modifica el arr, y si hay C en la pila, desapila.
        if(self.pila.items[-1].upper()=='C'):
            self.pila.desapilar()
            return self.q2()
    
    def q4(self):

        print(f'Arr: {self.arr}')
        print(f'Pila: {self.pila.mostrar()}')

        #Si hay G en el arr, y una A en la pila, desapilo.
        if(self.arr[0].upper()=='G' and self.pila.items[-1].upper()=='A'):
            self.pila.desapilar()
            return self.q4()
        
        #Si hay una G en el arr, elimino la G.
        elif(self.arr[0].upper()=='G'):
            self.arr.pop(0)
            return self.q5()
    
    def q5(self):

        print(f'Arr: {self.arr}')
        print(f'Pila: {self.pila.mostrar()}')

        #Si hay una G en el arr, elimino la G.
        if(len(self.arr)>0):
            if(self.arr[0].upper()=='G'):
                self.arr.pop(0)
                return self.q5()
        
        #Si esta vacio el arr, y hay una Z en la pila, desapilo.
        elif(len(self.arr)==0 and self.pila.items[-1].upper()=='Z'):
            self.pila.desapilar()
            return self.q6()
    
    def q6(self):

        print(f'Arr: {self.arr}')
        print(f'Pila: {self.pila.mostrar()}')

        resultado = 'Sudafrica'
        return resultado


#==============================================================================================================================
class JapanBrasil:

    def __init__(self,arr):
        self.pila = Pila()
        self.arr = list(arr)
    
    def q0(self):
        #Si esta vacio, apilo una Z.
        if(len(self.pila.items)==0):
            self.pila.apilar('Z')
            return self.q1()
    
    def q1(self):

        print(f'Arr: {self.arr}')
        print(f'Pila: {self.pila.mostrar()}')

        #Si hay un U en el arr y una U en la pila, apilo una U.
        if(len(self.arr)>0):
            if(self.arr[0].upper()=='U' and self.pila.items[-1].upper()=='U'):
                self.arr.pop(0) #Borra el elemento visto del arr
                self.pila.apilar('U')
                return self.q1()

            #Si hay un U en el arr y una Z en la pila, apilo una U.
            elif(self.arr[0].upper()=='U' and self.pila.items[-1].upper()=='Z'):
                self.arr.pop(0)
                self.pila.apilar('U')
                return self.q1()
            #Si hay una C en el arr y una U en la pila, desapilo
            elif(self.arr[0].upper()=='C' and self.pila.items[-1].upper()=='U'):
                self.arr.pop(0)
                self.pila.desapilar()
                return self.q2()
    
    def q2(self):

        print(f'Arr: {self.arr}')
        print(f'Pila: {self.pila.mostrar()}')

        #Si hay una U en la pila, desapilo.
        if(self.pila.items[-1].upper()=='U'):
            self.pila.desapilar()
            return self.q3()
    
    def q3(self):

        print(f'Arr: {self.arr}')
        print(f'Pila: {self.pila.mostrar()}')

        #Si hay una C en el arr, y una U en la pila, desapila.
        if(self.arr[0].upper()=='C' and self.pila.items[-1].upper()=='U'):
            self.arr.pop(0)
            self.pila.desapilar()
            return self.q2()
        
        #Si hay un A en el arr, y una Z en la pila, apilo una A.
        elif(self.arr[0].upper()=='A' and self.pila.items[-1].upper()=='Z'):
            self.arr.pop(0)
            self.pila.apilar('A')
            return self.q4()
        
        #Si hay una Z en la pila, desapilo
        elif(self.pila.items[-1].upper()=='Z'):
            self.pila.desapilar()
            return self.q7()
    
    def q4(self):

        print(f'Arr: {self.arr}')
        print(f'Pila: {self.pila.mostrar()}')

        #Si hay una A en el arr, y una A en la pila, apilamos A.
        if(self.arr[0].upper()=='A' and self.pila.items[-1].upper()=='A'):
            self.arr.pop(0)
            self.pila.apilar('A')
            return self.q4()
        
        #Si hay una G en el arr, eliminadamos.
        elif(len(self.arr)>0):
            if(self.arr[0].upper()=='G'):
                self.arr.pop(0)
                return self.q5()
        
    def q5(self):

        print(f'Arr: {self.arr}')
        print(f'Pila: {self.pila.mostrar()}')

        #Si hay una G en el arr, y un A en la pila, desapilamos.
        if(len(self.arr)>0):
            if(self.arr[0].upper()=='G' and self.pila.items[-1].upper()=='A'):
                self.arr.pop(0)
                self.pila.desapilar()
                return self.q6()
    
    def q6(self):

        print(f'Arr: {self.arr}')
        print(f'Pila: {self.pila.mostrar()}')

        #si hay una G, eliminado.
        if(len(self.arr)>0):
            if(self.arr[0].upper()=='G'):
                self.arr.pop(0)
                return self.q5()
        
        #Si hay una Z en la pila. desapilo.
        elif(self.pila.items[-1].upper()=='Z'):
            self.pila.desapilar()
            return self.q7()
    
    def q7(self):

        print(f'Arr: {self.arr}')
        print(f'Pila: {self.pila.mostrar()}')

        resultado = 'JaponBrasil'
        return resultado


#===================================================================================================================================
class California:

    def __init__(self,arr):
        self.pila = Pila()
        self.arr = list(arr)
        #e: no cambia la cadena, desapila.

    def q0(self):
        #Si esta vacio, apilo una Z.
        if(len(self.pila.items)==0):
            self.pila.apilar('Z')
            return self.q1()

    def q1(self):

        print(f'Arr: {self.arr}')
        print(f'Pila: {self.pila.mostrar()}')

        if(len(self.arr)>0):
            #Si hay un U en el arr y una Z en la pila, apilo una U.
            if(self.arr[0].upper()=='U' and self.pila.items[-1].upper()=='Z'):
                self.arr.pop(0) #Borra el elemento visto del arr
                self.pila.apilar('U') #Agrega el elemento visto en el arr
                return self.q1()

            #Si hay un U en el arr y una U en la pila, apilo una U.
            elif(self.arr[0].upper()=='U' and self.pila.items[-1].upper()=='U'):
                self.arr.pop(0)
                self.pila.apilar('U')
                return self.q1()

            #Si hay un C en el arr y una U en la pila, desapila.
            elif(self.arr[0].upper()=='C' and self.pila.items[-1].upper()=='U'):
                self.arr.pop(0)
                self.pila.desapilar()
                return self.q2()

            #Si hay un C en el arr y una Z en la pila, apilo una C.
            elif(self.arr[0].upper()=='C' and self.pila.items[-1].upper()=='Z'):
                self.arr.pop(0)
                self.pila.apilar('C')
                return self.q3()

    def q2(self):

        print(f'Arr: {self.arr}')
        print(f'Pila: {self.pila.mostrar()}')
        
        if(len(self.arr)>0):
            #Si hay un C en el arr y una U en la pila, desapila.
            if(self.arr[0].upper()=='C' and self.pila.items[-1].upper()=='U'):
                self.arr.pop(0) 
                self.pila.desapilar()
                return self.q2()

            #Si hay un C en el arr y una Z en la pila, apilo una C.
            elif(self.arr[0].upper()=='C' and self.pila.items[-1].upper()=='Z'):
                self.arr.pop(0) #Borra el elemento visto del arr
                self.pila.apilar('C') #Agrega el elemento visto en el arr
                return self.q3()

    def q3(self):

        print(f'Arr: {self.arr}')
        print(f'Pila: {self.pila.mostrar()}')

        if(len(self.arr)>0):
            #Si hay un C en el arr y una C en la pila, apilo una C.
            if(self.arr[0].upper()=='C' and self.pila.items[-1].upper()=='C'):
                self.arr.pop(0) #Borra el elemento visto del arr
                self.pila.apilar('C') #Agrega el elemento visto en el arr
                return self.q3()

            #Si hay una G en el arr y una C en la pila, desapila.            
            elif(self.arr[0].upper()=='G' and self.pila.items[-1].upper()=='C'):
                self.arr.pop(0)
                self.pila.desapilar()
                return self.q4()
    
    def q4(self):

        print(f'Arr: {self.arr}')
        print(f'Pila: {self.pila.mostrar()}')
        
        if(len(self.arr)>0):
            #Si hay un G en el arr y una C en la pila, desapila.
            if(self.arr[0].upper()=='G' and self.pila.items[-1].upper()=='C'):
                self.arr.pop(0) #Borra el elemento visto del arr
                self.pila.desapilar()
                return self.q4()

            #Si hay una A en el arr, elimino la A.
            elif(self.arr[0].upper()=='A'):
                self.arr.pop(0)
                return self.q5()

    def q5(self):

        print(f'Arr: {self.arr}')
        print(f'Pila: {self.pila.mostrar()}')

        if(len(self.arr)>0):
            #Si hay un A en el arr elimino la A.
            if(self.arr[0].upper()=='A'):
                self.arr.pop(0)
                return self.q5()
        #Si esta vacio el arr, y hay una Z en la pila, desapilo.
        elif(len(self.arr)==0 and self.pila.items[-1].upper()=='Z'):
            self.pila.desapilar()
            return self.q6()
        
    def q6(self):

        print(f'Arr: {self.arr}')
        print(f'Pila: {self.pila.mostrar()}')

        resultado = 'California'
        return resultado



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