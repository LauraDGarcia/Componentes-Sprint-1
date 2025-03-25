from Sprint2.login import loginpage
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
 

def test_login(driver):
    login = loginpage(driver)
    login.navigate_home()  # Ir a la página de inicio de sesión
    login.select_button_email() 
    login.select_text_email()
    login.text_email(email) # ingresar correo 
    login.select_text_password()
    login.text_password(password)  # Ingresar contraseña
    time.sleep(5)
    login.select_captcha()  # Resolver CAPTCHA manualmente  buscar como no hacerlo manual
    #time.sleep(20)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(login.BUTTON_LOGIN))
    login.select_button_login()
    login.select_button_close()
    login.select_button_modal() 
    
    #Aca inicia la recuperación de contraseña
def test_recovery(driver):
    login = loginpage(driver)
    login.navigate_home()
    login.select_email_button()
    login.select_recovery()
    login.select_mail()
    time.sleep(5)
    login.text_mail_recovery(email)
    time.sleep(5)
    login.select_button_code()
    login.select_dialog()
    login.text_code()
    login.get_code1(code1)
    login.get_code2(code2)
    login.get_code3(code3)
    login.get_code4(code4)
    login.get_code5(code5)
    login.get_code6(code6) #Codigo que llega al email
    login.next_button()
    login.new_password()
    login.text_new_password("NuevaContraseña@123")
    login.confirm_password()
    login.text_password_confirm("NuevaContraseña@123")
    