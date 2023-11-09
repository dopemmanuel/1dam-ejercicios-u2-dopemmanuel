"""
()⌐■_■)
"""
def Pass_words():
    """
    ()⌐■_■)
    """
    while True:
        Pass1 = "Usuario_Tarde"
        contraseña = input("Introduzca la contraseña: ")

        if contraseña != Pass1:
            print("Incorrect Password!!, try again...  🍷(˘︹˘()")
        else:
            print("BRAAAVOO... CORRECTO (✪ ω ✪)")
            break  

def main():
    """
    d=====(￣▽￣*)b
    """
    print("(☞ﾟヮﾟ)☞ Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje,Incorrect Password!!: ")
    try:
        Pass_words()
    except NameError as e:
        print(e)

if __name__=="__main__":
    main()
   