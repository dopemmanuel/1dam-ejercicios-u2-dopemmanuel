def tabla_de_multiplicar():
    num1 = input("Ingrese el multiplicando(factor): ")


    if num1:
        num1 = int(num1)
        print("Tabla de multiplicar del", num1)
        for i in range(1,11):
            resultado = num1 * i
            print("", num1, "x", i,"=", resultado,)
        else:
            for i in range(1,11):
                print("Tabla de multiplicar del", i)
                for k in range(1,11):
                    resultado = i * k
                print("", i,"x", k,"=",resultado)

def main():
    print("Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.")
    tabla_de_multiplicar()
if __name__ =="__main__":
    main()