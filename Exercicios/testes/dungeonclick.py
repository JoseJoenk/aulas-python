import pyautogui
import time

print('''
      [ 1 ] Matar Monstros em Tela Espremida
      [ 2 ] Mineirar em Tela Espremida
      [ 3 ] Matar Monstros em Tela Cheia''')
n = int(input('Qual o layout do farm? '))

if n == 1:
    while True:
        time.sleep(40)
        pyautogui.click(1692, 754)
        time.sleep(40)
        pyautogui.click(1633, 754)
elif n == 2:
    while True:
        time.sleep(15)
        pyautogui.click(1690, 923)
        time.sleep(15)
        pyautogui.click(1632, 924)
elif n == 3:
    while True:
        time.sleep(40)
        pyautogui.click(440, 835)
        time.sleep(40)
        pyautogui.click(388, 835)
