#2. Realizar un programa que tenga una clase producto el cual solo tiene los atributos de nombre y codigo
# el codigo tiene la siguiente estructura PAIS-LOTE-AÑO ejemplo:PERU-00001-2024 crear un metodo que imprima el objeto de forma 
# literal (__str__) y que permita identificar el pais de origen y nro de lote

#Resolución
class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        pais,lote,año = self.codigo.split('-')
        return f"Nombre: {self.nombre}, Código: {self.codigo}\nPaís de origen: {pais}, Número de lote: {lote}, Año: {año}"

# Función para ingresar los datos del producto por consola
def ingresar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    codigo = input("Ingrese el código del producto (PAIS-LOTE-AÑO): ")
    return Producto(nombre, codigo)

# Ejemplo de uso
producto = ingresar_producto()
print(producto)