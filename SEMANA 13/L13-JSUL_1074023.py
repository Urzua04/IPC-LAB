# Introducción a la programación, sección:17
# 31/10/2023
# José Santiago Urzúa Luarca
# Objetivo:  recopilar información personal de una persona, calcular su edad y mostrar su fecha de nacimiento 
# en un formato específico, además de indicar si está casada y, en caso afirmativo, mostrar su apellido de casada precedido por "De".
#Entrada: información personal
import datetime

# Define la clase Persona
class Persona:
    def __init__(self):
        self.nombres = ""
        self.apellidos = ""
        self.apellido_casada = ""
        self.fecha_nacimiento = None

    def insertar_nombres(self, nombres):
        self.nombres = nombres

    def insertar_apellidos(self, apellidos):
        self.apellidos = apellidos

    def insertar_apellido_casada(self, apellido_casada):
        self.apellido_casada = apellido_casada

    def insertar_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def obtener_nombres(self):
        return self.nombres

    def obtener_apellidos(self):
        return self.apellidos

    def obtener_apellido_casada(self):
        return self.apellido_casada

    def obtener_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def calcular_edad(self):
        hoy = datetime.date.today()
        edad = hoy.year - self.fecha_nacimiento.year - ((hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        return edad

# Función principal para interactuar con el usuario
def main():
    persona = Persona()

    # Solicitar al usuario que ingrese los datos
    nombres = input("Ingresa los nombres de la persona: ")
    apellidos = input("Ingresa los apellidos de la persona: ")
    apellido_casada = input("Ingresa el apellido de casada (si aplica): ")
    fecha_nacimiento_str = input("Ingresa la fecha de nacimiento (formato: DD-MM-YYYY): ")

    # Asignar los datos ingresados
    persona.insertar_nombres(nombres)
    persona.insertar_apellidos(apellidos)
    if apellido_casada:
        persona.insertar_apellido_casada(apellido_casada)
    fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento_str, "%d-%m-%Y")
    persona.insertar_fecha_nacimiento(fecha_nacimiento)

    # Mostrar la información ingresada
    print("\nInformación de la persona:")
    print(f"Nombres: {persona.obtener_nombres()}")
    print(f"Apellidos: {persona.obtener_apellidos()}")
    print(f"Fecha de Nacimiento: {persona.obtener_fecha_nacimiento().strftime('%d-%m-%Y')}")
    edad = persona.calcular_edad()
    print(f"Edad: {edad} años")

    apellido_casada = persona.obtener_apellido_casada()
    if apellido_casada:
        print(f"Apellido de Casada: De {apellido_casada}")
    else:
        print("No está casada.")

if __name__ == "__main__":
    main()


