"""
()$_$)
"""

def grados_a_fahrenheit():
    """
    ()^o^)
    """
    while True:
        try:
            


            celsius = float(input("Ingrese los grados celcius: "))

            fahrenheit =  celsius * 9/5 + 32
            print("La temperatura de celcius a fharenheit es:", fahrenheit )
            break
        except ValueError:
            print("ERROR, no son los datos que esperabamos (˘︹˘()")

def main():
    print("(☞ﾟヮﾟ)☞ Reescribe el programa conversor de temperaturas para que lea repetidamente la temperatura hasta que sea correcta, debe detectar los fallos usando try y except:")
    grados_a_fahrenheit()
if __name__=="__main__":
    main()

