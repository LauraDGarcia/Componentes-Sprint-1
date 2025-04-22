from Commizzion.wallet_balance import balancepage
from data.data import email_wallet_y
from data.data import password_wallet_y
from data.data import email_wallet_n
from data.data import password_wallet_n
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
    Wallet_balance.text_email(email_wallet_y) 
    Wallet_balance.select_text_password()
    Wallet_balance.text_password(password_wallet_y)
    time.sleep(20)
    Wallet_balance.select_checkbox()  
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(Wallet_balance.button_login))
    Wallet_balance.select_button_login()
    #Redirigir a wallet
    Wallet_balance.select_button_wallet()
    Wallet_balance.select_button_balance()
    Wallet_balance.select_button_eye_balance()
    Wallet_balance.select_icon_total_balance()
    Wallet_balance.select_icon_incoming_balance()
    Wallet_balance.select_icon_value_receive()
    Wallet_balance.select_icon_lapz_button()
    Wallet_balance.select_button_balance()
    #Salida de una cuenta e ingreso de la otra 
    Wallet_balance.select_button_close()
    Wallet_balance.select_button_modal()
    Wallet_balance.select_button_email() 
    Wallet_balance.select_text_email()
    Wallet_balance.text_email(email_wallet_n) 
    Wallet_balance.select_text_password()
    Wallet_balance.text_password(password_wallet_n)
    time.sleep(20)
    Wallet_balance.select_checkbox()  
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(Wallet_balance.button_login))
    Wallet_balance.select_button_login()
    #Sin saldo
    Wallet_balance.select_button_wallet()
    Wallet_balance.select_button_balance()
    Wallet_balance.select_modal_add_account_button_yes()
    Wallet_balance.select_modal_add_account_button_not()
    Wallet_balance.select_modal_add_account_button_X()
    Wallet_balance.select_Button_add_account()
