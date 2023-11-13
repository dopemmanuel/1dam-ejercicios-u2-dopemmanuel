"""
# Acabo de entender que el main es el titulo en salida para lo que acabas de programar... hice pruebas y es facinante:
def main():
    print("Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.")
#Aqui Coloque la funcion de lo que programe y el print que esta arriba sirve como titulo:
if __name__ == "__main__":
    main()
"""
#Esto es para comprender mejor lo de "range" ignoralo:
num = input("Dame un numero: ")
while True:

    for i in range(num):
        print(i)
        break
