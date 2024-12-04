# 1. Crear una lista vacía para almacenar los nombres de estudiantes
estudiantes = []

# Solicitar al usuario que ingrese los nombres de los estudiantes
n = int(input("¿Cuántos estudiantes quieres ingresar? "))
for _ in range(n):
    nombre = input("Ingresa el nombre del estudiante: ")
    estudiantes.append(nombre)

# Mostrar los nombres de los estudiantes usando un bucle
print("\nLista de estudiantes:")
for estudiante in estudiantes:
    print(estudiante)


