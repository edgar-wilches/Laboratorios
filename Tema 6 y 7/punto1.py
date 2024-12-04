# Imprimir un mensaje en la consola
print("¡Bienvenido al programa!")

# Declarar variables de diferentes tipos y pedir al usuario que ingrese los valores
entero = int(input("Ingresa un número entero: "))
decimal = float(input("Ingresa un número decimal: "))
texto = input("Ingresa un texto: ")

# Realizar operaciones matemáticas simples
suma = entero + decimal
resta = entero - decimal
multiplicacion = entero * decimal
division = entero / decimal if decimal != 0 else "No se puede dividir por cero"

# Concatenar cadenas de texto
mensaje = f"El número entero es {entero}, el número decimal es {decimal} y el texto ingresado es: {texto}"

# Imprimir los resultados
print("\nOperaciones matemáticas:")
print(f"Suma (entero + decimal): {suma}")
print(f"Resta (entero - decimal): {resta}")
print(f"Multiplicación (entero * decimal): {multiplicacion}")
print(f"División (entero / decimal): {division}")

# Imprimir el mensaje concatenado
print("\n" + mensaje)
