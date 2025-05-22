from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import os

navegador = webdriver.Chrome()
navegador.get("https://golcargo.gollog.com.br/account/#/login")
navegador.maximize_window()
time.sleep(3)
botao_user = navegador.find_element("xpath",'//*[@id="user"]').send_keys("vrg000050926")
botao_pass = navegador.find_element("xpath",'//*[@id="div-fields"]/form/div[1]/tti-password-with-label/p-password/div/input').send_keys("Golllog2025*")
botao_base = navegador.find_element("xpath",'//*[@id="franchise"]').send_keys("CGH")
botao_enter = navegador.find_element("xpath",'//*[@id="franchise"]').send_keys(Keys.ENTER)
    
time.sleep(1)
try:
    botao_confirma = navegador.find_element("xpath",'/html/body/div/div/div/button[2]')  # Use o seletor correto aqui
    botao_confirma.click()
except:
    pass
time.sleep(1)
for arquivo in os.listdir(r"C:\Users\User\Desktop\AutoDmin\AutorizaçõesNãoAnexadas"):
    if arquivo.lower() != "desktop.ini":
     caminho_completo = os.path.join(r"C:\Users\User\Desktop\AutoDmin\AutorizaçõesNãoAnexadas", arquivo)
    if os.path.isfile(caminho_completo):
        nome_arquivo_sem_extensao = os.path.splitext(arquivo)[0]
        
        barra_busca = navegador.find_element("xpath",'//*[@id="quickSearch"]')
        barra_busca.clear() 
        barra_busca.send_keys(nome_arquivo_sem_extensao)
        rastreio = navegador.find_element("xpath",'//*[@id="quickTracking-icon"]')    
        rastreio.click()  
        time.sleep(1)
        
        anexo_link_elemento = navegador.find_element("xpath",'//*[@id="trackingAWB"]/div[1]/div[1]/div/div/div[2]/div/div[3]/div/div[2]/a')

        onclick_value = anexo_link_elemento.get_attribute("onclick")

       
        start_index = onclick_value.find("'") + 1
        end_index = onclick_value.find("'", start_index)
        link_relativo = onclick_value[start_index:end_index]
        link_completo = f"https://golcargo.gollog.com.br{link_relativo}"
       

        navegador.execute_script(f"window.open('{link_completo}', '_blank');")
        
       
        janelas_abertas = navegador.window_handles
        janela_principal = navegador.current_window_handle
        for janela in janelas_abertas:
            if janela != janela_principal:
                navegador.close()
                navegador.switch_to.window(janela)
                pass
        
        time.sleep(5)
    
        add_arquivo_txt = navegador.find_element("xpath",'//*[@id="systemPanelBackground"]/div[2]/div[1]/div[2]/div[2]/div/ul/li[2]/a')
        add_arquivo_txt.click()
        time.sleep(2)
       
        
        upload_element = navegador.find_element("xpath","//input[@type='file']")
        
        upload_element.send_keys(caminho_completo)
        descricao = navegador.find_element("xpath",'//*[@id="FileContent"]/tbody/tr[1]/td[2]/input').send_keys("AUTORIZAÇÃO")
        tipo = navegador.find_element("xpath",'//*[@id="FileTypes"]').send_keys("Outros documentos")
        importar = navegador.find_element("xpath",'//*[@id="btnImport"]').send_keys(Keys.ENTER)
        
        
        

