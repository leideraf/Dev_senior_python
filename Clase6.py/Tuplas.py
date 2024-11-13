paises = ('Colombia', 'Mexico', 'Ecuador', 'Venezuela')

print(type(paises)) # saber el tipo de dato
print(paises)
print(len(paises))
print(paises[2])
print(paises[-1])

for pais in paises:
    print(pais)

paisesLista = list(paises) # convertir la tupla a una lista
paisesLista[1] ='Argentina'
paises = tuple(paisesLista) # convertir la lista en una tupla
print(paises)

del paises # eliminar la tupla
