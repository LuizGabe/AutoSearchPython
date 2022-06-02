from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
browser = webdriver.Chrome()
text = "Oi"

browser.get("https://translate.google.com.br/?hl=pt-BR&sl=auto&tl=en&text="+text+"&op=translate") 
time.sleep(5)

traduzido = browser.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[8]/div/div[1]/span[1]/span/span").text

print(traduzido)
for i in range(100):
    time.sleep(1)
    print(i)

browser.close()


