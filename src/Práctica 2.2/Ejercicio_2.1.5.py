"""
edad = int(input("Introduzca su edad: "))
ingresos =int(input("Coloque sus ingresos mensuales:"))

if ingresos < 1000:
    print("No debes tributar.")

elif edad < 16:
    print("No debes tributar.")
else:
    print("Debes tributar.")
"""
edad = int(input("Introduzca su edad: "))
ingresos =int(input("Coloque sus ingresos mensuales:"))

if ingresos >= 1000 and edad == 16:
    print("Debes tribular")
else:
    print("No debes")