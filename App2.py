class EstructuraPorFilas:
    def __init__(self):
        self.matriz = []

    def agregar_fila(self, fila):
        """Agrega una nueva fila a la matriz."""
        self.matriz.append(fila)
        print(f"Fila {fila} agregada.")

    def eliminar_fila(self, indice):
        """Elimina una fila de la matriz dado su índice."""
        if 0 <= indice < len(self.matriz):
            fila_eliminada = self.matriz.pop(indice)
            print(f"Fila {fila_eliminada} eliminada.")
        else:
            print("Índice fuera de rango.")

    def mostrar_filas(self):
        """Muestra todas las filas de la matriz."""
        print("Matriz actual:")
        for i, fila in enumerate(self.matriz):
            print(f"Fila {i}: {fila}")

    def obtener_fila(self, indice):
        """Obtiene una fila específica dado su índice."""
        if 0 <= indice < len(self.matriz):
            return self.matriz[indice]
        else:
            print("Índice fuera de rango.")
            return None

# Ejemplo de uso
estructura = EstructuraPorFilas()

# Agregar filas
estructura.agregar_fila([1, 2, 3])
estructura.agregar_fila([4, 5, 6])
estructura.agregar_fila([7, 8, 9])

# Mostrar filas
estructura.mostrar_filas()

# Obtener una fila específica
fila = estructura.obtener_fila(1)
print(f"Fila obtenida: {fila}")

# Eliminar una fila
estructura.eliminar_fila(0)

# Mostrar filas actualizadas
estructura.mostrar_filas()
