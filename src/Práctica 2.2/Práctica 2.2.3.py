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
# Acabo de entender que el "main" puede ser  un titulo en salida para lo que acabas de programar... hice pruebas y es facinante:
def main():
    print("Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas: ")
#Aqui Coloque la funcion de lo que programe y el print que esta arriba sirve como titulo:
    numeros()
if __name__ == "__main__":

    main()