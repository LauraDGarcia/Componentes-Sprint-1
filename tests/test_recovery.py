from Commizzion.recovery_password import recoverypage
from data.data import email
from data.data import password
from data.data import code1
from data.data import code2
from data.data import code3
from data.data import code4
from data.data import code5
from data.data import code6
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
 

def test_recovery(driver):
    recovery = recoverypage(driver)
    recovery.navigate_home()  # Ir a la página de inicio de sesión
    recovery.select_button_email() 
    recovery.select_email_button()
    recovery.select_recovery()
    recovery.select_mail()
    time.sleep(5)
    recovery.text_mail_recovery(email)
    time.sleep(5)
    recovery.select_button_code()
    recovery.select_dialog()
    recovery.text_code()
    recovery.get_code1(code1)
    recovery.get_code2(code2)
    recovery.get_code3(code3)
    recovery.get_code4(code4)
    recovery.get_code5(code5)
    recovery.get_code6(code6) #Codigo que llega al email
    time.sleep(60)
    recovery.next_button()
    recovery.new_password()
    recovery.text_new_password("NuevaContraseña@123")
    recovery.confirm_password()
    recovery.text_password_confirm("NuevaContraseña@123")
    recovery.change_password()
    recovery.button_RETURN()