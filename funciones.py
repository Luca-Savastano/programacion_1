def cargar_matriz():
    matriz = []
    for i in range(11):
        print(f"\nJugador {i + 1}:")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        posicion = input("Posición: ")
        edad = input("Edad: ")
        goles = input("Goles: ")
        matriz.append([nombre, apellido, posicion, edad, goles])
    return matriz


def mostrar_matriz(matriz):
    print("\nEquipo titular:")
    print("Fila | Nombre | Apellido | Posición | Edad | Goles")
    print("-" * 50)
    for i in range(len(matriz)):
        jugador = matriz[i]
        print(f"{i:<4} | " + " | ".join(jugador))


def modificar_matriz(matriz):
    mostrar_matriz(matriz)
    fila = int(input("\nIngresá el número de fila (0 a 10): "))
    columna = int(input("Ingresá el número de columna (0 a 4): "))

    if 0 <= fila < len(matriz) and 0 <= columna < len(matriz[0]):
        nuevo_valor = input("Nuevo valor: ")
        matriz[fila][columna] = nuevo_valor
        print("Dato modificado con éxito.")
    else:
        print("Fila o columna fuera de rango.")
