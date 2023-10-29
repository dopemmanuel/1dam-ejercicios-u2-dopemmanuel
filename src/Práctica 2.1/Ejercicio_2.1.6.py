"""
# Pedir al usuario su nombre y sexo
nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (M para Mujer, H para Hombre): ")

# Convertir el nombre a mayúsculas para facilitar la comparación
nombre = nombre.upper()

# Verificar a qué grupo pertenece el usuario
if (sexo == "M" and nombre < "M") or (sexo == "H" and nombre > "N"):
    grupo = "A"
else:
    grupo = "B"

# Mostrar el grupo correspondiente
print(f"Usted pertenece al grupo {grupo}")

"""
def determinar_Grupo(nombre, sexo):
    
    nombre = nombre.upper()
    if sexo == "M" and nombre < "M" or sexo == "H" and nombre > "N":
        return "A"
    else:
        return "B"
    
def main():

    nombre = input("Ingrese su nombre: ")
    sexo = input("Ingrese su sexo (M para Mujer, H para Hombre): ")

    grupo = determinar_Grupo(nombre, sexo)
    print("Perteneces al grupo", grupo)

if __name__ =="__main__":
    main()