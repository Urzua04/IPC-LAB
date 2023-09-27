#Introducción a la programación - Sección:17
#Reposición de práctica del día martes 19/09/2023
#26/09/2023
#José Santiago Urzúa Luarca
#Objetivo:Crear un programa que ejecute cálculos matemáticos.
#Entrada: Numero1, Numero2.
""" PROCESO
1. El usuario proporcionará dos números enteros y el programa realizará las operaciones de suma, resta, multiplicación y división.
2. Se mostrarán los resultados obtenidos
"""
""" SALIDA
3. Resultado suma
4. Resultado resta
5. Resultado multiplicacion
6. Resultado division
7. El usuario tiene la opción de realizar otra operación o finalizar el programa.
"""
while True:
    print ("Ejercicio 1: Operaciones aritmeticas")
    Numero1=int(input("Ingrese un número: "))
    Numero2=int(input("Ingrese un número: "))

    print(Numero1,"+", Numero2,"=", Numero1+Numero2)
    print(Numero1,"-", Numero2,"=", Numero1-Numero2)
    print(Numero1,"*", Numero2,"=", Numero1*Numero2)
    print(Numero1,"/", Numero2,"=", Numero1/Numero2)
    print(Numero1,"^", Numero2,"=", Numero1**Numero2)
    print(Numero1,"//", Numero2,"=", Numero1//Numero2)
        
    ingrese = input("¿Desea realizar una nueva operación? (Ingrese 'salir' para finalizar): ")
    if ingrese == "salir":
       break
