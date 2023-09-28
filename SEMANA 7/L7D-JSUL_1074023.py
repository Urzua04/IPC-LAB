#Introducción a la programación - Sección:17
#Reposición de práctica del día martes 19/09/2023
#26/09/2023
#José Santiago Urzúa Luarca
#Objetivo:Crear un programa que ejecute el cálculo de una ecuación cuadrática por medio de la fórmula.
#Entrada: numa, numb, numc
""" PROCESO
1. El usuario proporcionará tres números (coeficientes de las variables de su ecuación cuadrática) y el programa realizará las operaciones según jerarquía.
2. Se mostrarán los resultados obtenidos.
"""
""" SALIDA
3. Resultado 1
4. Resultado 2
"""
print ("Ejercicio 4: Jerarquia de operaciones para resulver una ecuación cuadrática")

while True:
    print("Menú:")
    print("1. Calcular expresión cuadrática")
    print("2. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        coea = float(input("Ingrese coeficiente a: "))
        coeb = float(input("Ingrese coeficiente b: "))
        coec = float(input("Ingrese coeficiente c: "))

        if coea == 0:
            print("\nError: 'a' no puede ser igual a 0.")
        else:
            discriminante = coeb ** 2 - 4 * coea * coec

            if discriminante < 0:
                print("\nError: El discriminante debe ser positivo para calcular la raíz cuadrada.")
            else:
                resultado1 = (-coeb + (discriminante ** 0.5)) / (2 * coea)
                resultado2 = (-coeb - (discriminante ** 0.5)) / (2 * coea)
                print("\nResultado 1:", resultado1)
                print("Resultado 2:", resultado2)
    elif opcion == '2':
        print("Apagar")
        break
    else:
        print("Opción no válida. Seleccione una opción del menú.")
