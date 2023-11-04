def edad_usuario():

    edad = int(input("Cual es tu edad? "))

    while edad <= 0:
        print("coloca una edad valida")
        edad = int(input("Cual es tu edad? "))
    for a in range(1, edad + 1):
        print("Has cumplido",a ,"años")


def main():
    print("Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad):")
    edad_usuario()
if __name__ == "__main__":
    main()