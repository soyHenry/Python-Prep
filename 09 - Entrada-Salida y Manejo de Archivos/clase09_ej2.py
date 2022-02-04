import sys
# Comprobación de seguridad, ejecutar sólo si se recibe 3 argumentos
if len(sys.argv) == 4:
    import datetime
    import os
    marca_de_tiempo = datetime.datetime.now()
    marca_de_tiempo = datetime.datetime.timestamp(marca_de_tiempo)

    temperatura = sys.argv[1]
    humedad = sys.argv[2]
    lluvia = sys.argv[3]
    linea = str(marca_de_tiempo) + ',' + temperatura + ',' + humedad + ',' + lluvia

    logs_lluvia = open('clase09_ej2.csv', 'a')
    logs_lluvia.write(linea+'\n')
    logs_lluvia.close()

else:
    print("ERROR: Introdujo una cantidad de argumentos distinta de tres (3)")
    print('Ejemplo: clase09_ej1.py <temperatura> <humedad> <True o False>')