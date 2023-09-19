import pyautogui
import time

x, y = 425, 1062

duration = 2

pyautogui.moveTo(x, y, duration=duration)

pyautogui.click(x, y)

time.sleep(2) #após clicar espera 2s

pyautogui.hotkey('alt', 'f4') #fecha a janela após os 2s

input("Pressione Enter para encerrar o programa...")
