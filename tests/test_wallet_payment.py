from Commizzion.wallet_payment import paymentpage
from data.data import email_Campaña
from data.data import password_campaña
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Haria falta el ingresar a la cuenta

def test_Wallet_Pay(driver):
    wallet_pay = paymentpage(driver)
    wallet_pay.navigate_home()
    #Ingreso
    wallet_pay.select_button_email() 
    wallet_pay.select_text_email()
    wallet_pay.text_email(email_Campaña) 
    wallet_pay.select_text_password()
    wallet_pay.text_password(password_campaña)
    time.sleep(20)
    wallet_pay.select_checkbox()  
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(wallet_pay.button_login))
    wallet_pay.select_button_login()