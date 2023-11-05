def numeros_cuenta_atras():
        
        num2 = int(input("Ingrese el numero: "))
        
        if num2 < 0:
            print("El numero ingresado no es positivo")
        else:
            cuenta_atras = list(range(num2,-1,-1))
            atras =', '.join(map(str, cuenta_atras))
            print("Cuenta regresiva:", atras)



def main():
    print("Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas: ")
    numeros_cuenta_atras()
if __name__ == "__main__":
    main()
