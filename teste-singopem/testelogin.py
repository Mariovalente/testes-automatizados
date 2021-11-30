import selenium
import time 

#abrindo o navegador
navegador = webdriver.Chrome()
navegador.get('https://pt-br.facebook.com/')
navegador.find_element_by_xpath('//*[@id="email"]').click()
navegador.find_element_by_xpath('//*[@id="email"]').send_keys('mario123')
navegador.find_element_by_xpath('//*[@id="pass"]').click()
navegador.find_element_by_xpath('//*[@id="pass"]').send_keys('1234')
time.sleep(2)
navegador.find_element_by_name('login').click()
time.sleep(10)

if len(navegador.find_element_by_xpath('//*[@id="mount_0_0_F+"]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/ul')) == 1:
    print('teste bem sucedido')
else:
    print('teste mal sucedido')

