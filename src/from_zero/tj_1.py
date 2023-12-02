
#Ejercicio 1:
def nombre_y_edad():
    while True:
        try:
            nombre = str(input("Tu nombre? "))
            edad = int(input("Tu edad? "))

            print("Ok tu nombre es:", nombre,"y tienes ", edad)
            break
        except ValueError:
            print("ERROR ese digito no es soportado")
#Ejercicio 2:
def sumar():
    while True:
        try:
            num1 = int(input("Numero inicial: "))
            num2 = int(input("Numero para sumar: "))
            suma = num1 + num2
            print(suma)
            break

        except ValueError:
            print("ERROR: solo se aceptan valores numericos")
#Ejercicio 3:
def multi():
    while True:
        try:
            num3 = int(input("Ingresa el numero para multiplicar:"))
            for i in range(1, 11):
                mult = num3 * i
                print(num3, 'x', i, '=', mult)
        except ValueError:
            print("ERROR: solo valores numericos")

#Ejercicio 4:
def intercambiar_entre_variables():
    while True:
        try:
            num4 = int(input("Primer numero:"))
            num5 = int(input("Segundo numero: "))
            
            tem = num4
            num4 = num5
            num5 = tem
            print(num4, 'y' , num5)
            break
        except ValueError:
            print("ERROR: te dije que no, usa valores numericos")

#Ejercicio 5:
def area_de_un_triangulo():
    while True:
        try:
            base = int(input("Ingresa la base del triangulo: "))
            altura = int(input("Ingresa la altura del triangulo: "))

            x =(base * altura) / 2
            print(x)
            break
        except ValueError:
            print("ERROR SOLO VALORES NUMERICOS")

nombre_y_edad()
sumar()
multi()
intercambiar_entre_variables()
area_de_un_triangulo()