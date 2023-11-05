def triangulo_numerico():
    num = int(input("Ingrese el numero entero: "))

    for i in range(1, num + 1):
        for j in range(i, 0, -2):
            print (j, end=" ")
        print()



def main():
    print("Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo: ")
    triangulo_numerico()
if __name__  == "__main__":
    main()