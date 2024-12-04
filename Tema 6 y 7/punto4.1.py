def calculadora():
    print("Bienvenido a la calculadora básica")
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    while True:
        try:
            opcion = int(input("\nIngresa el número de la operación que deseas realizar (1-5): "))
            if opcion == 5:
                print("Gracias por usar la calculadora. ¡Adiós!")
                break
            elif opcion in [1, 2, 3, 4]:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))

                if opcion == 1:
                    print(f"El resultado de {num1} + {num2} es: {num1 + num2}")
                elif opcion == 2:
                    print(f"El resultado de {num1} - {num2} es: {num1 - num2}")
                elif opcion == 3:
                    print(f"El resultado de {num1} * {num2} es: {num1 * num2}")
                elif opcion == 4:
                    if num2 != 0:
                        print(f"El resultado de {num1} / {num2} es: {num1 / num2}")
                    else:
                        print("Error: No se puede dividir entre cero.")
            else:
                print("Opción no válida. Por favor, selecciona un número entre 1 y 5.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

# Llamar a la función para iniciar la calculadora
calculadora()
