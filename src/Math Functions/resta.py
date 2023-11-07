def restar():
    try:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("ingrese el segundo numero: "))

        resta = num1 - num2
        print("Su resultado es:", resta)
    except ValueError:
        print("ERROR solo numeros, eso no esta disponible")

def main():
    print("Resta: ")
    restar()
if __name__=="__main__":
    main()