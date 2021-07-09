from funciones import Pila

class California:

    def __init__(self,arr):
        self.pila = Pila()
        self.arr = list(arr)

    def q0(self):
        #Si esta vacio, apilo una Z.
        if(len(self.pila.items)==0):
            self.pila.apilar('Z')
            return self.q1()

    def q1(self):

        #print(f'Arr q1: {self.arr}')
        #print(f'Pila q1: {self.pila.mostrar()}')

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

        #print(f'Arr q2: {self.arr}')
        #print(f'Pila q2: {self.pila.mostrar()}')
        
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

        #print(f'Arr q3: {self.arr}')
        #print(f'Pila q3: {self.pila.mostrar()}')

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

        #print(f'Arr q4: {self.arr}')
        #print(f'Pila q4: {self.pila.mostrar()}')
        
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

        #print(f'Arr q5: {self.arr}')
        #print(f'Pila q5: {self.pila.mostrar()}')

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

        #print(f'Arr q6: {self.arr}')
        #print(f'Pila q6: {self.pila.mostrar()}')
        resultado = ''
        if(len(self.arr)==0 and len(self.pila.items)==0):
            resultado = 'California'

        return resultado