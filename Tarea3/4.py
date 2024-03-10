#4. crear un archivo nuevo y realizar una funcion que permita dividir 2 numeros, importar esta funcion
# ponerlo en un bucle while True , y al ser llamada la importacion ponerlo dentro de un try except 
# ejecutar la funcion hasta que realice correctamente la division luego de eso romper el bucle

from division import dividir

while True:
    try:
        numerador = float(input("Ingrese numerador: "))
        denominador = float(input("Ingrese denominador: "))
        #Usamos la función importada
        resultado = dividir(numerador, denominador)
        print("El resultado de la división es: ", resultado)
        break
    #Usamos ZeroDivisionError por si se quiere dividir por 0
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero")
    except ValueError:
        print("Error: Ingrese números válidos.")