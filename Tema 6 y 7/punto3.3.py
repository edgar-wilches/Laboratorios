# 3. Función para agregar un nuevo estudiante a la lista
def agregar_estudiante(estudiantes):
    nombre = input("Ingresa el nombre del estudiante a agregar: ")
    estudiantes.append(nombre)

# Función para agregar o actualizar un contacto en el diccionario
def agregar_o_actualizar_contacto(contactos):
    nombre = input("Ingresa el nombre del contacto: ")
    correo = input(f"Ingresa el correo de {nombre}: ")
    contactos[nombre] = correo

# Menú para elegir qué acción realizar
def menu():
    estudiantes = []
    contactos = {}
    
    while True:
        print("\nMenú:")
        print("1. Agregar estudiante a la lista")
        print("2. Agregar/Actualizar contacto")
        print("3. Mostrar lista de estudiantes")
        print("4. Mostrar contactos")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            agregar_estudiante(estudiantes)
        elif opcion == "2":
            agregar_o_actualizar_contacto(contactos)
        elif opcion == "3":
            print("\nLista de estudiantes:")
            for estudiante in estudiantes:
                print(estudiante)
        elif opcion == "4":
            print("\nInformación de contacto:")
            for nombre, correo in contactos.items():
                print(f"{nombre}: {correo}")
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, por favor ingresa una opción correcta.")

# Llamar al menú para empezar el script
menu()
