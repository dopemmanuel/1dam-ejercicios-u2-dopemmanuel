"""
()^_____^)
"""
def sumar():
    """
    ()O.O)
    """
    try:     
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("ingrese el segundo numero: "))
    
        suma = num1 + num2
        print("Su resultado es: ", suma)
    except ValueError:
        print("ERROR Solo se utilizan numeros （︶^︶（）")

def main():
    print("Suma: ")
    sumar()
if __name__ == "__main__":
    main()