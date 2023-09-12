#Introducción a la programación, sección:17
#12/09/2023
#José Santiago Urzúa Luarca
#Objetivo: Crear un programa que determine si un número ingresado es positivo, negativo o cero.
#Entrada: NumEntero
""" PROCESO
1. Solicitar al usuario un número entero.
2. Mostrar los resultados.
"""
""" SALIDA
3. El número ingresado es positivo, negativo o cero
4. El número ingresado negativo.
5. El número ingresado es cero.
"""
print("Ejercicio 1")

#Declarar variables y pedir datos:
NumEntero=int(input("Ingrese un número entero: "))

#Mostrar resultados evaluando si es positivo, negativo o cero:
if NumEntero > 0:
    print("El número que usted ha ingresado es positivo.")
elif NumEntero < 0:
    print("El número que usted ha ingresado es negativo.")
else:
    print("El número que usted ha ingresado es cero.")