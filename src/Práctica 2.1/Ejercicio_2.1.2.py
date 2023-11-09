"""
(⌐■_■)
"""
def verificar_contraseña():
    """
    (⌐■_■)
    """
    contraseñas = {
    "Usuario_Tarde": "CORRECTO!!",
    "4358": "Correcto papu!!",
    "Password": "Correct yoo got an ice cream",
    "Prog_DAM": "Incorret- naaaa mentiras, Es CORRECTO",
    "GITHUB": "cOrEcToOoOoOoOoOoO!!",
    "Porfin emma se aprendio el Pseudocodigo con Python": "Sii aprendio(le falta aprender), y si acabas de introducir la contraseña correcta",
    }

    while True:
        contraseña = input("Introduzca la contraseña: ")
        if contraseña in contraseñas:
            print(contraseñas[contraseña])
            return True
        else:
            print("Incorrecto")
            continuar = input("Desea intentarlo de nuevo? (SI/NO): ")
            if continuar != "si":
                return False
            
def main():
    print("(⌐■_■)")
    verificar_contraseña()
if __name__=="__main__":
    main()