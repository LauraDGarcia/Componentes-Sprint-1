from Commizzion.wallet_balance import balancepage
from data.data import email_Campaña
from data.data import password_campaña
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Haria falta el ingresar a la cuenta

def test_Wallet_balance(driver):
    Wallet_balance = balancepage(driver)
    Wallet_balance.navigate_home()
    #Ingreso
    Wallet_balance.select_button_email() 
    Wallet_balance.select_text_email()
    Wallet_balance.text_email(email_Campaña) 
    Wallet_balance.select_text_password()
    Wallet_balance.text_password(password_campaña)
    time.sleep(20)
    Wallet_balance.select_checkbox()  
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(Wallet_balance.button_login))
    Wallet_balance.select_button_login()