from datetime import datetime
import statistics

class Tarea:
    # Funcion de inicializacion - metodo constructor
    def __init__(self, nombre, fechaLimite, categorias, horasDedicadas):
        self.nombre = nombre
        self.fechaLimite = fechaLimite
        self.categorias = categorias
        self.horasDedicadas = horasDedicadas

# funcion para agregar una tarea
def agregarTarea(listaTareas):
    nombre = input('Ingrese el nombre de la tarea: ')
    fechaLimite_str = input('Ingrese la fecha limite de la tarea (DD/MM/YY): ')
    try:
        fechaLimite = datetime.strptime(fechaLimite_str, '%d/%m/%Y')
    except ValueError:
        print('fecha no valida')
        return
    categorias = input('Ingrese la categoria de la tarea (Estudio, Personal, Trabajo, etc): ')
    horasDedicadas_str = input('Ingrese las horas dedicadas separadas en comas: ')
    try:
        horasDedicadas = list(map(float, horasDedicadas_str.split(',')))
    except ValueError:
        print('Horas no validas')
        return

    #crear un objeto y lo agrega a la lista de tareas
    tarea = Tarea(nombre, fechaLimite, categorias, horasDedicadas)
    listaTareas.append(tarea)
    print('Tarea agregada con exito....')

def visualizarTareas(listaTareas):
    if not listaTareas:
        print('No hay tareas registradas ')
        return

    for i, tarea in enumerate(listaTareas, start=1):
        print(f'\nTarea {i} ')
        print(f'Nombre: {tarea.nombre}')
        print(f'Fecha limite: {tarea.fechaLimite.strftime("%d/%m/%Y")}')
        print(f'Categoria: {tarea.categorias}')
        print(f'Horas dedicadas: {tarea.horasDedicadas}')

def analizarHoras(listaTareas):
    if not listaTareas:
        print('No hay tareas registradas ')
        return

    for tarea in listaTareas:
        promedio = statistics.mean(tarea.horasDedicadas)
        maximo = max(tarea.horasDedicadas)
        minimo = min(tarea.horasDedicadas)
        print(f'\nAnalisis de {tarea.nombre}')
        print(f'Promedio de horas {promedio}')
        print(f'Maximo de horas {maximo}')
        print(f'Minimo de horas {minimo}')

def generarInforme(listaTareas):
    if not listaTareas:
        print('No hay tareas registradas ')
        return

    # abrir un archivo txt para escribir un informe
    with open('informe_tareas.txt', 'w') as archivo:
        # escribir los detalles de la tarea en el archivo
        for tarea in listaTareas:
            archivo.write(f'Nombre: {tarea.nombre}\n')
            archivo.write(f'Fecha limite: {tarea.fechaLimite.strftime("%d/%m/%Y")}\n')
            archivo.write(f'Categoria: {tarea.categorias}\n')
            archivo.write(f'Horas dedicadas: {tarea.horasDedicadas}\n')
    print('Informe generado como "informe_tareas.txt"')

def menu():
    listaTareas = []
    while True:
        print('\nMenu de opciones')
        print('1. Agregar tarea')
        print('2. Visualizar tarea')
        print('3. Analizar horas dedicadas')
        print('4. Generar informe')
        print('5. Salir')

        opcion = int(input('Seleccione una opcion: '))

        if opcion == 1:
            agregarTarea(listaTareas)
        elif opcion == 2:
            visualizarTareas(listaTareas)
        elif opcion == 3:
            analizarHoras(listaTareas)
        elif opcion == 4:
            generarInforme(listaTareas)
        elif opcion == 5:
            print('Saliendo del programa...')
            break
        else:
            print('Opcion invalida')

if __name__ == '__main__':
    menu()





