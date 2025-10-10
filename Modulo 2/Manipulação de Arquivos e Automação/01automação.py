#1° passo: intalar o pyautogui com o comando:
# pip install pyautogui

# crie uma automação que abra automaticamente um navegador

# importamos a biblioteca para o script em uso
import pyautogui

# 'Press' é um comando q ultilizamos
# para pressionar a tecla desejada
pyautogui.press()

# 'sleep' é um comando q ultilizamos para deixar o código
# em espera por alguns segundos
pyautogui.sleep(1)

#'Write' é um comando que ultilizamos para passar o que queremos
# escrever
pyautogui.write('Google Chrome')

pyautogui.press('Enter')