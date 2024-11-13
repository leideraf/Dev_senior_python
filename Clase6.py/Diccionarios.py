conceptosProgramacion ={
    'POO': 'Programacion orientada a objetos',
    'IDE': 'Entorno de desarrollo integrado',
    'DBMS': 'Sistema de gestion de bases de datos'

}

print(conceptosProgramacion)
print(len(conceptosProgramacion))

print(conceptosProgramacion['IDE'])

print(conceptosProgramacion.get('POO'))

conceptosProgramacion['DBMS'] = 'Database Managment System'
print(conceptosProgramacion)

for key in conceptosProgramacion: # imprime las llaves
    print(key)

for key, value in conceptosProgramacion.items(): # imprime las llaves con los valores
    print(key, value)

