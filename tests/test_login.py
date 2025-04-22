from Commizzion.login import loginpage
from data.data import email
from data.data import password
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

    