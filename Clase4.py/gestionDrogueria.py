ventasTotales = 0.0

#Solicitar el numero de productos
numProductos = int(input('Ingrese el numero de productos a gestionar: '))

#Listas para almacenar la informacion
nombres = []
precios = []
cantidades = []

print('Ingreso inicial de productos a la tienda: ')

for i in range (numProductos):
    print(f'Producto {i+1}: ')
    nombre = input('Ingrese el nombre del producto: ').lower()
    nombres.append(nombre)
    precio = float(input('Digite el precio del producto: '))
    precios.append(precio)
    cantidad =int(input('Digite la cantidad del producto: '))
    cantidades.append(cantidad)

while True:
    print('\n-----MENU DE GESTION DROGUERIA------')
    print('1. Vender producto')
    print('2. Mostrar inventario')
    print('3. Mostrar ventas totales')
    print('4. Salir')

    opcion =int(input('Ingrese una opcion: '))

    if opcion == 1:
        print('\n Vender producto')
        nombreVenta = input('Ingrese el nombre del producto a vender: ').lower()
        cantidadVender = int(input('Ingrese la cantidad a vender: '))
        productoEncontrado = False

        for i in range(len(nombres)):
            if nombres [i] == nombreVenta:
                productoEncontrado = True
                if cantidadVender <= cantidades[i]:
                    totalVenta = cantidadVender * precios[i]
                    ventasTotales += totalVenta
                    cantidades[i] -= cantidadVender
                    print(f'Venta realizada. total de esta venta ${totalVenta:.2f}')
                    print(f'Quedan {cantidades[i]} unidades {nombres[i]} en el inventario ')
                else:
                    print('cantidad insuficiente en inventario')
                    breakE
        if not productoEncontrado:
            print('Producto no encontrado en el inventario')
    elif opcion == 2:
    
        print('\n Inventario de productos')
        for i in range(len(nombres)):
            print(f'Producto {i+1}: {nombres[i].capitalize()}, Precio: {precios[i]:.2f}, cantidad: {cantidades[i]}')
    
    elif opcion == 3:
        print(f'\n Ventas totales acumuladas: 4{ventasTotales:.2f}')
    elif opcion == 4:
        print('\n Gracia por usar el siatema')
        break
    else:
        print('\n opcion invalida')





