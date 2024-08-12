#Bibliotecas usadas

import yfinance
import pyautogui
import pyperclip
import webbrowser
import time

#Buscar dados e salvado variáveis

ticker = input("Digite o Código da ação desejada: ")
dados = yfinance.Ticker(ticker).history(start="2024-01-01", end="2024-12-31")
fechamento = dados.Close
valor_max = round(fechamento.max(), 2)
valor_medio = round(fechamento.mean(), 2)
valor_minimo = round(fechamento.min(), 2)

#para graáfico no vs code - 
#{fechamento.plot()}


destinatario = "eloyneto61@gmail.com"
assunto = "Teste automação python"
mensagem = f"""
Prezado Gestor,

Seguem as análises da ação {ticker}:

Cotação máxíma: R${valor_max}
Cotação Minima: R$ {valor_minimo}
Valor Médio: R${valor_medio}


Qualquer duvida, estou à disposição

Atte.
"""
#Pra identificar o ponto na tela que vai clicar
#time.sleep(10)
#pyautogui.position()


#enviando email:
#texto com 3 aspas pode quebrar a linha

#abrir navegador e ir para o email
webbrowser.open("www.gmail.com")
time.sleep(4)

#Configurando pausa de 3s do pyautogui
pyautogui.PAUSE = 3

#Clicar no botao escrever
pyautogui.click(x=102, y=171) #tela cheia 

#digitar o email o dest e clicar tab
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

#digitar asssunto do email + tab
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

#digitar texto
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", 'v')

#clicar no botao enviar
pyautogui.click (x=1296, y=1017)

#fechar o gmail
pyautogui.click("ctrl", "f4")

print("Email Enviado com Sucesso!")