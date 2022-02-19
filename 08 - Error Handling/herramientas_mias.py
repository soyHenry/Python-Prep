class calculador:
    '''
    Esta clase toma las funciones de ejercicios anteriores para utilizarlas en metodos, toma una lista
    '''
    def __init__(self, lista):
        if type(lista) != list:
                raise ValueError('El objeto solo se puede crear con una lista como parametro')
        else:
            for a in lista:
                if type(a) != int:
                    raise ValueError('La lista solo puede tener enteros')    
        self.lista = lista
    
    def es_primo(self):
        lista_primos = []
        for x in self.lista:
            lista_primos.append(self.__es_primo(x))
        return lista_primos

    def __es_primo(self, x):
        self.x = x
        if x == 1 or x == 0:
            return False
        primo = True
        j = 2
        while j < x:
            if x % j == 0:
                return False
            j += 1
        return primo

    def moda(self, max_rep):
        if max_rep == 'maximo':
            max_rep = True
        elif(max_rep == 'minimo'):
            max_rep = False
        lista_cont = {}
        for x in self.lista:
            n = 0
            for y in self.lista:
                if y == x:
                    n+=1
                lista_cont[x] = n

        for x in self.lista:
            if lista_cont[x] == 1:
                del lista_cont[x]
    
        if max_rep:
            return ((max(lista_cont, key=lista_cont.get),max(lista_cont.values())))
        else:
            return ((min(lista_cont, key=lista_cont.get),min(lista_cont.values())))
    
    def tempconv(self,o,d):
        conversion = []
        if o not in ['Celsius','Farenheit','Kelvin'] or d not in ['Celsius','Farenheit','Kelvin']:
                raise ValueError("Los parametros admitidos para convertir grados son ['Celsius','Farenheit','Kelvin']")
        else:
            for x in self.lista:          
                conversion.append(self.__tempconv(x,o,d))
        return conversion

    def __tempconv(self,valor,origen,destino):
        self.valor = valor
        self.origen = origen
        self.destino = destino
        if origen == destino:
            raise ValueError("Los parametros admitidos para convertir grados son ['Celsius','Farenheit','Kelvin'] y debe ser distinto el parametro de origen y destino")
        if origen == "Celsius":
            if destino == "Farenheit":
                temp = (valor * 9/5) + 32
            if destino == "Kelvin":
                temp = valor + 273.15
        if origen == "Farenheit":
            if destino == "Celsius":
                temp = (valor - 32) * 5/9
            if destino == "Kelvin":
                temp = (valor - 32) * 5/9 + 273.15
        if origen == "Kelvin":
            if destino == "Celsius":
                temp = valor - 273.15
            if destino == "Farenheit":
                temp = (valor - 273.15) * 9/5 + 32
        return temp

    def factorial(self):
        resultado = []
        for n in self.lista:
            resultado.append(self.__factorial(n))
        return resultado
        

    def __factorial(self, n):
        self.n = n
        if n < 0 or type(n) is not int:
            raise ValueError("Esta funcion solo calcula factoriales de enteros popstivos")
        if n == 1:
            return 1
        else:
            fact = n * self.__factorial(n-1)
        return fact