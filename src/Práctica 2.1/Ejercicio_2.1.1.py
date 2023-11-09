"""
( ´･･)ﾉ(._.`)
"""
def verificar_edad():
    """
    (⌐■_■)
    """
    while True:
        try:
            edad = int(input("Ingrese su edad: "))

#Esta es opcional XD... o(^▽^)o
            if edad > 100:
                print("En serio??!!", edad, "años??, felicidades si has vivido esos años eso es imposible...")
        
            elif  edad < 18:
                print("Eres menor de edad")
            else:
                print("Eres mayor de edad")
            break
        except ValueError:
            print("Por Favor, Ingrese una edad valida")
def main():
    print("")
    verificar_edad()
if __name__=="__main__":
    main()