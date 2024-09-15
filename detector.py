nombre_archivo = input("Introduce el nombre del archivo a procesar: ")
idioma_archivo = input("Ingresa el idioma en que está el archivo: ")

idioma_archivo = idioma_archivo.lower()

#Para almacenar en el registro de entrenamiento
if idioma_archivo == "español":
    idioma_archivo = "espaniol"
elif idioma_archivo == "inglés" or idioma_archivo == "ingles":
    idioma_archivo = "ingles"
elif idioma_archivo == "francés" or idioma_archivo == "frances":
    idioma_archivo = "frances"
else:
    pass

#Creación de las rutas
ruta_archivo = "textos\\" + nombre_archivo 
ruta_registro = "textos\\" + idioma_archivo.lower() + ".txt"

#Diccionario que almacena la frecuencia de cada letra
diccionario_letras = {}

#Abrimos el registro para acumular las frecuencias conforme le damos más textos en el idioma en cuestión
with open(ruta_registro, encoding="UTF-8") as registro_input:
    for linea in registro_input.readlines():
        letra, frecuencia = linea.split(": ")
        diccionario_letras[letra] = int(frecuencia)

#Realiza el conteo de las letras
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

#Guarda los valores finales actualizados en el mismo archivo de registro
with open (ruta_registro, 'w',encoding="UTF-8") as registro:
    for llave, valor in diccionario_letras.items():
        registro.write(f"{llave}: {valor}\n")