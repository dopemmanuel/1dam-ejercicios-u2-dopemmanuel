"""
(⌐■_■)
"""
def numero_primo():
    """
    (⌐■_■)
    """
    while True:
        try:
            numero = int(input("Ingrese un número entero: "))

            if numero > 1:
                for i in range(2, int(numero**0.5) + 1):
                    if numero % i == 0:
                        print(numero," no es un número primo.")
                        break
                else:
                    print(numero, "es un número primo.")
            else:
                print(numero, "no es un número primo.")
                break
        except ValueError:
            print("ERROR: solo acepto digitos numericos... 🍷(￣へ￣()")
def main():
    """
    (⌐■_■)
    """
print("Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no: ")
numero_primo()
if __name__ =="__main__":
    main()