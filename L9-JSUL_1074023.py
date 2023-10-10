#Introducción a la programación, sección:17
#10/10/2023
#José Santiago Urzúa Luarca
# Objetivo: Convertir una cantidad en centímetros a metros, kilómetros, pulgadas o pies según la elección del usuario.
# Entrada: Menú de opciones.

"""
PROCESO:
1. Mostrar menú de opciones que incluye las conversiones disponibles.
2. Solicitar al usuario que elija una opción del menú.
3. Si la opción es válida:
   a. Solicitar al usuario la cantidad en centímetros a convertir.
   b. Realizar la conversión utilizando las funciones del módulo CONVERSIONES.
   c. Mostrar el resultado de la conversión.
4. Si la opción es "5", salir del programa.
5. Si la opción no es válida, mostrar un mensaje de error.
6. Repetir el proceso hasta que el usuario elija salir.

SALIDA:
- Mostrar la cantidad en centímetros ingresada por el usuario y el resultado de la conversión en la unidad correspondiente.
"""

import CONVERSIONES

opcion = ""
while opcion != "5":
    print("\nBienvenido al menú de opciones para convertir de cm a cuatro distintas unidades...")
    print("1. Centímetros a metros")
    print("2. Centímetros a kilómetros")
    print("3. Centímetros a pulgadas")
    print("4. Centímetros a pies")
    print("5. Salir\n")
    
    opcion = input("Ingrese la opción que desea elegir: ")
    
    if opcion == "1":
        print("\nHa seleccionado la opción 1: Centímetros a metros")
        cm = float(input("Ingrese la cantidad en centímetros para convertir: "))   
        metros = CONVERSIONES.cmAm(cm)
        if round(metros) == 1:
            print(cm, "centímetro equivale a", round(metros), "metro\n")
        else:
            print(cm, "centímetros equivalen a", round(metros), "metros\n")
    elif opcion == "2":
        print("\nHa seleccionado la opción 2: Centímetros a kilómetros")
        cm = float(input("Ingrese la cantidad en centímetros para convertir: "))   
        kmetros = CONVERSIONES.cmAkm(cm)
        if round(kmetros) == 1:
            print(cm, "centímetro equivale a", round(kmetros), "kilómetro\n")
        else:
            print(cm, "centímetros equivalen a", round(kmetros), "kilómetros\n")
    elif opcion == "3":
        print("\nHa seleccionado la opción 3: Centímetros a pulgadas")
        cm = float(input("Ingrese la cantidad en centímetros para convertir: "))   
        pulg = CONVERSIONES.cmAin(cm)
        if round(pulg) == 1:
            print(cm, "centímetro equivale a", round(pulg), "pulgada\n")
        else:
            print(cm, "centímetros equivalen a", round(pulg), "pulgadas\n")
    elif opcion == "4":
        print("\nHa seleccionado la opción 4: Centímetros a pies")
        cm = float(input("Ingrese la cantidad en centímetros para convertir: "))   
        pies = CONVERSIONES.cmAft(cm)
        if round(pies) == 1:
            print(cm, "centímetro equivale a", round(pies), "pie\n")
        else:
            print(cm, "centímetros equivalen a", round(pies), "pies\n")
    elif opcion == "5":
        print("Gracias por utilizar nuestro servicio\nSaliendo del programa...")
    else:
        print("Opción no válida. Por favor, ingrese una opción válida (1-5).")
