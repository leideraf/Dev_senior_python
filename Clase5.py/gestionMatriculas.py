estudiantes = []
cursos = ['Java', 'Python']
docentes = []
horarios = []

#Funciones para crear funciones
def matricularEstudiante():
    nombre = input('Digite el nombre del estudiante: ')
    print('Seleccione el curso a matricularse: ')
    for i, curso in enumerate(cursos):
        print(f'{i+1}: {curso}')

    cursoSeleccionado = int(input('Ingrese el numero del curso: '))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado-1]
        estudiante = {'nombre': nombre, 'curso': curso}
        estudiantes.append(estudiante)
        print(f'Estudiante: {nombre}, Matriculado en el curso: {curso}')
    else:
        print('Opcion de curso no valida ')

#Funcion para asignar un docente a un curso

def asignarDocente():
    print('Seleccione el curso al que desea asignarle el docente: ')
    for i, curso in enumerate(cursos):
        print(f'{i+1}: {curso}')

    cursoSeleccionado = int(input('Ingrese el numero del curso: '))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado-1]
        nombreDocente = input('Ingrese el nombre del docente: ')
        docente = {'nombre': nombreDocente, 'curso': curso}
        docentes.append(docente)
        print(f'Docente: {nombreDocente},  en el curso: {curso}')
    else:
        print('Opcion de curso no valida ')

#Funcion para asignar horario a un curso

def asignarHorario():
    print('Seleccione el curso al que desea asignarle el horario: ')
    for i, curso in enumerate(cursos):
        print(f'{i+1}: {curso}')

    cursoSeleccionado = int(input('Ingrese el numero del curso: '))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len(cursos):
        curso = cursos[cursoSeleccionado-1]
        dias = input('Ingrese los dias de clase (ej: martes y jueves): ')
        hora = input(' Ingrese la hora clase (ej: 6 pm): ')
        horario = {'curso': curso, 'dias': dias, 'hora': hora}
        horarios.append(horario)
        print(f'Horario asignado al curso: {curso}: {dias} a las {hora}')
    else:
        print('Opcion no valida')

def mostrarDocentes():
    if docentes:
        print('docentes de los cursos')
        for docente in docentes:
            print(f'docente: {docente['nombre']}, curso: {docente['curso']}')
    else:
        print('No hay docentes  asignados ')

def mostrarHorarios():
    if horarios:
        print('Horarios de los cursos')
        for horario in horarios:
            print(f'horario: {horario['nombre']}, curso: {horario['curso']}')
    else:
        print('No hay horarios  asignados ')

def mostrarEstudiantes():
    if estudiantes:
        print('estudiantes asignados a  cursos')
        for estudiante in estudiantes:
            print(f'Estudiante: {estudiante['nombre']}, curso: {estudiante['curso']}')
    else:
        print('No hay docentes  asignados ')

while True:
    print('\n sistema de matricula de Dev senior')
    print('1.  Matricular estudiante')
    print('2.  Asignar docente a curso')
    print('3.  Asignar horario a curso')
    print('4.  Mostrar la lista de estudiantes matriculados')
    print('5.  Mostrar la lista de docentes asignados')
    print('6.  Mostrar los horarios')
    print('7.  salir')

    opcion =int(input('digite la opcion: '))
    if opcion == 1:
        matricularEstudiante()
    elif opcion == 2:
        asignarDocente()
    elif opcion == 3:
        asignarHorario()
    elif opcion == 4:
        mostrarEstudiantes()
    elif opcion == 5:
        mostrarDocentes()
    elif opcion == 6:
        mostrarHorarios()
    elif opcion == 7:
        print(' Saliendo')
        break
    else:
        print('Opcion no valida')







