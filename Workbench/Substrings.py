# Buscar una subcadena con index
import re
obj_iter="palabra"
varany  = int
pos_ini = int
pos_fin = int
obj_iter.sub[varany, pos_ini, pos_fin]) 
#es similar a find() pero en caso de que no se encuentre la subcadena sub lanza la excepción ValueError.
cadena = 'me gusta la mermelada'
cadena.index('lo')
#La cadena 'lo' no existe, por lo que provocará un error 
# Traceback (most recent call last):
#  File "<input>", line 1, in <module>
# ValueError: substring not found

cadena.index('la')
9
# Encontrar la última posición de una subcadena con RFIND
cadena = 'me gusta la mermelada'
cadena.rfind('la')
print (cadena.rfind('la'))
# 17
print (cadena.rfind('lo'))
# -1
# Encontrar la última posición de una subcadena con RINDEX
print (cadena.rindex('la'))
# 17
# print (cadena.rindex('lo'))
# Debe arrojar un error porque no existe la cadena (ValueError: substring not found)
