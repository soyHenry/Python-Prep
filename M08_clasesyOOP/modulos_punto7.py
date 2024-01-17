class Funciones:

    def __init__(self, lista_numeros):
        self.lista = lista_numeros
        
    def verificar_primo(self, numero):
        es_primo = True
        for divisor in range (2, numero):
            if numero % divisor == 0:
             es_primo = False
             break 
        return es_primo
      

    def calcular_moda(self, lista):

        from collections import Counter  

        conteo = Counter(lista)
        llave = max(conteo, key = conteo.get)
        valor = conteo[llave] 

        return llave, valor


    def convertir_grados(self, valor, origen, destino):
    
        if origen == "Celsius":
            if destino  == "Celsius":
                valor_destino = valor
            elif destino == "Farenheit":
                valor_destino = (valor * 9/5) + 32
            elif destino == "Kelvin":
                valor_destino = valor + 273.15
            else:
                print("Debe ingresar un destino correcto")
    
        if origen == "Farenheit":
            if destino == "Celsius":
                valor_destino = (valor -32) * 5/9
            elif destino == "Farenheit":
                valor_destino = valor_destino       
            elif destino == "Kelvin":
                valor_destino = ((valor - 32 )* 5/9) + 273.15
            else:
                print("Debe ingresar un destino correcto")    
    
        if origen == "Kelvin":
            if destino == "Celsius":
                valor_destino = valor - 273.15 
            elif destino == "Farenheit":
                valor_destino = ((valor - 273.15) * 9/5) + 32
            elif destino == "Kelvin":
                valor_destino = valor
            else:
                print("Debe ingresar un destino correcto")

        return valor_destino

    def calcular_factorial (self,numero):

        if type(numero) != int:
            return "La entrada debe ser in entero"
        if numero <= 0:
            return "La entrada debe ser un positivo"
        if numero == 1:
            return 1
        numero = numero * self.calcular_factorial(numero - 1)

        return numero    