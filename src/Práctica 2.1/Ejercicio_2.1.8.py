def evaluacion_puntuacion():
    while True:
        try:
            puntos = float(input("Ingrese la puntuacion: "))

            if puntos <= -1:
                print("estas QUEMAO!!!")
            elif puntos == 0:
                nivel = "inaceptable"
                dinero = 0
            elif puntos <= 0.4:
                nivel = "Aceptable"
                dinero = 2400 * puntos
            elif puntos >= 0.6:
                nivel = "Meritorio"
                dinero = 4800 * puntos

            print("Tu nivel de rendimiento es ", nivel)
            print("Recibiras", dinero,"€")
            break
        except ValueError:
            print("ERROR: eso no es un formato numerico...")
def main():
    print("")
evaluacion_puntuacion()
