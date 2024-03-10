#1. Crear un menu iterativo con las siguientes opciones 
#2. opcion 1 'Saludar' , pedir datos personales
#3. opcion 2 Realizar una operacion matematica pedir 2 numeros 
#4. opcion 3 Agregar a lista un diccionario que tenga (nombre ,edad ,correo,cursos). Los cursos sera a su vez una lista de diccionario que tendra las llaves de nombre de curso y listado de notas
#5. opcion 4 calcular el promedio de las notas y agregar las notas finales a una lista  
#6. opcion 5 mostrar listado de alumnos aprobados 
#7. opcion 6 mostrar listado de alumnos desaprobados
#8. opcion 7 Generar una funcion rango hasta un numero grande (10^10) con un step y agregar a una lista los numeros que cumplan la condicion de ser multiplo de 2 ,  5 y de 7.Finalmente mostrar el tamaño de esa lista.
#9. opcion 8 llamar a una funcion que devuelva el mayor de 2 numeros ingresados por teclado.
#10. opcion 9 Salir.

#Resolución:
alumnos = []

#Opción 1
def saludar():
    nombre = input("Ingrese su nombre completo: ")
    print(f"\nBienvenido, {nombre}")
    return {"nombre": nombre}

#Opción 2
def operacion():
    print("Ingrese 2 números y escoja la operación matemática que desee.")
    num1 = float(input("Ingrese su primer número: "))
    num2 = float(input("Ingrese su segundo número: "))
    operador = input("Ingrese la operación que quiera hacer (+, -, *, /): ")
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        resultado = num1 / num2
    else:
        resultado = "Operador no válido"
    print("El resultado es:", resultado)

#Opción 3
def agregar():
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    correo = input("Ingrese su correo: ")
    cursos = []
    while True:
        curso_nombre = input("Ingrese el nombre del curso (o 'fin' para terminar): ")
        if curso_nombre.lower() == 'fin':
            break
        notas = input("Ingrese las notas del curso separadas por espacios: ").split()
        notas = [float(nota) for nota in notas]  # Convertimos las notas a float
        cursos.append({"curso": curso_nombre, "notas": notas})
    alumno = {"nombre": nombre, "edad": edad, "correo": correo, "cursos": cursos}
    alumnos.append(alumno)
    print("Datos registrados correctamente.")

#Opción 4
def promedio():
    for alumno in alumnos:
        for curso in alumno["cursos"]:
            suma_notas = sum(curso["notas"])
            cantidad_notas = len(curso["notas"])
            promedio = suma_notas / cantidad_notas
            print(f"El promedio de notas de {alumno['nombre']} en el curso {curso['curso']} es: {promedio}")

#Opción 5
def aprobados():
   for alumno in alumnos:
        for curso in alumno["cursos"]:
            suma_notas = sum(curso["notas"])
            cantidad_notas = len(curso["notas"])
            promedio = suma_notas / cantidad_notas
            if promedio >= 10:
                print(f"{alumno['nombre']} aprobó el curso {curso['curso']} con un promedio de {promedio}")

#Opción 6
def desaprobados():
     for alumno in alumnos:
        for curso in alumno["cursos"]:
            suma_notas = sum(curso["notas"])
            cantidad_notas = len(curso["notas"])
            promedio = suma_notas / cantidad_notas
            if promedio < 10:
                print(f"{alumno['nombre']} desaprobó el curso {curso['curso']} con un promedio de {promedio}")

#Opción 7
def lista_multiplos():
    numeros = []
    #El valor de de rango debería ser 10**10, como demora en cargar usé 1000
    for num in range(1, 1000):
        if num % 2 == 0 and num % 5 == 0 and num % 7 == 0:
            numeros.append(num)
    print("Números que son múltiplos de 2, 5 y 7:", numeros)
    print("Tamaño de la lista de números múltiplos de 2, 5 y 7:", len(numeros))
#Opción 8
def mayor_2():
    print("Ingrese dos números y le diremos cuál es del mayor valor")
    while True:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        if num1 == num2:
            print("Los números ingresados son iguales. Ingrese números diferentes.")
        else:
            print("El mayor número es:", max(num1, num2))
            break

#Menú
while True:
    print("\nMENU")
    print("1. Saludar")
    print("2. Realizar una operación matemática")
    print("3. Agregar alumno")
    print("4. Calcular promedio de notas")
    print("5. Mostrar listado de alumnos aprobados")
    print("6. Mostrar listado de alumnos desaprobados")
    print("7. Generar lista de múltiplos")
    print("8. Obtener el mayor de 2 números")
    print("9. Salir")

    opcion = input("Ingrese el número de la opción que desea ejecutar: ")

    if opcion == '1':
        saludar()
    elif opcion == '2':
        operacion()
    elif opcion == '3':
        agregar()
    elif opcion == '4':
        promedio()
    elif opcion == '5':
        aprobados()
    elif opcion == '6':
        desaprobados()
    elif opcion == '7':
        lista_multiplos()
    elif opcion == '8':
        mayor_2()
    elif opcion == '9':
        print("Saliendo del programa......")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 9.")