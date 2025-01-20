from Sprint2.login import loginpage
from data.data import email
from data.data import password
from Sprint2.login import loginpage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 

def test_login(driver):
    login = loginpage(driver)
    login.navigate_home()  # Ir a la página de inicio de sesión
    login.select_button_email() 
    #time.sleep(5) # Seleccionar el botón de "Correo electrónico"
    login.select_text_email()
    login.wait_for_element(login.EMAIL)
    login.text_email(email) # ingresar correo 
    #time.sleep(5)
    login.text_password(password)  # Ingresar contraseña
    #time.sleep(5)
    login.select_captcha()  # Resolver CAPTCHA manualmente
    #time.sleep(10)
    login.select_button_login()
    login.navigate_login() #Ingresar a la pagina
    login.select_button_close()

#def test_forgot_password(driver):