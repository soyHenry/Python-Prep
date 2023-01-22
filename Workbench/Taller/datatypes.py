#On this file we going to learn about different data types
#Boolean, int, float, cmplex mumbers
#Boolean true or false
#String, list (dictionary
current_year=2023
print (current_year)
next_year=current_year+1
print (next_year)
print (type (current_year))
print(type (3.14))
print (type (1+2j))
print (type (9.81))
#a = input ("Ingresa un texto")
#print ("El texto ingresado es", a)
#converting data type e.g int to float o vs
print (int(9.81))
print (round (9.81))
#BOOLEAN CASES
enjoying_lesson=True
is_light_on=True
is_single=False
value = 3 < 2 #almacena el valor lógico de la expresión
print (value)
#STRINGS ==> Son datos almacenados del tipo cadena de texto
#Concatenación se suman las variables de texto
firstname = "Jota"
print (firstname) 
lastname="Cordova"
print (lastname)
print (firstname+" "+ lastname)
country = "Finland"
print (country)
#Recordar
fullname = firstname + " "+lastname
print (fullname,", aquí usamos la variable concatenada")
print (type (firstname))
print (country.upper()) #métodos de la clase print
print (fullname.title())
#LIST ==> It's a list of something, could be task, groceries
empty_list1 = list() #dos formas de inicializar listas
empty_list2 = []     #la nombro y luego declaro como list()
# la nombre y asigno una lista vacia con corchetes []
print (empty_list1, "esta es la lista 1")
print (empty_list2, "esta es la lista 2")
numbers = [1,2,3,4,5,6]
groceries = ["tomato", "carrot", "letuce"]
print (groceries [0])  #el puntero va con corchete y parte de 0
print (numbers [3])    #es una COLECCION 
print (len(groceries)) #conocer el largo de la la lista con len
mix_of_data_types_list = [1, "Jota", lastname, 2+5, 1-3j, 3.14]
#podemos almacenar un mix de datos
