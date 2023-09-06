#Introducción a programación - Sección:17
#05/09/2023
#José Santiago Urzúa Luarca
#Objetivo: Crear un programa que realice las operaciones aritméticas básicas.
#Entrada: Número 1, Número 2
""" PROCESO
1. Solicitar al usuario dos numeros enteros y realizar los cálculos de suma, resta, multiplicación y división
2. Mostrar los resultados.
"""
""" SALIDA
3. Resultado de suma
4. Resultado de resta
5. Resultado de multiplicación
6. Resultado de división
"""
#Declarar variables
N1=0
N2=0

#Pedir datos
N1=int(input("Ingrese el número 1:"))
N2=int(input("Ingrese el número 2:"))

#Operaciones y resultados
Suma=N1+N2
Resta=N1-N2
Multiplicación=N1*N2
División=N1/N2

#Mostrar resultados
print("Al sumar los números se obtiene:",Suma)
print("Al restar los números se obtiene:",Resta)
print("Al multiplicar los números se obtiene:",Multiplicación)
print("Al dividir los números se obtiene:",División)