nombre_archivo = input("Introduce el nombre del archivo a procesar: ")

ruta_archivo = "textos\\" + nombre_archivo 

with open (ruta_archivo, encoding= "UTF-8") as archivo:
    texto = archivo.read()
    print(texto)
    