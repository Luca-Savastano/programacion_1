'''
La ferretería de Don Eusebio necesita un programa para calcular la comisión que debe pagar a cada uno de sus 3 empleados.

El programa debe:
    Pedir el nombre de cada empleado.
    Solicitar el monto total en pesos que cada empleado vendió en el día.
    Pedir el porcentaje de comisión que recibe cada empleado.
    Calcular y mostrar la comisión que cobrará cada uno.
    
Al finalizar, el programa debe mostrar:

    El total de dinero recaudado en el día.
    El total de comisiones pagadas.
    El dinero restante que le quedó a la ferretería.
    
Tiempo despues, Don Eusebio ha decidido cubrir parte del almuerzo de cada día. Modificar lo necesario para que también se
cumplan las siguientes consignas:

    Se debe ingresar el monto total del almuerzo.
    Cada empleado contribuirá con el 10% de su comisión.
    El resto lo pagará Don Eusebio.
    Mostrar cuánto debe abonar cada empleado y cuánto pagara Don Eusebio.
'''
nombre1 = input("Por favor, ingrese el nombre del primer empleado: ")
ventas1 = float (input ("Ingrese el monto diario que vendio en el dia: "))
comision1 = float(input(f"Ingrese el porcentaje de comision de {nombre1}: "))


nombre2 = input("\nIngrese el nombre del segundo empleado: ")
ventas2 = float(input(f"Ingrese el monto total vendido por {nombre2}: "))
comision2 = float(input(f"Ingrese el porcentaje de comision de {nombre2}: "))

nombre3 = input("\nIngrese el nombre del tercer empleado: ")
ventas3 = float(input(f"Ingrese el monto total vendido por {nombre3}: "))
comision3 = float(input(f"Ingrese el porcentaje de comision de {nombre3}: "))

pago1 = ventas1 * (comision1 /100)
pago2 = ventas2 * (comision2 /100)
pago3 = ventas3 * (comision3 /100)

print("La comision de {nombre1} es: ${pago1:}")
print("La comision de {nombre2} es: ${pago2:}")
print("La comision de {nombre3} es: ${pago3:}")

total_recaudado = ventas1 + ventas2 + ventas3
print ("El monto total recaudado en el dia es de: {total_recaudado}")

total_comisiones_pagadas = pago1 + pago2 + pago3
print ("El monto de comisiones pagadas es de: {total_comisiones_pagadas}")

dinero_restante = total_recaudado - total_comisiones_pagadas
print ("El dinero restante que le quedo a la ferreteria es de: {dinero_restante}")

total_almuerzo= float(input ("Ingrese la cantidad total del amuerzo: "))

aporte1 = pago1 * 0.10
aporte2 = pago2 * 0.10
aporte3 = pago3 * 0.10
total_aporte = aporte1 + aporte2+ aporte3

paga_eusebio = total_almuerzo - total_aporte

#comisiones
print("La comision de {nombre1} es: ${pago1:}")
print("La comision de {nombre2} es: ${pago2:}")
print("La comision de {nombre3} es: ${pago3:}")

#monto diario
print ("El monto total recaudado en el dia es de: {total_recaudado}")

#comisiones pagadas
print ("El monto de comisiones pagadas es de: {total_comisiones_pagadas}")

#dinero para ferreteria
print ("El dinero restante que le quedo a la ferreteria es de: {dinero_restante}")

#
print("{nombre1} debe aportar: ${aporte1:}")
print("{nombre2} debe aportar: ${aporte2:}")
print("{nombre3} debe aportar: ${aporte3:}")
print("Don Eusebio pagará: ${paga_eusebio:}") 