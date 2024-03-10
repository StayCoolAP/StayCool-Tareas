# 2.Realizar un programa que calcule el area y el perimetro de un poligono a tu eleccion( triangulo , cuadrado , circulo)
#Triangulo
import math

def c_perimetro(l1, l2, l3):
    perimetro = l1 + l2 + l3
    return perimetro

def c_area(l1, l2, l3):
    semiperimetro = c_perimetro(l1, l2, l3) / 2
    area = math.sqrt(semiperimetro*(semiperimetro-l1)*(semiperimetro-l2)*(semiperimetro-l3))
    return area

# Longitudes de los lados del triángulo, float para usar decimales
l1 = float(input("Longitud primer lado: "))
l2 = float(input("Longitud segundo lado: "))
l3 = float(input("Longitud tercer lado: "))

#Calculo perímetro y área
perimetro = c_perimetro(l1, l2, l3)
area = c_area(l1, l2, l3)

#Resultado
print("El perímetro del triángulo es:", perimetro)
print("El área del triángulo es:", area)