#Introducción a la programación - Sección:17
#Reposición de práctica del día martes 19/09/2023
#26/09/2023
#José Santiago Urzúa Luarca
#Objetivo:Crear un programa que ejecute cálculos matemáticos por medio de un menú de opciones.
#Entrada: Numero1, Numero2.
""" PROCESO
1. El usuario eligrirá la opción y proporcionará dos números enteros y el programa realizará la operación correspondiente.
2. Se mostrarán los resultados obtenidos
"""
""" SALIDA
3. Resultado suma
4. Resultado resta
5. Resultado multiplicacion
6. Resultado division
7. El usuario tiene la opción de realizar otra operación o finalizar el programa.
"""
print ("Ejercicio 2: Operaciones aritmeticas")
while True:

    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Cociente")
    print("7. Salir")

    opcion = input("Ingrese el número de la operación que desea realizar: ")

    if opcion == '7':
        print("¡Gracias, hasta la próxima!")
        break
    elif opcion in ('1', '2', '3', '4', '5', '6'):
        Numero1 = int(input("Ingrese el primer número: "))
        Numero2 = int(input("Ingrese el segundo número: "))

        if opcion == '1':
            print(Numero1, "+", Numero2, "=", Numero1 + Numero2)
        elif opcion == '2':
            print(Numero1, "-", Numero2, "=", Numero1 - Numero2)
        elif opcion == '3':
            print(Numero1, "*", Numero2, "=", Numero1 * Numero2)
        elif opcion == '4':
            if Numero2 != 0:
                print(Numero1, "/", Numero2, "=", Numero1 / Numero2)
            else:
                print("No es posible dividir entre cero.")
        elif opcion == '5':
            print(Numero1, "^", Numero2, "=", Numero1 ** Numero2)
        elif opcion == '6':
            if Numero2 != 0:
                print(Numero1, "//", Numero2, "=", Numero1 // Numero2)
            else:
                print("No es posible calcular el cociente con denominador cero.")
        
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 7.")
        
    ingrese = input("¿Desea realizar una nueva operación? (Ingrese 'salir' para finalizar): ")
    if ingrese == "salir":
        print("¡Gracias, hasta la próxima!")
        break
