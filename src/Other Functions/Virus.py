import msvcrt
import ctypes

def virus():
    ctypes.windll.kernel32.SetConsoleTitleW("Virus Simulation")

    print("¡Tu PC ha sido infectada por el virus! Para eliminarlo, ingresa la contraseña correcta.")

    password = ""
    while True:
        char = msvcrt.getch().decode("utf-8")
        if char == "\r":
            break
        password += char
        print("*", end="")

    print(" (X_X() Correcto")  # Nueva línea después de ingresar la contraseña

    if password == "virus":
        print("Virus eliminado. Tu PC está a salvo ahora. (ノ｀Д)ノ")
    else:
        print("Contraseña incorrecta. El virus persiste... ヾ(⌐■_■)ノ♪")

virus() 