"""
def suma():

    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("ingrese el segundo numero: "))
    
    if num2 == "":
        raise ValueError("ERROR Solo se usa el formato de numeros")
    elif num1 == "":
        raise ValueError("ERROR ese formato no esta permitido")

    suma = num1 + num2

    if num1 + num2:
        print("Su resultado es: ", suma)

try:
    def main():
        print("Suma:")
        suma()
    if __name__ =="__main_":
        main()
except ValueError as e:
    print(e)
"""
def suma():
    while True:
        try:     
            num1 = int(input("Ingrese el primer numero: "))
            num2 = int(input("ingrese el segundo numero: "))
    
            suma = num1 + num2
            print("Su resultado es: ", suma)
            break
        except ValueError:
            print("Error Solo se utilizan numeros")
            
            

def main():
    print("Suma: ")
    suma()
if __name__ == "__main__":
    main()


