
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



class Sudafrica:

    def __init__(self,arr):
        self.pila = Pila()
        self.arr = list(arr)
        #e: no cambia la cadena, desapila.

    
    def q0(self):
        #Si esta vacio, apilo una Z.
        if(len(self.pila)==0):
            self.pila.apilar('Z')
            self.q1()
    
    def q1(self):
        
        #Si hay un A en el arr y una Z en la pila, apilo una A.
        if(self.arr[0].upper()=='A' and self.pila[-1].upper()=='Z'):
            self.arr.pop(0) #Borra el elemento visto del arr
            self.pila.apilar('A') #Agrega el elemento visto en el arr
            self.q1()

        #Si hay un A en el arr y una A en la pila, apilo una A.
        if(self.arr[0].upper()=='A' and self.pila[-1].upper()=='A'):
            self.arr.pop(0) #Borra el elemento visto del arr
            self.pila.apilar('A') #Agrega el elemento visto en el arr
            self.q1()
        
        #Si hay un C en el arr y una A en la pila, apilo una C.
        if(self.arr[0].upper()=='C' and self.pila[-1].upper()=='A'):
            self.arr.pop(0) #Borra el elemento visto del arr
            self.pila.apilar('C') #Agrega el elemento visto en el arr
            self.q2()

    
    def q2(self):
        
        #Si hay un C en el arr y una C en la pila, apilo una C.
        if(self.arr[0].upper()=='C' and self.pila[-1].upper()=='C'):
            self.arr.pop(0)
            self.pila.apilar('C')
            self.q2()
        
        #Si hay un U en el arr y una C en la pila, desapila.
        if(self.arr[0].upper()=='U' and self.pila[-1].upper()=='C'):
            self.arr.pop(0)
            self.pila.desapilar()
            self.q3()
        
        #Si hay un G en el arr y una A en la pila, desapila.
        if(self.arr[0].upper()=='G' and self.pila[-1].upper()=='A'):
            self.arr.pop(0)
            self.pila.desapilar()
            self.q4()
    
    def q3(self):
        
        #No se modifica el arr, y si hay C en la pila, desapila.
        if(self.pila[-1].upper()=='C'):
            self.pila.desapilar()
            self.q2()
    
    def q4(self):

        #Si hay G en el arr, y una A en la pila, desapilo.
        if(self.arr[0].upper()=='G' and self.pila[-1].upper()=='A'):
            self.pila.desapilar()
            self.q4()
        
        #Si hay una G en el arr, elimino la G.
        if(self.arr[0].upper()=='G'):
            self.arr.pop(0)
            self.q5()
    
    def q5(self):

        #Si hay una G en el arr, elimino la G.
        if(self.arr[0].upper()=='G'):
            self.arr.pop(0)
            self.q5()
        
        #Si esta vacio el arr, y hay una Z en la pila, desapilo.
        if(len(self.arr)==0 and self.pila[-1].upper()=='Z'):
            self.pila.desapilar()
            self.q6()
    
    def q6(self):
        #Si tiene adn de negro.
        print("30cm confirmado.")




def main():

    Test = Sudafrica('AACCCCUUGGGGGG')

if __name__ == '__main__':
    main()