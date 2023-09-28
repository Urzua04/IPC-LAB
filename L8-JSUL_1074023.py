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
5. Secuencia Fibonacci
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
        print()

    elif opcion == "2":
        print("Selecciónó la opción 2\n")
        numero = int(input("Ingresa un número que desea ver su secuencia fibonacci: "))
        

        if numero <= 0:
            print("error")
        elif numero == 1:
            print("0")
        elif numero == 2:
            print("0,1")
        else:
            c = 3
            n1=0
            n2=1
            texto= str(n1)+","+str(n2)+","
            n3=0
            while c <= numero:
                n3 = n1 + n2
                texto += str(n3) + ","
                n1=n2
                n2=n3
                c += 1
            
            print("La secuencia de Fibonacci de ", numero, " es: ", texto)
            print()
    elif opcion == "3":
        print("¡Gracias por utilizar el menú!..")
        break
    else:
        print("Opción no válida")
    
