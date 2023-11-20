def main():
    total = 0
    asignaturas = {"Matt":6, "Fisics":4, "Chemistry":8}
    for asignaturas, credits in asignaturas.items():
        print(asignaturas, "tiene" ,credits,)
        total += credits
    print("Total =", total)
if __name__=="__main__":
    main()