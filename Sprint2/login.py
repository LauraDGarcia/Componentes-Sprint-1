from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class loginpage(BasePage):
    #GOOGLE_EMAIL = (By.XPATH, "//span[contains(.,'Google')]")
    #SELECT_ACCOUNT = (By.XPATH, "")
    #NEXT_BUTTON_ONE = (By.XPATH, "")
    #CANCEL_BUTTON_ONE = (By.XPATH, "")
    SELECT_EMAIL = (By.XPATH, "(//button[contains(@class,'NyLay')])[1]")
    EMAIL = (By.XPATH, "//input[contains(@name,'email')]")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    BUTTON_CATPCHA = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/section/form/div[2]")
    BUTTON_LOGIN = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/section/form/button")
    CLOSE_BOTTON = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div/button[3]")
    MODAL_CLOSE_SESION = (By.XPATH, "(//button[contains(@class,'39')])[2]")
    FORGOT_PASSWORD = (By.XPATH, "//a[contains(@class,'yGGaR')]")
    RECOVERY_EMAIL = (By.XPATH, "//input[@placeholder='abc@mail.com']")
    SEND_CODE_button = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/form/button")
    DIALOG = (By.XPATH, "//*[@id='_button--standard_9pqly_1']")
    CODE = (By.XPATH, "//input[contains(@id,'otp-input-0')]")
    RESEND_CODE = (By.XPATH, "//span[contains(@class,'VowFu')]")
    CODE_NOT_YET_RECEIVED = (By.XPATH, "(//button[@type='button'])[2]")
    NEXT_BUTTON = (By.XPATH, "//button[contains(@class,'42')]")
    PASSWORD_NEW = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/form/fieldset[1]/label/div/div/input")
    CONFIRM_PASSWORD_NEW = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/form/fieldset[2]/label/div/div/input")
    CHANGE = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/form/button")
    RETURN = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/button[2]")


    def navigate_home(self):
        self.go_to_page("https://qa-account-commizzion-vm.inlazetest.com/login")

    def navigate_recovery(self):
        self.go_to_page("https://qa-account-commizzion-vm.inlazetest.com/recovery-password")


    #Ingresar con google 
    def select_email_google(self):
        self.wait_for_element(self.GOOGLE_EMAIL).click()

    def select_google(self):
        self.wait_for_element(self.SELECT_ACCOUNT).click()
   
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
        element.clear()
        element.send_keys(password)

    def select_captcha(self):
        self.wait_for_element(self.BUTTON_CATPCHA).click()

    def select_button_login(self):
        self.wait_for_element(self.BUTTON_LOGIN).click()

    def select_button_close(self):
        self.wait_for_element(self.CLOSE_BOTTON).click()

    def select_button_modal(self):
        self.wait_for_element(self.MODAL_CLOSE_SESION).click()

    #Recuperar contraseña

    def select_email_button(self):
        self.wait_for_element(self.SELECT_EMAIL).click()

    def select_recovery(self):
        self.wait_for_element(self.FORGOT_PASSWORD).click()

    def select_mail(self):
        self.wait_for_element(self.RECOVERY_EMAIL).click()

    def text_mail(self, email):
        element = self.wait_for_element(self.RECOVERY_EMAIL) 
        element.clear() 
        element.send_keys(email)

    def select_button_code(self):
        self.wait_for_element(self.SEND_CODE_button).click()

    def select_dialog(self):
        self.wait_for_element(self.DIALOG).click()

    def Verify_email(self,code):
        self.wait_for_element(self.CODE).click()
        element = self.wait_for_element(self.CODE) 
        element.clear() 
        element.send_keys(code)
        
    def next_button(self):    
        self.wait_for_element(self.NEXT_BUTTON).click()

    def new_password(self):
        self.wait_for_element(self.PASSWORD_NEW).click()

    def text_new_password(self, password):
        element = self.wait_for_element(self.PASSWORD_NEW)
        element.send_keys(password)

    def confirm_password(self):
        self.wait_for_element(self.CONFIRM_PASSWORD_NEW).click()

    def text_password_confirm(self, password):
        element = self.wait_for_element(self.CONFIRM_PASSWORD_NEW)
        element.send_keys(password)

#   
