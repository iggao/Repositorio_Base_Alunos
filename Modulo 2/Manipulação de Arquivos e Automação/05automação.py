import pyautogui
import webbrowser
import time

# passo 1: abri o yt com uma musica especifica
url ='https://www.youtube.com/watch?v=othqNdVQgS8&list=RDothqNdVQgS8&start_radio=1'
webbrowser.open(url)

# passo 2: aguardar o carregamento da pagina
time.sleep(5) # ajustar de acordo com a velocidade da internet ultilizada

# passo 3: garantir q o video comece (aperte o espaço para "play")
pyautogui.press('space') # toca ou pausa o video