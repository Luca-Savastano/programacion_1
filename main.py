from funciones import cargar_matriz, mostrar_matriz, modificar_matriz

matriz = []
opcion = ""
while opcion != "4":
    print("\n--- Menú Principal ---")
    print("1. Pedir datos para cargar la matriz")
    print("2. Mostrar matriz")
    print("3. Modificar matriz")
    print("4. Salir")

    opcion = input("Seleccioná una opción: ")

    if opcion == "1":
        matriz = cargar_matriz()
    elif opcion == "2":
        if len(matriz) > 0:
            mostrar_matriz(matriz)
        else:
            print("Primero tenés que cargar la matriz.")
    elif opcion == "3":
        if len(matriz) > 0:
            modificar_matriz(matriz)
        else:
            print("Primero tenés que cargar la matriz.")
    elif opcion == "4":
        print("¡Programa finalizado!")
    else:
        print("Opción inválida. Intentá de nuevo.")
