'''
Este código crea una estructura de datos de listas anidadas y
demuestra cómo acceder a elementos específicos dentro de esas listas anidadas.
'''

# Se crea una lista vacía llamada listaDeListas.
listaDeListas = []
'''
Creación de listas individuales:
lista1 = ['X', ' ', 'O']: Se crea una lista llamada lista1 
que contiene tres elementos: 'X', ' ' (un espacio en blanco) y 'O'.
lista2 = [' ', 'X', 'O']: Se crea una lista llamada lista2 con los elementos ' ', 'X' y 'O'.
lista3 = [' ', ' ', 'X']: Se crea una lista llamada lista3 con los elementos ' ', ' ' y 'X'.
'''
lista1 = ['X', ' ', 'O']
lista2 = [' ', 'X', 'O']
lista3 = [' ', ' ', 'X']

# Adiciona las listas a la lista de listas:
listaDeListas.append(lista1)
listaDeListas.append(lista2)
listaDeListas.append(lista3)

# Se imprime la longitud de la lista principal:
print(len(listaDeListas))

# Se imprime la longitud de la primera lista interna:
print(len(listaDeListas[0]))

# Se accede al valor en la posición 1, 2
print("El elemento en la posición 1, 2 es:")
print(listaDeListas[1][2])
