# %% [markdown]
# ## Entrada / Salida

# %% [markdown]
# 1) Crear un script con el nombre "clase09_ej1.py" que reciba 3 parametros a elección, verificando que sean exactamente esa cantidad, y muestre como salida los parámetros recibidos

# %% [markdown]
# 2) Crear un script con el nombre "clase09_ej2.py2" que reciba como un valor de temperatura en grados centígrados, un valor de humedad y por último si llovio (Con True o False). Y que cada vez que sea invocado, cargue en el archivo provisto "clase09_ej2.csv" una marca de tiempo y esa información.

# %% [markdown]
# Para trabajar con tipos de datos relacionados con la medición del tiempo, como ser fechas, horarios o marcas de tiempo se puede utilizar la clase *datetime*

# %%
import datetime

# %%
x = datetime.datetime.now()
print("Ahora =",x)
x = datetime.datetime(2020, 5, 10)
print("Fecha fija =",x)

# %%
fecha_hora = '2022-05-10 12:30:00'
objeto_datetime = datetime.datetime.strptime(fecha_hora, '%Y-%m-%d %H:%M:%S')
print("objeto datetime =", objeto_datetime)
marca_de_tiempo = datetime.datetime.timestamp(objeto_datetime)
print("timestamp =", marca_de_tiempo)
fecha_hora2 = datetime.datetime.fromtimestamp(marca_de_tiempo)
print("fecha hora =", fecha_hora2)

# %% [markdown]
# 3) Crear un archivo a partir de los datos presentes en el diccionario provisto. El cual debe contener en la primera fila el nombre de las claves y luego cada línea los elementos i-ésimos de las listas de valores contiguos y separados por coma ','. Este archivo debe llamarse clase09_ej3.csv

# %%
montañas = {'nombre':[  'Everest','K2','Kanchenjunga','Lhotse','Makalu',
                        'Cho Oyu','Dhaulagiri','Manaslu','Nanga Parbat','Annapurna I'],
            'orden':[1,2,3,4,5,6,7,8,9,10],
            'cordillera':['Himalaya','Karakórum','Himalaya','Himalaya','Himalaya'
                        ,'Himalaya','Himalaya','Himalaya','Karakórum','Himalaya'],
            'pais': ['Nepal','Pakistán','Nepal','Nepal','Nepal','Nepal','Nepal','Nepal',
                    'Pakistán','Nepal'],
            'altura':[8849,8611,8586,8516,8485,8188,8167,8163,8125,8091]}

# %%
import os
archivo = open('clase09_ej3.csv', 'w')

# %%
for clave in montañas.keys():
    if (clave == 'altura'):
        archivo.write(clave+'\n')
    else:
        archivo.write(clave+',')

# %%
ind = 0
while (ind < 10):
    archivo.write(montañas['nombre'][ind]+',')
    archivo.write(str(montañas['orden'][ind])+',')
    archivo.write(montañas['cordillera'][ind]+',')
    archivo.write(montañas['pais'][ind]+',')
    archivo.write(str(montañas['altura'][ind])+'\n')
    ind += 1

# %%
archivo.close()

# %% [markdown]
# 4) Mostrar el tamaño en MB del archivo generado en el punto 3

# %%
print('El archivo tiene un tamaño de', str(round(os.path.getsize('clase09_ej3.csv')/1024,2)),'MB')

# %% [markdown]
# 5) Crear una carpeta llamada clase09_montañas_altas

# %%
os.makedirs('clase09_montañas_altas')

# %% [markdown]
# 6) Copiar el archivo clase09_ej3.scv en la carpeta clase09_montañas_altas usando la sentencia **os.system**

# %%
os.system('copy clase09_ej3.csv clase09_montañas_altas')

# %% [markdown]
# 7) Listar el contenido de la carpeta clase09_montañas_altas

# %%
os.listdir('./clase09_montañas_altas')


