============================= Sistema de Chamados ========================================
import os
import time
import datetime, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

google = os.system('chrome.exe')
google = os.system('start chrome "https://cati.tjce.jus.br/assystweb/application.do"')

user = google.find_element_by_xpath('//*[@id="login-user"]')
user.click()
user.send_keys('')

senha = google.find_element_by_xpath('//*[@id="login-password"]')
senha.click()
senha.send_keys('')

entrar = google.find_element_by_xpath('//*[@id="loginSubmit"]')
entrar.click()

filas = google.find_element_by_xpath('//*[@id="FilasdeAtendimento_button_title"]')
filas.click()

meuschamados = google.find_element_by_xpath('//*[@id="dijit__TreeNode_17_label"]')
meuschamados.click()

============================= Ponto ==================================================
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

#Ponto
navegador = webdriver.Chrome()
navegador.get("http://ponto/")
time.sleep(2)

user = navegador.find_element_by_xpath('//*[@id="P101_USERNAME"]')
user.click()
user.send_keys('')

senha = navegador.find_element_by_xpath('//*[@id="P101_PASSWORD"]')
senha.click()
senha.send_keys('')

entrar =  navegador.find_element_by_xpath('//*[@id="B4361864787786875"]/span')
entrar.click()

baterpt = navegador.find_element_by_xpath('//*[@id="uHeader"]/nav/ul/li[2]/a')
baterpt.click()



==================================== Whatsapp===============================
import os
import time
import datetime, random
os.system('chrome.exe')
numero = int(input('Qual é o telefone.: '))
chamado = input('Qual é o Chamado.: ')
nome = input('Qual é o Nome.: ')

def saudacao():
   mensagem = '\n'
hora = datetime.datetime.now().hour
if hora < 12:
   mensagem = 'Bom dia, '
elif 12 <= hora < 18:
   mensagem = 'Boa tarde, '
else:
   mesnagem = 'Boa noite, '
   
mensagem += '''%s! Meu nome é Joadison! Sou no CATI, estou entrando em contato referente ao chamado.:%s''' %(nome, chamado)
print(mensagem)

os.system('start chrome "https://web.whatsapp.com/send?phone=%d&text=%s"' %(numero, mensagem))
