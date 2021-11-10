# iniciowhatsss
import os
import time
import datetime, random
os.system('chrome.exe')
numero = int(input('Qual é o telefone'))
chamado = input('Chamado')
nome = input('Nome')

def saudacao():
   mensagem = '\n'
hora = datetime.datetime.now().hour
if hora < 12:
   mensagem = 'Bom dia, '
elif 12 <= hora < 18:
   mensagem = 'Boa tarde, '
else:
   mesnagem = 'Boa noite, '
   
mensagem += '''%s ! Meu nome é Joadison! Sou no CATI estou entrando em contato referente ao chamado.:%s''' %(nome, chamado)
print(mensagem)

os.system('start chrome "https://web.whatsapp.com/send?phone=%d&text=%s"' %(numero, mensagem))
