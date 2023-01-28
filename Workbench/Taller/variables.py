#Variables
#It's a memory location to assign data to store and use it later
a=10
b=3
print (a)

print ("what's the value of a", a)
print ("what's the value of b", b)
print (a+b)
total =2+4
print (total)
# Ejemplo 10 - SWAP de variable - Deben ser del mismo tipo (INT)
# caso 1) Creamos una Función

def swap(a,b):
	c=a
	a=b
	b=c
	return a,b

x = 5
y = 4
print (x,y)
x,y= swap(x,y)
print (x,y)
print ()

# caso 2) Directo y,x = x,y, propiedades de Python
#  
x=10
y=20
print (x,y)
x,y=y,x
print (x,y)