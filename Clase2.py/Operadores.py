# Operadores aritméticos
a = 10
b = 3

suma = a + b         # Suma
resta = a - b        # Resta
multiplicacion = a * b  # Multiplicación
division = a / b     # División (resultado flotante)
division_entera = a // b  # División entera
modulo = a % b       # Residuo (módulo)
exponente = a ** b   # Exponenciación

print("Operadores aritméticos:")
print(f"Suma: {a} + {b} = {suma}")
print(f"Resta: {a} - {b} = {resta}")
print(f"Multiplicación: {a} * {b} = {multiplicacion}")
print(f"División: {a} / {b} = {division}")
print(f"División entera: {a} // {b} = {division_entera}")
print(f"Módulo: {a} % {b} = {modulo}")
print(f"Exponenciación: {a} ** {b} = {exponente}")
print()

# Operadores de comparación
igual = a == b       # Igualdad
diferente = a != b   # Diferencia
mayor = a > b        # Mayor que
menor = a < b        # Menor que
mayor_igual = a >= b # Mayor o igual que
menor_igual = a <= b # Menor o igual que

print("Operadores de comparación:")
print(f"¿{a} es igual a {b}? {igual}")
print(f"¿{a} es diferente de {b}? {diferente}")
print(f"¿{a} es mayor que {b}? {mayor}")
print(f"¿{a} es menor que {b}? {menor}")
print(f"¿{a} es mayor o igual que {b}? {mayor_igual}")
print(f"¿{a} es menor o igual que {b}? {menor_igual}")
print()

# Operadores lógicos
x = True
y = False

and_operador = x and y  # Operador AND
or_operador = x or y    # Operador OR
not_operador = not x    # Operador NOT

print("Operadores lógicos:")
print(f"{x} AND {y} = {and_operador}")
print(f"{x} OR {y} = {or_operador}")
print(f"NOT {x} = {not_operador}")
print()

# Operadores de asignación
c = 5
print(f"Valor inicial de c: {c}")

c += 2  # Asignación suma (equivalente a c = c + 2)
print(f"Después de c += 2: {c}")

c *= 3  # Asignación multiplicación (equivalente a c = c * 3)
print(f"Después de c *= 3: {c}")

c -= 1  # Asignación resta (equivalente a c = c - 1)
print(f"Después de c -= 1: {c}")

c /= 2  # Asignación división (equivalente a c = c / 2)
print(f"Después de c /= 2: {c}")

c %= 4  # Asignación módulo (equivalente a c = c % 4)
print(f"Después de c %= 4: {c}")
