# Crie uma automação q escreva um texto automaticamente

import pyautogui
import time

# Obs: deixar aberto o bloco d notas
# aguarde 5 segundos para vc abrir o bloco d notas
time.sleep(5)

# esreva o texto
pyautogui.write('Automatização com pyautogui', interval=0.1)
