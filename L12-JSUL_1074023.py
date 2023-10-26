# Introducción a la programación - Sección:17
# 25/10/2023
# José Santiago Urzúa Luarca
# Objetivo: Crear un programa que administre una lista de contactos.
""" PROCESO
Entrada:
# 1. El usuario ingresa la cantidad de contactos que desea agregar.
# 2. Para cada contacto:
#    - El usuario ingresa el nombre del contacto.
#    - El usuario ingresa el número de teléfono del contacto.
#    - El usuario puede ingresar un nuevo contacto y eliminar un contacto existente.
#    - El usuario puede ingresar un nuevo contacto en mayúsculas y en una posición específica.

# Salida:
# 1. Se muestra la lista de contactos completa.
# 2. El usuario puede eliminar un contacto por nombre.
# 3. Se muestra la lista de contactos actualizada.
# 4. Se muestra la lista de contactos ordenada alfabéticamente por nombre.
# 5. El usuario puede ingresar un nuevo contacto en mayúsculas.
# 6. El usuario puede ingresar un nuevo contacto en una posición específica.
# 7. Se muestra la lista de contactos completa.
# 8. Se crea una copia de la lista original y se muestra ordenada de forma descendente.
# 9. Se muestra la lista de contactos original para confirmar que no ha cambiado.
"""
contactos = []

n = int(input("Para iniciar con su lista de contactos, por favor, ingrese la cantidad de contactos que desea agregar: "))

for i in range(n):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono del contacto: ")
    contacto = [nombre, numero]
    contactos.append(contacto)

print("\nLista de contactos completa:")
for contacto in contactos:
    print(f"Nombre: {contacto[0]}, Teléfono: {contacto[1]}")

nombreEliminar = input("\nLocalice e ingrese el nombre del contacto que desea eliminar: ")
for contacto in contactos:
    if contacto[0] == nombreEliminar:
        contactos.remove(contacto)
        break

print("\nLista de contactos actualizada:")
for contacto in contactos:
    print(f"Nombre: {contacto[0]}, Teléfono: {contacto[1]}")

contactos.sort()

print("\nLista de contactos ordenada alfabéticamente:")
for contacto in contactos:
    print(f"Nombre: {contacto[0]}, Teléfono: {contacto[1]}")

nombreMayusculas = input("\nIngrese el nombre del nuevo contacto que será almacenado en mayúsculas: ").upper()
numero = input("Ingrese el número de teléfono del nuevo contacto: ")
contactoNuevo = [nombreMayusculas, numero]
contactos.append(contactoNuevo)

posicion = int(input("\nIngrese la posición donde desea guardar un contacto extra: "))
nombreNuevo = input("Ingrese el nombre del nuevo contacto: ")
numeroNuevo = input("Ingrese el número de teléfono del nuevo contacto: ")
contactoNuevo = [nombreNuevo, numeroNuevo]
contactos.insert(posicion, contactoNuevo)

print("\nLista de contactos completa:")
for contacto in contactos:
    print(f"Nombre: {contacto[0]}, Teléfono: {contacto[1]}")

contactosCopia = contactos.copy()
contactosCopia.sort(reverse=True)

contactosCopia = contactos.copy()
contactosCopia.sort(reverse=True)

print("\nLista ordenada de forma descendente:")
for contacto in contactosCopia:
    print(f"Nombre: {contacto[0]}, Teléfono: {contacto[1]}")

print("\nLista de contactos original:")
for contacto in contactos:
    print(f"Nombre: {contacto[0]}, Teléfono: {contacto[1]}")
