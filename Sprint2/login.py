from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from data.data import email 
#from data.data import password

class loginpage(BasePage):
    #GOOGLE_EMAIL = (By.XPATH, "//button[contains(.,'Google')]")
    #SELECT_ACCOUNT = (By.XPATH, "")
    #NEXT_BUTTON_ONE = (By.XPATH, "")
    #CANCEL_BUTTON_ONE = (By.XPATH, "")
    SELECT_EMAIL = (By.XPATH, "//button[contains(.,'Correo electrónico')]")
    EMAIL = (By.XPATH, "//input[contains(@name,'email')]")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    BUTTON_CATPCHA = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/section/form/div[2]")
    BUTTON_LOGIN = (By.XPATH, "//button[contains(.,'Log In')]")
    CLOSE_BOTTON = (By.XPATH, "(//button[@id='_button--standard_15l1n_1'])[2]")
    MODAL_CLOSE_SESION = (By.XPATH, "")
    FORGOT_PASSWORD = (By.XPATH, "//a[@href='recovery-password']")
    #RECOVERY_EMAIL = (By.XPATH, "")
    #SEND_CODE = (By.XPATH, "")
    #DIALOG = (By.XPATH, "")
    #CODE = (By.XPATH, "")
    #RESEND_CODE = (By.XPATH, "")
    #CODE_NOT_YET_RECEIVED = (By.XPATH, "")
    #NEXT_BUTTON = (By.XPATH, "")
    #PASSWORD_NEW = (By.XPATH, "")
    #CONFIRM_PASSWORD_NEW = (By.XPATH, "")
    #CHANGE = (By.XPATH, "")

    def navigate_home(self):
        self.go_to_page("https://qa-account-commizzion-tmp.inlazetest.com/login")

    def navigate_login(self):
        self.go_to_page("https://qa-account-commizzion-tmp.inlazetest.com/")


    #Ingresar con google 
    def select_email_google(self):
        self.wait_for_element(self.GOOGLE_EMAIL).click()

    def select_google(self):
        self.wait_for_element(self.SELECT_ACCOUNT)
   
    #Ingreso al formulario por medio de correo
    def select_button_email(self):
        self.wait_for_element(self.SELECT_EMAIL).click()

    def select_text_email(self):
        self.wait_for_element(self.EMAIL).click()

    def text_email(self, email):
        element = self.wait_for_element(self.EMAIL)  # Corregido
        element.clear() 
        element.send_keys(email)

    def select_text_password(self):
        self.wait_for_element(self.PASSWORD).click()

    def text_password(self, password):
        element = self.wait_for_element(self.PASSWORD)
        element.send_keys(password)

    def select_captcha(self):
        self.wait_for_element(self.BUTTON_CATPCHA).click()

    def select_button_login(self):
        self.wait_for_element(self.BUTTON_LOGIN).click()

    def select_button_close(self):
        self.wait_for_element(self.CLOSE_BOTTON).click()

    #Recuperar contraseña

    