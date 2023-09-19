import pyautogui

print("Mova o mouse para a posição desejada e aguarde alguns segundos.")
print("As coordenadas serão exibidas em seguida.")

# Aguarde alguns segundos para mover o mouse
pyautogui.sleep(5)

# Obtenha as coordenadas atuais do mouse
x, y = pyautogui.position()

# Exiba as coordenadas
print(f"Coordenadas X: {x}, Coordenadas Y: {y}")