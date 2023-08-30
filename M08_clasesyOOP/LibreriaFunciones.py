class Funciones7:
    def __init__(self, ListaEvaluada):
        self.Lista = ListaEvaluada

    def ValidarPrimo(self):
        for i in self.Lista:
            if(self.__ValidarPrimo(i)):
                print("El número: ", i, "es primo")
            else:
                print("El número: ", i, "no es primo")

    def ConvertirGrados(self, Origen, Destino):
        for i in self.Lista:
            print(i,"Grados ", Origen, " son: " , self.__ConvertirGrados(i, Origen, Destino), " en ", Destino)
    
    def Factorial(self):
        for i in self.Lista:
            print("El factorial de: ", i, " es: ", self.__Factorial(i))
    
    def __ValidarPrimo(self, Numero):
        EsPrimo = True
        for div in range(2, Numero):
            if (Numero % div == 0):
                EsPrimo = False
                break
        return EsPrimo
    
    def ContarDuplicados(self, ListaDeEvaluacion):
        i = 0
        TotalRepeticiones = 0
        MasRepetido = 0
        for Elemento in ListaDeEvaluacion:
            Repeticiones = 0
            j = 0   
            for Elemento in ListaDeEvaluacion:
                if (ListaDeEvaluacion[i] == ListaDeEvaluacion[j]):
                    Repeticiones+=1
                j+=1
            if(TotalRepeticiones < Repeticiones):
                TotalRepeticiones = Repeticiones
                MasRepetido = ListaDeEvaluacion[i]
            i+=1
        return MasRepetido,TotalRepeticiones
    
    def __ConvertirGrados(self, Grados, Origen, Destino):
        if(Origen == "Celsius" and Destino == "Farenheit"):
            Resultado = (Grados * 1.8) + 32
        elif (Origen == "Celsius" and Destino == "Kelvin"):
            Resultado = Grados + 273.15
        elif (Origen == "Celsius" and Destino == "Celsius"):
            Resultado = Grados
        elif (Origen == "Farenheit" and Destino == "Celsius"):
            Resultado = (Grados - 32) * (5/9)
        elif (Origen == "Farenheit" and Destino == "Kelvin"):
            Resultado = (Grados - 32) * (5/9) + 273.15
        elif (Origen == "Farenheit" and Destino == "Farenheit"):
            Resultado = Grados
        elif (Origen == "Kelvin" and Destino == "Celsius"):
            Resultado = (Grados - 273.15)
        elif (Origen == "Kelvin" and Destino == "Farenheit"):
            Resultado = (Grados - 273.15) * (9/5) + 32
        elif (Origen == "Kelvin" and Destino == "Kelvin"):
            Resultado = Grados
        else:
            print("Parámetros incorrectos")

        return Resultado
    
    def __Factorial(self, Numero):
        if(type(Numero) != int):
            return "EL número debe de ser entero"
    
        if(Numero < 0):
            return "El número debe de ser positivo"
    
        if(Numero <= 1):
            return 1
    
        Numero = Numero * self.__Factorial(Numero -1)
        return Numero