#Introducción a la programación - Sección:17
#Reposición de práctica del día martes 19/09/2023
#26/09/2023
#José Santiago Urzúa Luarca
#Objetivo:Crear un programa que ejecute cálculos matemáticos.
#Entrada: num1, num2, num3
""" PROCESO
1. El usuario proporcionará tres números enteros y el programa realizará las operaciones según jerarquía.
2. Se mostrarán los resultados obtenidos.
"""
""" SALIDA
3. Resultado 1
4. Resultado 2
5. Resultado 3
6. Resultado 4
"""
print ("Ejercicio 3: Jerarquia de operaciones")

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese el siguiente número: "))
num3 = int(input("Ingrese, el último número que desea ingresar en la operación: "))

print("\n", num1*num2+num3)
print("\n", num1*(num2+num3))
print("\n", (num1)/(num2*num3))
print("\n", (3*num1+2*num2)/(num3**2))

