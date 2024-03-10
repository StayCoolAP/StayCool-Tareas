#3. Del siguiente texto :
texto ="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
# realizar al menos 4 funciones de string

#Resolución

#Separamos todas las palabras del texto
print("\nSe separa todas las palabras del texto: ")
palabras=texto.split()
print(palabras)

#Menciona cuántas veces se repite la palabra mencionada
print("\nCuántas veces se menciona la palabra 'it': ")
conteo = texto.count("it")
print(conteo)

#Convertimos en texto en mayusculas
print("\nSe muestra el texto en mayuscula: ")
texto_mayusculas = texto.upper()
print(texto_mayusculas)

#Reemplazamos " " por "", osea quitamos los espacios
print("\nSe muestra el texto sin espacios: ")
texto_reemplazo = texto.replace(" ", "")
print(texto_reemplazo)