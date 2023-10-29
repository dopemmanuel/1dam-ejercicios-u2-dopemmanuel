
"""
num1 = int(input("Ingrese el numero a dividir: "))
num2 = int(input("Ingrese el segundo numero divisor: "))


try:
    
    if num1 / num2:
        div = num1 / num2
        print("El resultado es", div)
        
#Tuve que personalizar el mensaje predeterminado cuando divides entre cero:
except ZeroDivisionError:
    print("Error: No puedes dividir entre cero")   
"""

num1 = int(input("Ingrese el numero a dividir: "))
num2 = int(input("Ingrese el segundo numero divisor: "))

if num2 == 0: 
    print("Error: No puedes dividir entre cero")
else:
    div = num1 / num2
    print("El resultado es", div)
