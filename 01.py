
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


#Automata.
class Sudafrica:

    def __init__(self,arr):
        self.pila = Pila()
        self.arr = arr
        #e: no cambia la cadena, desapila.

    
    def q0(self):
        #Si esta vacio, apilo una Z.
        if(len(self.pila.items)==0):
            self.pila.apilar('Z')
            return self.q1()
    
    def q1(self):
        
        print(f'Arr: {self.arr}')
        print(f'Pila: {self.pila.items}')
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
        print(f'Pila: {self.pila.items}')
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
        print(f'Pila: {self.pila.items}')
        #No se modifica el arr, y si hay C en la pila, desapila.
        if(self.pila.items[-1].upper()=='C'):
            self.pila.desapilar()
            return self.q2()
    
    def q4(self):

        print(f'Arr: {self.arr}')
        print(f'Pila: {self.pila.items}')
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
        print(f'Pila: {self.pila.items}')
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
        print(f'Pila: {self.pila.items}')
        #Si tiene adn de negro.
        print("30cm confirmado.")





arr = list('AACCCCUUGGGGGG')
print(arr)
Test = Sudafrica(arr)
Test.q0()
