from Sprint2.login import loginpage
from data.data import email
from data.data import password
from data.data import code
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
    login.select_button_modal() #Aca llega el login
    login.select_email_button()
    login.select_recovery()
    login.select_mail()
    login.text_mail(email)
    login.select_button_code()
    login.select_dialog()
    login.Verify_email(code) #Codigo que llega al email
    login.next_button()
    login.new_password()
    login.text_new_password("NuevaContraseña@123")
    login.confirm_password()
    login.text_password_confirm("NuevaContraseña@123")
    