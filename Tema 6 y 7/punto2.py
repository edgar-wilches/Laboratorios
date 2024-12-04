# Solicitar un número al usuario y determinar si es par o impar
numero = int(input("Introduce un número: "))

if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

# Solicitar al usuario una lista de números separados por espacios
entrada = input("Introduce una lista de números separados por espacios: ")
numeros = [int(x) for x in entrada.split()]

# Iterar sobre la lista de números e imprimir sus cuadrados
print("Los cuadrados de los números son:")
for num in numeros:
    print(f"El cuadrado de {num} es {num ** 2}")

# Usar un bucle while para pedir un número y asegurarse de que esté en un rango específico
while True:
    numero_while = int(input("Introduce un número entre 1 y 10: "))
    if 1 <= numero_while <= 10:
        print(f"El número {numero_while} está dentro del rango.")
        break
    else:
        print("Número fuera de rango. Inténtalo de nuevo.")
