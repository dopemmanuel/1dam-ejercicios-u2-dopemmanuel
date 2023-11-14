def palabra() -> tuple:
    wrd = tuple(input("Dame una palabra: "))
    return wrd


def vocales(wrd: tuple) -> tuple:
    vocal = tuple(["a",0],["e",0],["i",0],["o",0],["u",0])
    for vocale in vocal:
        vocale[1] = palabra.count(vocal[0])
        return vocal
def main():
    wrd = palabra()
    vocal = vocales()
    print