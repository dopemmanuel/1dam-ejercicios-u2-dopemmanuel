def numeros():
    while True:
       
        num1 = int(input("Ingresa un numero entero positivo: "))

        if num1 > 0:
            impares = (str(i) for i in range( 1, num1 + 1) if i % 2 != 0)
            resultado = ", ".join(impares)
            print("Numeros impares desde 1 hasta", num1, ":", resultado)
            break
        else:
            print("El número ingresado no es positivo. Por favor, ingresa un número entero positivo")

def main():
    print("Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas: ")

    numeros()
if __name__ == "__main__":

    main()