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
#Esta es una forma mas simple de crear una lista:
"""
x, y, z, a, b, c = "Orange", "Banana", "Cherry", "Apple", "pinapple", "candy"
print(x)
print(y)
print(z)
print(a)
print(b)
print(c)
"""
#Otra forma de lista, con la diferencia de que las variables tienen asignado el mismo valor:
"""
x = y = z = "orange"
print(x)
print(y)
print(z)
"""
#Esta sirve para empaquetar una lista, sirve para cuando quieres hacer una colecion de valores esto se usa con lista o tupla:
"""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)
"""
#esto es algo mas especifico... algo que usaba pero no entendia:
"""
#En programación, el tipo de datos es un concepto importante.
Las variables pueden almacenar datos de diferentes tipos y diferentes tipos pueden hacer cosas diferentes.

Python tiene los siguientes tipos de datos integrados de forma predeterminada, en estas categorías:

Tipo de texto:	str
Tipos numéricos:	int, float, complex
Tipos de secuencia:	list, tuple, range
Tipo de mapeo:	dict
Tipos de conjuntos:	set, frozenset
Tipo booleano:	bool
Tipos binarios:	bytes, bytearray, memoryview
Ninguno Tipo:	NoneType

#Configuración del tipo de datos
En Python, el tipo de datos se establece cuando asignas un valor a una variable:

x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	NoneType


#Configuración del tipo de datos específico
Si desea especificar el tipo de datos, puede utilizar las siguientes funciones de constructor:

x = str("Hello World")	str	
x = int(20)	int	
x = float(20.5)	float	
x = complex(1j)	complex	
x = list(("apple", "banana", "cherry"))	list	
x = tuple(("apple", "banana", "cherry"))	tuple	
x = range(6)	range	
x = dict(name="John", age=36)	dict	
x = set(("apple", "banana", "cherry"))	set	
x = frozenset(("apple", "banana", "cherry"))	frozenset	
x = bool(5)	bool	
x = bytes(5)	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview
"""