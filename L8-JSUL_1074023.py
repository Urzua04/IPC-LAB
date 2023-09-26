#Introducción a la programación, sección:17
#26/09/2023
#José Santiago Urzúa Luarca
#Objetivo: Crear un programa que determine calcule factorial y una secuencia Fibonacci
#Entrada: numero
""" PROCESO
1. Solicitar al usuario un número entero.
2. Mostrar los resultados.
"""
""" SALIDA
3. Menú
4. Calculo de factorial
5. Secuencia
"""
#Menú de opciones en ciclo
print("\n")
opcion = ""
contador = 1
while opcion != "3":
    print("Menú de opciones")
    print("1. Factorial")
    print("2. Secuencia de Fibonacci")
    print("3. Salir")
    
    opcion = input("Ingrese la opción que desea elegir: ")
    if opcion == "1":
        print("Selecciónó la opción 1\n")
        numero = int(input("Ingresa un número para calcular su factorial: "))
    
        if numero < 0:
            print("El factorial debe ser un número natural.")
        else:
            print("Vamos a mostrar el factorial de:", numero)
        contador = 1
        resultado = 1
        
        while contador <= numero:
            print(contador, end=" * ")
            resultado *= contador
            contador += 1
        
        print("\nEl factorial de", numero, "es:", resultado)

    """elif opcion == "2":
        print("Selecciónó la opción 2\n")
        numero = int(input("Ingresa un número que desea ver su secuencia fibonacci: "))

        if contador <= 0:
            return []
        elif contador == 1:
            return [0]
        elif contador == 2:
            return [0, 1]
        else:
            secuencia_fibonacci = [0, 1]
            a, b = 0, 1
            for _ in range(contador - 2):
                a, b = b, a + b
        secuencia_fibonacci = secuencia_fibonacci + [b]  
            return secuencia_fibonacci
secuencia_fibonacci = fibonacci(numero)
print("La secuencia de Fibonacci de", numero, "es:", secuencia_fibonacci)
"""

    






