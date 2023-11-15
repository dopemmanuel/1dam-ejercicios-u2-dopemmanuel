"""
(⌐■_■):
"""
def carga():
    """
    (⌐■_■):
    """
    import time 
    def animation(interaciones = 8 , retraso = 5.90):
        for _ in range(interaciones):
            print("📁→",end="📂",flush=True)
        time.sleep(retraso)
    animation()
def main():
    print("Loading")
    carga()
    print("\n¡Carga completa")
if __name__=="__main__":
    main()