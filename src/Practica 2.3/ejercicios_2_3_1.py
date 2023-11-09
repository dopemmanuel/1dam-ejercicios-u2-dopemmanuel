"""
()O_O)
"""
def pedir_edad():
    """
    ()>.<)
    """
    while True:
        try:
            edad = int(input("Cual es tu edad? "))

            for a in range(1, edad + 1):
                print("Has cumplido",a ,"años")
            else:
#¯\_(ツ)_/¯:
                if edad > 100:
                    print("EN SERIO??!! (。_ 。)", edad,"años, eso es imposible...(X_X) ")
                break

        except ValueError:
            print("ERROR ingrese una edad valida")

def main():
    """
    Docstring... esto solo es de detalle
    """
    print("Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad): ")
    pedir_edad()
if __name__=="__main__":
    main()