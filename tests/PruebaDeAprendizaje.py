"""
# Acabo de entender que el main es el titulo en salida para lo que acabas de programar... hice pruebas y es facinante:
def main():
    print("Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.")
#Aqui Coloque la funcion de lo que programe y el print que esta arriba sirve como titulo:
if __name__ == "__main__":
    main()
"""
#Esto es para comprender mejor lo de "range" ignoralo:
"""
num = input("Dame un numero: ")

for i in range(1, 10 + 1):
    print(i, end=" ")
"""
#esta es una forma mas simple de crear una lista:
"""
x, y, z, a, b, c = "Orange", "Banana", "Cherry", "Apple", "pinapple", "candy"
print(x)
print(y)
print(z)
print(a)
print(b)
print(c)
"""
#otra forma de lista, con la diferencia de que las variables tienen asignado el mismo valor:
"""
x = y = z = "orange"
print(x)
print(y)
print(z)
"""
#esta sirve para empaquetar una lista, sirve para cuando quieres hacer una colecion de valores esto se usa con lista o tupla:
"""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)
"""