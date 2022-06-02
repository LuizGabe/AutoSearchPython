import pyautogui as pyg
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# Iniciar a variavel de resposta
resposta = []

# Abra o arquivo (leitura)
arquivo = open("C:/Logica_Programacao/AutoSearch/arquivo.txt", 'r',encoding="utf-8")

# Colocarem um array
conteudo = arquivo.readlines()
print(conteudo)
arquivo.close()

# Ver quantos tem no arquivo
numeroElem = len(conteudo)
print(numeroElem)

# Pesquisar uma resposta
browser = webdriver.Chrome()


time.sleep(10)
# Analisar um por um os itens e depois
for i in range(numeroElem):
    pesquisa = conteudo[i]
    browser.get("https://www.google.com/")
    # Variaveis para localizar objetos no selenium
    inputSearch = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    buttonSearch = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]")
    inputSearch.send_keys(pesquisa)
    buttonSearch.submit()
    resposta = browser.find_element_by_xpath("/html/body/div[7]/div/div[10]/div[1]/div[2]/div/div/div[1]/div/div[1]/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div/div[1]/div/span")
    print(resposta)

time.sleep(10)
browser.close()