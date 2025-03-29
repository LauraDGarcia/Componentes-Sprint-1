from Commizzion.configuration import configurationpage
from data.data import email_Campaña
from data.data import password_campaña
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Haria falta el ingresar a la cuenta

def test_configuration(driver):
    confi = configurationpage(driver)
    confi.navigate_home()
    #Ingreso
    confi.select_button_email() 
    confi.select_text_email()
    confi.text_email(email_Campaña) 
    confi.select_text_password()
    confi.text_password(password_campaña)
    time.sleep(5)
    confi.select_checkbox()  
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(campaigns.BUTTON_LOGIN))
    confi.select_button_login()
    #ir a configuracion
