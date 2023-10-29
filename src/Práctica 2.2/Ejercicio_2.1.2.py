"""
Pass1 = "Usuario_Tarde"
Pass2 = "4358"
Pass3 = "Password"
Pass4 = "Prog_DAM"
Pass5 = "GITHUB"
Pass6 = "Porfin emma se aprendio el Pseudocodigo con Python"

contraseña = input("Introduzca la contraseña: ")

if contraseña == Pass1 :
    print("Correcto!!")

elif contraseña == Pass2 :
    print("Correcto Papu")

elif contraseña == Pass3 :
    print("Correct yoo got an ice cream")

elif contraseña == Pass4 :
    print("Incorret- naaaa mentiras, Es CORRECTO")

elif contraseña == Pass5 :
    print("cOrEcToOoOoOoOoOoO!!")

elif contraseña == Pass6 :
    print("Sii aprendio(le falta aprender), y si acabas de introducir la contraseña correcta")

else:
    print("Incorrecto!!")
"""

def verificar_contraseña(contraseña):
    contraseñas = {
        "Usuario_Tarde": "CORRECTO!!",
        "4358": "Correcto papu!!",
        "Password" : "Correct yoo got an ice cream",
        "Prog_DAM" : "Incorret- naaaa mentiras, Es CORRECTO",
        "GITHUB" : "cOrEcToOoOoOoOoOoO!!",
        "Porfin emma se aprendio el Pseudocodigo con Python" : "Sii aprendio(le falta aprender), y si acabas de introducir la contraseña correcta",
    }

    if contraseña in contraseñas:
        print(contraseñas[contraseña])
        return True
    else:
        print("Incorrecto")
        return False

while True:
    contraseña = input("Introduzca la contraseña: ")
    if verificar_contraseña(contraseña):
        break
    else:
        continuar = input("Desea intentarlo de nuevo? (SI/NO): ")
        if continuar.lower() != "si":
            break