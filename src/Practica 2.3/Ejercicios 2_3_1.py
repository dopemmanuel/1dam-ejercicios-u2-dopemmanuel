def pedir_edad():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))

#Esta es opcional XD
            if edad > 100:
                print("En serio??!!", edad, "años?..., sorprendente a la par que medio imposible")
            elif  edad < 18:
                print("Eres menor de edad")
            else:
                print("Eres mayor de edad")
            break
        except ValueError:
            print("Por Favor, Ingrese una edad valida")

def main():
    print("Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad): ")
    pedir_edad()
if __name__=="__main__":
    main()