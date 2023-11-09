"""
(。﹏。()
"""
def num_entero():
    """
    (⌐■_■)
    """
    while True:
        try:
            num = int(input("Ingrrese el numero entero: "))
            print("Has ingresado el número:", num)
            break
        except ValueError:
            print("La entrada no es correcta")

def main():
    print("(☞ﾟヮﾟ)☞ Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el ,mensaje La entrada no es correcta, y lanzará la excepción capturada: ")
    num_entero()
if __name__=="__main__":
    main()