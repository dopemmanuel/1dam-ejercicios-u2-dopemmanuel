def invertir():

    cantidad = int(input("Ingrese la cantidad a invertir: "))
    taza = int(input("Ingrese el interes anual: "))
    años = int(input("Ingrese los años: "))

    intereses = taza / 100

    for años in range(1, años + 1):
        cantidad *= 1 + intereses
        print("Año:", años, "y Capital obtenido =", cantidad)
        print("Capital total al final de", años,"años: ", cantidad)

def main():
    print("Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión:")
    invertir()
if __name__ == "__main__":
    
    main()