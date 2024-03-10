# 3.Realizar un programa que nos pida el ingreso total de un hogar y vaya pidiendo posibles gastos.
#Como resultado debe decir  todos los egresos y el ahorro.

def c_ahorro(ingreso_total, gasto_total):
    ahorro = ingreso_total - gasto_total
    return ahorro

#Ingreso total del hogar
ingreso_total = float(input("Coloque el ingreso total de su hogar: "))

#Lista de gastos
gastos = []

# Solicitar los gastos
print("Ingrese sus gastos (ingrese 'fin' para terminar):")
while True:
    gasto = input("Gasto: ")
    if gasto.lower() == 'fin':
        break
    #append agregará a la lista los gatos añadidos
    gastos.append(float(gasto))

# gasto total, suma de gastos
gasto_total = 0
for gasto in gastos:
    #+= suma el valor de gasto a gasto_total
    gasto_total += gasto

#Calculo ahorro
ahorro = c_ahorro(ingreso_total, gasto_total)

#Resultado
print("\nTodos los egresos:")
for gasto in gastos:
    print("-$", gasto)
print("El ahorro es:", ahorro)