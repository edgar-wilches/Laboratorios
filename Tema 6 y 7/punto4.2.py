import random

def juego_adivinanza():
    print("¡Bienvenido al juego de adivinanza!")
    print("He elegido un número entre 1 y 100. ¿Puedes adivinar cuál es?")
    
    # Generar un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False
    
    while not adivinado:
        try:
            # Solicitar al usuario que introduzca un número
            intento = int(input("Introduce tu número: "))
            intentos += 1
            
            if intento < numero_secreto:
                print("El número es mayor. Intenta de nuevo.")
            elif intento > numero_secreto:
                print("El número es menor. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
                adivinado = True
        except ValueError:
            print("Por favor, introduce un número válido.")

# Ejecutar el juego
if __name__ == "__main__":
    juego_adivinanza()

#Este bloque se utiliza para determinar si el archivo Python se está ejecutando directamente como un programa principal o si está siendo importado como un módulo en otro programa.
