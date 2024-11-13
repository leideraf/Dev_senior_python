nombres = ['Leider', 'Manuela', 'Sebastian', 'Juan']

print(nombres) # imprimir toda la lista
print(nombres[1]) # imprimir la posicion 1
print(nombres[-1]) # imprimir el ultimo de la lista
print(nombres[:2]) # imprime desde la posicion  0  hasta la 2
print(len(nombres)) # nos da el total de valores de la lista
nombres.append('mariana') # Agregar un elemento al final de la lista
nombres.insert(1, 'Maria') # insertar a maria en la posicion 1
nombres.remove('Sebastian') # eliminar un nombre de la lista
nombres.pop() # elimina el ultimo elemento de la lista
del nombres[3] # elimina el valor en la posicion 3

print(nombres)

nombres.clear() # limpiar la lista
print(nombres)

del nombres # eliminar la lista