# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os
import re
import requests



#self.driver = webdriver.Edge(executable_path='driver\MicrosoftWebDriver') # - se for microsoft edge
driver = webdriver.Chrome(executable_path='driver/chromedriver') # se for chrome
#self.driver = webdriver.Firefox(executable_path='driver/geckodriver') # se for firefox

print('bot iniciado')
driver.get('http://www.fgf.edu.br/alunoonline/login.asp')
time.sleep(5)


#----INTERACAO COM A TELA DE LOGIN-----
print('interacao com a tela de login...')
login_box = driver.find_elements_by_class_name('td2')
user_box = login_box[0].find_element_by_tag_name('input')
password_box = login_box[1].find_element_by_tag_name('input')
send_button = driver.find_element_by_tag_name('caption')

user_box.click()
user_box.send_keys('hortanio')
password_box.click()
password_box.send_keys('tanio123')
send_button.click()
time.sleep(3)
#----INTERACAO COM A PAGINA PRINCIPAL-----
print('interacao com a tela principal...')
buttons = driver.find_elements_by_tag_name('a')
financeiro_button = buttons[3]
financeiro_button.click()

#----INTERACAO COM A PAGINA DO FINANCEIRO-----
print('interacao com o modulo financeiro...')
time.sleep(2)
#--- OBTENDO A URL COM OS VALORES
iframe_box_url = driver.find_element_by_tag_name('iframe').get_attribute('src')

#--REDIRECIONAMENTO PARA URL DE VALORES
driver.get(iframe_box_url)

fgf_title = driver.find_element_by_tag_name('legend').text
financeiro_head = driver.find_element_by_tag_name('thead')
financeiro_body = driver.find_element_by_tag_name('tbody')


finc_head_itens = financeiro_head.find_elements_by_tag_name('th')
finc_body_itens = financeiro_body.find_elements_by_tag_name('tr')
valor = 0
calc = 0
print(fgf_title +'\n')
for i in range(len(finc_body_itens)):
    valor = finc_body_itens[i].find_elements_by_tag_name('td')
    valor_tratado = valor[5].text.replace('R$ ', '').replace(',', '.')
    valor_convertido = float(valor_tratado)
    print(valor[5].text)
    calc = calc + valor_convertido

total = 'Total: R$ {:.2f}'.format(calc)
total = total.replace('.', ',')

print('\n' + total)