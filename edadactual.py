#Crear una función llamada calcular_edad(anio_nacimiento) que reciba el año de nacimiento y devuelva la edad actual (sin considerar el mes de nacimiento)
#Luego, el programa debe pedir el año de nacimiento del usuario y mostrar la edad calculada.


def calcular_Edad (año_actual, año_nacimiento):
    edad = año_actual - año_nacimiento
    return edad

año_nacimiento = int (input ("Ingrese el año de nacimiento: "))
año_actual = 2025

edad= calcular_Edad(año_actual, año_nacimiento)

print (f"Tenes {edad} años ")