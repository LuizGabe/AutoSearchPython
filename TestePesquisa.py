from http.client import responses
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

browser = webdriver.Chrome()
arquivo = open("C:/Logica_Programacao/AutoSearch/arquivo.txt", 'r',encoding="utf-8")

# Colocarem um array
indicePesquisa = arquivo.readlines()
indicePesquisaSem = []

for i in range(len(indicePesquisa)):
    indicePesquisaSem.append(indicePesquisa[i].replace("\n",""))

print(indicePesquisaSem)

arquivo.close()
conteudo = []

def pesquisar(pesquisa):
    browser.get("https://www.google.com/")
    inputSearch = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    buttonSearch = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]")
    inputSearch.send_keys(pesquisa)
    buttonSearch.submit()

    resposta = browser.find_element_by_xpath("/html/body/div[7]/div/div[10]/div[1]/div[2]/div/div/div[1]/div/div[1]/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div/div[1]/div/span/span").text 
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"+resposta+"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

    conteudo.append(pesquisa+"\n"+resposta+"\n")
    arquivo = open("Respostas.txt", 'w')
    arquivo.writelines(conteudo)
    arquivo.close() 

for i in range(len(indicePesquisaSem)):
    pesquisar(indicePesquisaSem[i])

time.sleep(5)
browser.close()
