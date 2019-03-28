# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os
import re
import requests



#self.driver = webdriver.Edge(executable_path='driver\MicrosoftWebDriver') # - se for microsoft edge
driver = webdriver.Chrome(executable_path='driver/chromedriver') # se for chrome
#self.driver = webdriver.Firefox(executable_path='driver/geckodriver') # se for firefox

driver.get('http://www.fgf.edu.br/alunoonline/login.asp')
time.sleep(5)


#----INTERACAO COM A TELA DE LOGIN-----
login_box = driver.find_elements_by_class_name('td2')
user_box = login_box[0].find_element_by_tag_name('input')
password_box = login_box[1].find_element_by_tag_name('input')
send_button = driver.find_element_by_tag_name('caption')

user_box.click()
user_box.send_keys(user)
password_box.click()
password_box.send_keys(password)
send_button.click()
time.sleep(3)
#----INTERACAO COM A PAGINA PRINCIPAL-----

buttons = driver.find_elements_by_tag_name('a')
financeiro_button = buttons[3]
financeiro_button.click()

#----INTERACAO COM A PAGINA DO FINANCEIRO-----

