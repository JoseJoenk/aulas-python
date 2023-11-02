import pyautogui

# Aguarde alguns segundos para que você possa mover o mouse para a posição desejada
input("Mova o mouse para a posição desejada e pressione Enter...")

# Obtenha as coordenadas atuais do cursor
x, y = pyautogui.position()

# Exiba as coordenadas na tela
print(f"Coordenadas: x={x}, y={y}")