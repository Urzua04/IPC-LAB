#Introducción a la programación, sección:17
#12/09/2023
#José Santiago Urzúa Luarca
#Objetivo: Crear un programa que determine día de la semana según numero ingresado.
#Entrada: NumEntero
""" PROCESO
1. Solicitar al usuario un número entero.
2. Mostrar los resultados.
"""
""" SALIDA
3. El día de la semana según número ingresado.
"""
print("Ejercicio 2")

#Declarar variables y pedir datos:
NumEntero = int(input("Ingrese un número entero equivalente a un dia de la semana: "))

#Mostrar resultados evaluando el día de la semana:
if  NumEntero <= 0 or NumEntero > 7:
    print("Error. El número a ingresar debe estar contenido entre 1 y 7.")
elif NumEntero == 1:
    print("Día: lunes")
elif NumEntero == 2:
    print("Día: martes")
elif NumEntero == 3:
    print("Día: miércoles")
elif NumEntero == 4:
    print("Día: jueves")
elif NumEntero == 5:
    print("Día: viernes")
elif NumEntero == 6:
    print("Día: sábado")
elif NumEntero == 7:
    print("Día: domingo")
