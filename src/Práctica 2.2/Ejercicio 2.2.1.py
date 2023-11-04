"""
#Me tomo 2 horas pero le hice una pequeña expansion por si acaso se quiere colocar otra cantidad:
def mostrar_palabra_n_veces(n=10):
    palabra = input("Ingresa la palabra: ")
    for _ in range(n):
        print(palabra)

cantidad = int(input("Coloca la cantidad de veces que quieres que se coloque la letra o palabra: "))
if cantidad:
    amount = int(cantidad)
    mostrar_palabra_n_veces(amount)
else:
    mostrar_palabra_n_veces()
"""

def mostrar_palabra_n_veces(n=10):
    
    palabra = input("Ingresa la palabra: ")
    for _ in range(n):
        print(palabra)

cantidad = input("Coloca la cantidad de veces que quieres que se coloque la letra o palabra (o simplemente presiona Enter para usar 10 por defecto): ")
if cantidad:
    amount = int(cantidad)
    mostrar_palabra_n_veces(amount)
else:

    def main():
        print("Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces:")
    mostrar_palabra_n_veces()
if __name__ == "__main__":
    main()