"""
def pizza_ingredientes():

    vegetariana = input("¿Quiere una pizza vegetariana? (Sí/No): ").lower()

    if vegetariana == "sí":
        print("Ingredientes vegetarianos disponibles: Pimiento y Tofu")
        ingrediente = input("Elige un ingrediente (Pimiento o Tofu): ").capitalize()

        if ingrediente in ["Pimiento", "Tofu"]:
            print("Pizza vegetariana con Mozzarella, Tomate y", ingrediente)
        else:
            print("Ese ingrediente no está disponible.")
    else:
        print("Ingredientes no vegetarianos disponibles: Peperoni, Jamón y Salmón")
        ingrediente = input("Elige un ingrediente (Peperoni, Jamón o Salmón): ").capitalize()

        if ingrediente in ["Peperoni", "Jamón", "Salmón"]:
            print("Pizza no vegetariana con Mozzarella, Tomate y", ingrediente)
        else:
            print("Ese ingrediente no está disponible.")

pizza_ingredientes()
"""

def pizza_I():

    veggy = input("quieres una pizza vegetariana? (Yes/Not)")

    if veggy =="si":
        print("Ingredientes vegetarianos disponibles: Pimiento y Tofu")
        ingredients = input("Elige un ingrediente (Pimiento o Tofu): ")

        if ingredients in ("pimiento", "tofu"):
            print("Pizza vegetariana con Mozzarella, Tomate y", ingredients)
        else:
            print("El ingrediente no esta disponible")
    else:
        print("Ingredientes no vegetarianos disponibles: Peperoni, Jamón y Salmón")
        ingredients = input("Elige un ingrediente (Peperoni, Jamón o Salmón): ")

        if ingredients in ("Peperoni", "jamon", "Salmon"):
            print("Pizza no vegetariana con Mozzarella, Tomate y", ingredients)
        else:
            print("Ese Ingrediente no esta en la lista")


pizza_I()