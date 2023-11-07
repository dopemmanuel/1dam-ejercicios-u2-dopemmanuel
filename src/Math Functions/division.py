def division():
    num1 = int(input("Dividendo: "))
    num2 = int(input("Divisor: "))
    
    if num2 == 0:
        raise ValueError("ERROR La división entre cero es imposible...")
    elif num1 == 0:
        raise ValueError(": La división entre cero es imposible...")
    
    div = num1 / num2
    print("Su resultado es:", div)

try:
    def main():
        print("Divide: ")
        division()
    if __name__=="__main__":
        main()
except ValueError as y:
    print(y)