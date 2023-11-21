def obtener_palabra() -> tuple:
    wrd = tuple(input("Dame una palabra: "))
    return wrd

def contar_vocales(wrd: tuple) -> tuple:
    vocales = [("a", 0), ("e", 0), ("i", 0), ("o", 0), ("u", 0)]

    for letra in wrd:
        for vocal in vocales:
            if letra.lower() == vocal[0]:
                vocal = (vocal[0], vocal[1] + 1)

    return vocales

def main():
    wrd = obtener_palabra()
    resultado_vocales = contar_vocales(wrd)
    print("Resultado de contar vocales:", resultado_vocales)

if __name__ == "__main__":
    main()
