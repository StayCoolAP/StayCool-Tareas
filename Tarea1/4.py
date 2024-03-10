# 4.Realizar un programa que filtre si eres apto para registrar un negocio ,condiciones: mayor de edad , tener ruc y tener un nombre comercial
# ,los inputs son si y /o no . la salida debe ser si esta apto o no para abrir un comercio.

#Haremos las siguiente preguntas con respuesta si/no, comando lower para que todo quede en minuscula
print("\nBienvenido al programa de filtros para abrir tu negocio, responda las siguientes preguntas")
#Es mayor de edad?
edad = input("\n¿Es usted mayor de edad? (Responda si o no): ").lower()
#Tiene Ruc?
t_ruc = input("¿Tiene RUC? (Responda si o no): ").lower()
#Tiene nombre comercial?
t_n_c = input("¿Tiene un nombre comercial? (Responda si o no): ").lower()

#Condición if else
if edad == "si" and t_ruc == "si" and t_n_c == "si":
    print("Eres apto para abrir un comercio.")
else:
    print("Lo sentimos, debes cumplir con todas las condiciones para abrir un comercio.")