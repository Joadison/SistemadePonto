import os
import time
import datetime, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Ponto
pont = webdriver.Chrome()
pont.get("http://ponto/")
time.sleep(1)

usuar=pont.find_element_by_xpath('//*[@id="P101_USERNAME"]')
usuar.click()
usuar.send_keys('USER')

senha = pont.find_element_by_xpath('//*[@id="P101_PASSWORD"]')
senha.click()
senha.send_keys('SENHA')

entrar =  pont.find_element_by_xpath('//*[@id="B4361864787786875"]/span')
entrar.click()

baterpt = pont.find_element_by_xpath('//*[@id="uHeader"]/nav/ul/li[2]/a')
baterpt.click()
time.sleep(5)

okk = pont.find_element_by_xpath('//*[@id="B4444627920887422"]/span')
okk.click()
time.sleep(5)
pont.close()
pont.quit()
exit()


# Fazer que bate em por horas 
# excutar somente de segunda a sexta 
# e bater de 07:50 - 13:10 - 14:10 - 17:40
#
