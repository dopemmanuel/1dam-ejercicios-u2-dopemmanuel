def suma():
    try:     
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("ingrese el segundo numero: "))
    
        suma = num1 + num2
        print("Su resultado es: ", suma)
    except ValueError:
        print("Error Solo se utilizan numeros")
    else:
        print("ERROR 404 numero no encontrado")

def main():
    print("Suma: ")
    suma()
if __name__ == "__main__":
    main()