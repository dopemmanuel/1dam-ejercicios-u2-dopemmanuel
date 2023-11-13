def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

while True:
    try:
        numero_usuario = int(input("Ingrese un número entero (ingrese 0 para salir): "))
        if numero_usuario == 0:
            break

        if es_primo(numero_usuario):
            print(numero_usuario, "es un número primo.")
        else:
            print(numero_usuario, "no es un número primo.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
def main():
    print("Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no: ")
    es_primo()
if __name__=="__main__":
    main()