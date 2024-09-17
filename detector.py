textos_procesados = []

try:
    with open("textos\\textos_registrados.txt", encoding="UTF-8") as archivo_aprendido:
        procesado = archivo_aprendido.read()
        textos_procesados = procesado.split(";")
        textos_procesados.pop()
except FileNotFoundError:
    pass

#Verifica que el archivo a procesar no haya sido utilizado anteriormente
nombre_archivo = input("Introduce el nombre del archivo a procesar: ")
while nombre_archivo in textos_procesados:
    nombre_archivo = input("Este texto ya fue procesado. Por favor, ingresa otro: ")
textos_procesados.append(nombre_archivo)

idioma_archivo = input("Ingresa el idioma en que está el archivo: ")

idioma_archivo = idioma_archivo.lower()

#Para almacenar en el registro de entrenamiento
if idioma_archivo == "español":
    idioma_archivo = "espaniol"
elif idioma_archivo == "inglés" or idioma_archivo == "ingles":
    idioma_archivo = "ingles"
elif idioma_archivo == "francés" or idioma_archivo == "francés":
    idioma_archivo = "frances"
else:
    pass

#Creación de las rutas
ruta_archivo = "textos\\" + nombre_archivo 
ruta_registro = "textos\\" + idioma_archivo.lower() + ".txt"

#Diccionario que almacena la frecuencia de cada letra
diccionario_letras = {}

#Abrimos el registro para acumular las frecuencias conforme le damos más textos en el idioma en cuestión
try:
    with open(ruta_registro, encoding="UTF-8") as registro_input:
        for linea in registro_input.readlines():
            letra, frecuencia = linea.split(": ")
            diccionario_letras[letra] = int(frecuencia)
except FileNotFoundError:
    pass

#Realiza el conteo de las letras
encontrado=1
try:
    with open (ruta_archivo, encoding= "UTF-8") as archivo:
        for linea in archivo.readlines():
            print(linea)
            linea = linea.upper()
            for letra in linea:
                if letra.isalpha():
                    try:
                        diccionario_letras[letra] += 1
                    except KeyError:
                        diccionario_letras[letra] = 1
except FileNotFoundError:
    print("Este archivo no existe.")
    encontrado=0

#Guarda los valores finales actualizados en el mismo archivo de registro
with open (ruta_registro, 'w',encoding="UTF-8") as registro:
    for llave, valor in diccionario_letras.items():
        registro.write(f"{llave}: {valor}\n")
        
if encontrado==1:
    with open("textos\\textos_registrados.txt", 'w',encoding="UTF-8") as archivo_aprendido:
        for nombre in textos_procesados:
            archivo_aprendido.write(f"{nombre};")