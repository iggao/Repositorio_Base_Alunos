import pyautogui,  time

pyautogui.press('win')
time.sleep(1)
pyautogui.write('Desenhando com o Pyautogui')
pyautogui.press('enter')
time.sleep(2)

arvore = [
    '     ^     ',
    '    ^^^    ',
    '   ^^^^^   ',
    '    |||    ',
    '    |||    '
]

for linha in arvore:
    pyautogui.write(linha, interval=0.1)
    pyautogui.press('enter')
print('Desenho da árvore concluído!') 