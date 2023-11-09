
"""
import time
import sys

while True:
    tiempo_anterior = ""
    while True:
        tiempo_actual = time.strftime("%H:%M:%S")
        if tiempo_actual != tiempo_anterior:
            sys.stdout.write("\r" + tiempo_actual)
            sys.stdout.flush()
            tiempo_anterior = tiempo_actual
        time.sleep(1)
"""
import time
while True:

    tiempo_trascurrido = time.strftime("%H:%M:%S")   
    print(tiempo_trascurrido, end="\r")
    time.sleep(1)
