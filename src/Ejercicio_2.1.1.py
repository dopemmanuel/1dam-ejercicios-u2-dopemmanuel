"""
edad = int(input("Ingrese su edad: "))

#Esta es opcional XD
if edad > 100:
        print("En serio??!!", edad, "años??, tu deverias de estar muerto eso es imposible...")
        
elif  edad < 18:
    print("Eres menor de edad")
      
elif edad > 18:
    print("Eres mayor de edad")
"""

def verificar_edad():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))

#Esta es opcional XD
            if edad > 100:
                print("En serio??!!", edad, "años??, tu deverias de estar muerto eso es imposible...")
        
            elif  edad < 18:
                print("Eres menor de edad")
            else:
                print("Eres mayor de edad")
            break
        except ValueError:
            print("Por Favor, Ingrese una edad valida")

verificar_edad()