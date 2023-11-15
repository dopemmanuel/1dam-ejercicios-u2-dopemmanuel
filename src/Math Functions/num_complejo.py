"""
(⌐■_■): 
"""
def num_complex():
    """
    (⌐■_■):
    """
    while True:
        try:

            num_complejo1 = complex(input("Ingresa el primer numero: "))
            num_complejo2 = complex(input("Ingresa el segundo numero: "))

            sumar_complejo = num_complejo1 + num_complejo2
            print("Este es tu resultado: ", sumar_complejo)
            break
        except ValueError:
            print("ERROR solo se debe usar un numero y una letra... 🍷( ˘︹˘ ()")
def main():
    """
    (⌐■_■): 
    """
    print("Calculadora de numeros complejos: ")
    num_complex()
if __name__ == "__main__":
    main()
