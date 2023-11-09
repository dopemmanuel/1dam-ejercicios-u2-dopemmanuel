import os

# Obtenemos la ruta del escritorio
desktop_path = os.path.expanduser("~/Desktop")

# Definimos el contenido del archivo
contenido = "Hola, mundo!"

# Creamos el archivo en el escritorio
with open(os.path.join(desktop_path, "(⌐■_■)"), "w") as archivo:
    archivo.write(contenido)

print("El archivo 'Hola' ha sido creado en el escritorio.")
