# Introducción a la programación, sección:17
# 07/10/2023
# José Santiago Urzúa Luarca
# Objetivo: Crear programa que almaacene datos en clase, imprimir y calcular conversiones de divisas (GTQ - USD).
# Entrada: Datos de vehículo de interés y descuento.
class Nave:
    def __init__(self, modelo=0, precio=0.0, marca="", disponible=True, tipoCambioDolar=0.0, descuentoAplicado=0.0):
        self.modelo = modelo
        self.precio = precio
        self.marca = marca
        self.disponible = disponible
        self.tipoCambioDolar = tipoCambioDolar
        self.descuentoAplicado = descuentoAplicado

    def DefinirModelo(self, unModelo):
        self.modelo = unModelo

    def DefinirPrecio(self, unPrecio):
        self.precio = unPrecio

    def DefinirMarca(self, unaMarca):
        self.marca = unaMarca

    def DefinirTipoCambio(self, unTipoCambio):
        self.tipoCambioDolar = unTipoCambio

    def CambiarDisponibilidad(self):
        self.disponible = not self.disponible

    def MostrarDisponibilidad(self):
        if self.disponible:
            return "Actualmente disponible"
        else:
            return "No se encuentra disponible actualmente"

    def MostrarInformacion(self):
        precioEnDolares = round(self.precio / self.tipoCambioDolar, 2)
        return f"Marca: {self.marca}. Modelo: {self.modelo}. Precio de venta: Q{self.precio}, Precio en dólares ${precioEnDolares}. {self.MostrarDisponibilidad()}"

    def AplicarDescuento(self, miDescuento):
        self.descuentoAplicado = miDescuento
        nuevoPrecio = self.precio - (self.precio * self.descuentoAplicado)
        self.DefinirPrecio(nuevoPrecio)

# Función para solicitar un número float al usuario
def obtener_numero_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Función para solicitar una cadena al usuario
def obtener_cadena(mensaje):
    return input(mensaje)

# Función para solicitar una respuesta sí/no al usuario
def obtenerRespuesta_si_no(mensaje):
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta in ["si", "sí"]:
            return True
        elif respuesta in ["no"]:
            return False
        else:
            print("Por favor, responda 'si' o 'no'.")

# Función principal
def main():
    print("Bienvenido al programa de gestión de automóviles.")
    modelo = int(input("Ingrese el modelo de la nave: "))
    precio = obtener_numero_float("Ingrese el precio de la nave en GTQ: ")
    marca = obtener_cadena("Ingrese la marca de la nave: ")
    tipo_cambio = obtener_numero_float("Ingrese el tipo de cambio a dólares: ")
    disponible = obtenerRespuesta_si_no("¿La nave está disponible? (si/no): ")

    nave = Nave(modelo, precio, marca, disponible, tipo_cambio)

    print("Información de la nave:")
    print(nave.MostrarInformacion())

    aplicar_descuento = obtenerRespuesta_si_no("¿Desea aplicar un descuento a la nave? (si/no): ")
    if aplicar_descuento:
        descuento = obtener_numero_float("Ingrese el descuento a aplicar (como decimal, por ejemplo, 0.1 para 10%): ")
        nave.AplicarDescuento(descuento)
        print(f"Descuento aplicado. Nuevo precio de la nave: Q{nave.precio}")
        nave.precio = nave.precio / tipo_cambio
        print(f"Nuevo precio de la nave: ${nave.precio}")

if __name__ == "__main__":
    main()



