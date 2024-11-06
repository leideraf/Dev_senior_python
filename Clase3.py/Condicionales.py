age = int(input('Escribe tu edad: '))
country = 'COL'

if age >= 21:
    print("Puedes comprar alcohol en USA")
elif age >= 18:
    print('Puedes comprar alcohol en COL')
elif age >= 16:
    print('Puedes comprar alcohol en GER')
else:
    print('No puedes comprar alcohol')
