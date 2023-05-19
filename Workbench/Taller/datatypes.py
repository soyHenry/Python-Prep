
# On this file we going to learn about different data types
# Boolean, int, float, complex mumbers
# Boolean true or false
# String, list (dictionary)

current_year=2023
print (current_year)
next_year=current_year+1
print (next_year)
print (type (current_year))
print(type (3.14))
print (type (1+2j))
print (type (9.81))
a = input ("Ingresa un texto")
print ("El texto ingresado es", a)
# Convertir data type e.g int to float o viceversa
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