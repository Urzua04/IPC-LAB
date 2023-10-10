#Introducción a la programación, sección:17
#10/10/2023
#José Santiago Urzúa Luarca
#Objetivo: Crear un módulo con las funciones necesarias para convertir una cantidad expresada en cm a m, km, in y ft.
#Entrada: conversiones

def cmAm(centimetros):
    metros = centimetros / 100
    return metros

def cmAkm(centimetros):
    kilometros = centimetros / 100000
    return kilometros

def cmAin(centimetros):
    pulgadas = centimetros / 2.54
    return pulgadas

def cmAft(centimetros):
    pies = centimetros / 30.48
    return pies
