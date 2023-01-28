# 
# Ordenar una lista de coches almacenados como tuplas
#
tuplas_coches = [('Rojo', '4859-A', 'A'), ('Azul', '2901-Z', 'M'), ('Gris', '1892-B', 'M')
    ]
# Ordenar los coches por matrícula
ordenados = sorted(tuplas_coches, key=lambda coche : coche[1])
print (ordenados)
#[('Gris', '1892-B', 'M'), ('Azul', '2901-Z', 'M'), ('Rojo', '4859-A', 'A')]
# Ordenar una lista de coches almacenados como diccionarios
diccionarios_coches = [
        {'color': 'Rojo', 'matricula': '4859-A', 'cambio': 'A'},
        {'color': 'Azul', 'matricula': '2901-Z', 'cambio': 'M'},
        {'color': 'Gris', 'matricula': '1892-B', 'cambio': 'M'}
]
ordenados = sorted(diccionarios_coches, key=lambda coche : coche['matricula'])
print (ordenados)

#[{'color': 'Gris', 'matricula': '1892-B', 'cambio': 'M'}, {'color': 'Azul', 'matricula': '2901-Z', 'cambio': 'M'}, {'color': 'Rojo', 'matricula': '4859-A', 'cambio': 'A'}]