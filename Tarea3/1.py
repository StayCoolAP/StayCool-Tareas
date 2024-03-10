#1.Una tienda de autopartes necesita un programa para catalogar sus productos,crear la clase catalogo
# y producto, realizar un objeto dentro de un catalogo de productos el cual debe tener un metodo para agregar
# productos el cual debe tener un metodo para agregar productos y otra para mostrar toda la lista de productos.

#Resolución
class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

class Catalogo:
    #Lista vacia, se agregarán productos
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        #Se agrega producto
        self.productos.append(producto)

    def mostrar_productos(self):
        if not self.productos:
            print("La lista de productos está vacía.")
        else:
            print("Lista de productos:")
            #Se mencionará cada "producto" añadido a la lista "productos"
            for producto in self.productos:
                print(f"Código: {producto.codigo}, Nombre: {producto.nombre}, Precio: {producto.precio}")

#Ingresar producto por consola
def ingresar_producto():
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    return Producto(codigo, nombre, precio)

#Mostrar catalogo, bucle
catalogo = Catalogo()

while True:
    opcion = input("¿Desea agregar un nuevo producto? (s/n): ")
    if opcion.lower() == 's':
        producto = ingresar_producto()
        catalogo.agregar_producto(producto)
    elif opcion.lower() == 'n':
        break
    else:
        print("Opción inválida. Por favor, ingrese 's' para sí o 'n' para no.")

catalogo.mostrar_productos()