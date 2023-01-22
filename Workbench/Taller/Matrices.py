# Ejemplo 1
# Uso de 'enumerate' para recorrer matrices
m = [['enteros', 1, 2, 3, 4],           #Define una matriz 'm'
    ['complex', 1j, 2j, 3j, 4j],
    ['float', 1.0, 2.0, 3.0, 4.0]]
# [['enteros', 1, 2, 3, 4], ['complex', 1j, 2j, 3j, 4j], ['float', 1.0, 2.0, 3.0, 4.0]]
for i, elems in enumerate(m):
    for j, jelem in enumerate(elems):
        print(f'row {i} - column {j}: {jelem}')

"""
row 0 - column 0: enteros
row 0 - column 1: 1
row 0 - column 2: 2
row 0 - column 3: 3
row 0 - column 4: 4
row 1 - column 0: complex
row 1 - column 1: 1j
row 1 - column 2: 2j
row 1 - column 3: 3j
row 1 - column 4: 4j
row 2 - column 0: float
row 2 - column 1: 1.0
row 2 - column 2: 2.0
row 2 - column 3: 3.0
row 2 - column 4: 4.0
"""