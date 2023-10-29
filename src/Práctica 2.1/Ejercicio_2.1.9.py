def verificar_edad():

    edad = int(input("¿Cual es su edad?: "))

    if edad < 4:
        precio = 0
    elif edad >= 4 and edad <= 18:
        precio = 5
    else:
        precio = 10
        
    print("El Precio de entrada es de ", precio,"€")

verificar_edad()