from Commizzion.wallet_payment import paymentpage
from data.data import email_wallet_y
from data.data import password_wallet_y
from data.data import email_wallet_n
from data.data import password_wallet_n
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
    wallet_pay.text_email(email_wallet_y) 
    wallet_pay.select_text_password()
    wallet_pay.text_password(password_wallet_y)
    time.sleep(20)
    wallet_pay.select_checkbox()  
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(wallet_pay.button_login))
    wallet_pay.select_button_login()
    #redirige a wallet
    wallet_pay.select_button_wallet()
    wallet_pay.select_payment_history()
    wallet_pay.select_drop_down()
    wallet_pay.select_receipt()
    wallet_pay.select_expand_history_button()
    wallet_pay.select_request_help_button()
    #Salida de una cuenta e ingreso de la otra 
    wallet_pay.select_button_close()
    wallet_pay.select_button_modal()
    wallet_pay.select_button_email() 
    wallet_pay.select_text_email()
    wallet_pay.text_email(email_wallet_n) 
    wallet_pay.select_text_password()
    wallet_pay.text_password(password_wallet_n)
    time.sleep(20)
    wallet_pay.select_checkbox()  
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(wallet_pay.button_login))
    wallet_pay.select_button_login()
    #Sin saldo
    wallet_pay.select_no_history_modal()