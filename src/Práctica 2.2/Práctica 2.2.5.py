def triangulo_numerico():
    num = int(input("Ingrese el numero entero: "))

    for num in range(1, num + 1):
        print("*" * num)


def main():
    print("Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido:")
    triangulo_numerico()
if __name__  == "__main__":
    main()