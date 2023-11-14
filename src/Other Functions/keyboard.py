"""
import keyboard
while True:
    keyboard.write("Has sido infectado (。_。()")
    keyboard.press_and_release("enter")
"""
import keyboard
import time
import pyautogui

# Espera unos segundos para abrir la aplicación deseada
time.sleep(5)

# Escribe 'Hola' usando keyboard
keyboard.write('Hola')

# Espera un momento y pulsa Enter usando keyboard
time.sleep(1)
keyboard.press_and_release('enter')

# Alternativamente, puedes usar pyautogui para escribir
pyautogui.write(' Mundo!')

# Espera un momento y pulsa Enter usando pyautogui
time.sleep(1)
pyautogui.press('enter')
