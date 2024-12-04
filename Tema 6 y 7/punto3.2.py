# 2. Crear un diccionario vacío para almacenar la información de contacto
contactos = {}

# Solicitar al usuario que ingrese los datos
n = int(input("¿Cuántos contactos quieres ingresar? "))
for _ in range(n):
    nombre = input("Ingresa el nombre del contacto: ")
    correo = input(f"Ingresa el correo de {nombre}: ")
    contactos[nombre] = correo

# Mostrar las claves y valores del diccionario
print("\nInformación de contacto:")
for nombre, correo in contactos.items():
    print(f"{nombre}: {correo}")
