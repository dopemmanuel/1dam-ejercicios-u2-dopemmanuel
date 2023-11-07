def multiplicar():
    try:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("ingrese el segundo numero: "))

        multiplica = num1 * num2
        print("Su resultado es: ", multiplica)
    except ValueError:
        print("ERROR eso no es posible")

def main():
    print("Multiplicacion: ")
    multiplicar()
if __name__=="__main__":
    main()