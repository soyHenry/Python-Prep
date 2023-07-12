class Herramientas:
    def __init__(self, lista_numeros):
        self.lista = lista_numeros
    
    def Verificaprimo(self):
        for i in self.lista:
            if (self.__Verificaprimo(i)):
                print('El elemento', i, 'SI es un numero primo')
            else:
                print('El elemento', i, 'NO es un numero primo')

    def Conversorgrados(self, origen, destino):
        for i in self.lista:
            print(i, 'grados', origen, 'son', self.__Conversorgrados(i, origen, destino),'grados',destino)
    
    def Factorial(self):
        for i in self.lista:
            print('El factorial de ', i, 'es', self.__Factorial(i))

    def __Verificaprimo(self, num):
        pri = True
        for i in range(2,num):
            if num%i == 0:
                pri = False
                break
        return pri
    
    def Valormodal(self, lista, modo='menor'):
        
        contador = {}    
        for num in self.lista:
            if num in contador.keys():
                contador[num] += 1            
            else:
                contador[num] = 1
        moda = []
        maximo = 0
        for numero, repeticion in contador.items():
            if repeticion > maximo:
                maximo = repeticion
                moda = [numero]
            elif repeticion == maximo:
                moda.append(numero)
        if modo == 'menor':
            masRepetido_num = min(moda)
        elif modo == 'mayor':
            masRepetido_num = max(moda)
        return masRepetido_num, maximo
    
    def __Conversorgrados(self, valor, origen, destino):
        if origen == 'celsius':
            if destino == 'celsius':
                valorDestino = valor
            elif destino == 'farenheit':
                valorDestino = (valor * 9/5) + 32
            elif destino == 'kelvin':
                valorDestino = valor + 273.15
            else:
                print("Parametro de destino no valido")
        elif origen == 'farenheit':
            if destino == 'farenheit':
                valorDestino = valor
            elif destino == 'celsius':
                valorDestino = ((valor - 32)*5) /9
            elif destino == 'kelvin':
                valorDestino = ((valor - 32)*5 /9) + 273.15
            else:
                print("Parametro de destino no valido")
        elif origen == 'kelvin':
            if destino == 'kelvin':
                valorDestino = valor
            elif destino == 'farenheit':
                valorDestino = (valor - 273.15) * (9/5) + 32
            elif destino == 'celsius':
                valorDestino = (valor - 273.15) 
            else:
                print("Parametro de destino no valido")
        else:
            print("parametro de origen no valido")
        return valorDestino
    
    def __Factorial(self, numero):
        if(type(numero) != int):
            return 'El numero debe ser un entero'
        if(numero < 0):
            return 'El numero debe ser pisitivo'
        if (numero > 1):
            numero = numero * self.__Factorial(numero - 1)
        return numero