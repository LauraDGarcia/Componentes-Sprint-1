from Commizzion.campaigns import campaignspage
from data.data import email_Campaña
from data.data import password_campaña
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Haria falta el ingresar a la cuenta

def test_campaigns_management(driver):
    campaigns = campaignspage(driver)
    campaigns.navigate_home()
    #Ingreso
    campaigns.select_button_email() 
    campaigns.select_text_email()
    campaigns.text_email(email_Campaña) 
    campaigns.select_text_password()
    campaigns.text_password(password_campaña)
    time.sleep(5)
    campaigns.select_checkbox()  
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(campaigns.BUTTON_LOGIN))
    campaigns.select_button_login()