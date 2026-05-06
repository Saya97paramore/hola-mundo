# Función para la suma
def sumar(a, b):
    return a + b

# Función para la resta
def restar(a, b):
    return a - b

# Función para la multiplicación
def multiplicar(a, b):
    return a * b

# Función para la división
def dividir(a, b):
    """
    Realiza la división de dos números.
    Maneja el caso de división por cero para evitar errores.
    """
    if b == 0:
        return "Error: No se puede dividir por cero"
    else:
       