import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#Executa ChromeDriver
driver = webdriver.Chrome(executable_path=r"C:\Users\55169\Desktop\info\chromedriver.exe")


#Abrir site
driver.get("https://www.google.com")


#Movendo o mouse e clicando no pop-up de login
pyautogui.moveTo(800,355)
pyautogui.click(800,355)


#Maximiza a janela
driver.maximize_window()


#Clicar no campo de pesquisa e digitar busca
pyautogui.click(800,305)
pyautogui.typewrite("Canal Datacoin YouTube", interval=0.1)
pyautogui.click(1100,315)


#Clicar no botão pesquisar
pyautogui.click(550,390)
time.sleep(3)


#Fechar janela atual utilizando hotkeys
pyautogui.hotkey('ctrl','f4')