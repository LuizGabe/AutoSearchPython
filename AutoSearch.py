# Importar bibliotecas necessárias
# Biblioteca selenium importante para abrir um navegador e pesquisar de forma muito rápida
# Biblioteca time importante para alguns atrasos 
from http.client import responses
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

# Armazena o navegador que vamos usar na variável Browser
browser = webdriver.Chrome()

# Armazena na variavel arquivo o local do arquivo que queremos. 
#    OBS: Nesta linha ele abre o arquivo
#    O "encoding=utf-8" é a codificação do arquivo, funciona sem, mas os caracteres especias são totalmente distorcidos.
#    O "r" é para abrir o arquivo em modo de leitura, existe um jeito de abrir o arquivo em formado de escrita com "w"
arquivo = open("C:/Logica_Programacao/AutoSearch/arquivo.txt", 'r',encoding="utf-8")

# Coloca o conteudo do arquivo dentro de um conjunto chamado "indicePesquisa"
indicePesquisa = arquivo.readlines()

# Inicia um conjunto com o nome "indicePesquisaSem"
indicePesquisaSem = []

# Usa o Len para contar quantos elementos tem o conjunto e roda o código de acordo com isso
for i in range(len(indicePesquisa)):
    # Coloca dentro do conjunto "indicePesquisaSem" o "indicePesquisa" porém sem o "\n", esse \n é um comando de passar a linha dentro de um arquivo de texto
    indicePesquisaSem.append(indicePesquisa[i].replace("\n",""))

# Imprimi no console o Indice da pesquisa
print(indicePesquisaSem)

# Fecha o arquivo de texto
arquivo.close()

# Inicia um conjunto chamado "conteudo"
conteudo = []

# Essa é a função que faz tudo, ela recebe um termo de pesquisa e quarda o que conseguir no conjunto chamado "conteudo"
def pesquisar(pesquisa):
    # Abre o site do Google
    browser.get("https://www.google.com/")
    
    # Guarda o xpath(lugar unico de um site) do lugar onde nós escrevemos a pesquisa no google em uma variavel
    inputSearch = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    
    # Grarda o xpath(lugar unico de um site) do botão de pesquisar em uma variavel
    buttonSearch = browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]")
   
    # Escreve o termo da pesquisa no buscador
    inputSearch.send_keys(pesquisa)
    
    # Aperta o botão de pesquisar
    buttonSearch.submit()
    
    # Guarda o resultado da pesquisa em uma variavel chamada "resposta"
    resposta = browser.find_element_by_xpath("/html/body/div[7]/div/div[10]/div[1]/div[2]/div/div/div[1]/div/div[1]/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div/div[1]/div/span/span").text 
    
    # Coloca dentro do conjunto "conteudo" o termo da pesquisa, pula uma linha e escreve o resultado da pesquisa
    conteudo.append(pesquisa+"\n"+resposta+"\n")
    
    # Armazena na variavel arquivo o local do arquivo que queremos no modo de escrita OBS: Nesta linha ele abre o arquivo
    arquivo = open("Respostas.txt", 'w')
    
    # Escreve no arquivo o conjunto "conteudo"
    arquivo.writelines(conteudo)
    
    # Fecha o arquivo
    arquivo.close() 

# De acordo com o número de elementos do conjunto roda o código dentro
for i in range(len(indicePesquisaSem)):
    # Pesquisa cada elemento do conjunto de acordo o indice do for
    pesquisar(indicePesquisaSem[i])

# Dá um tempo no final da última pesquisa
time.sleep(5)

# Fecha o navegador
browser.close()
