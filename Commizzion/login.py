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
    BUTTON_CATPCHA = (By.XPATH, "//div[@class='recaptcha-checkbox-border']")
    BUTTON_LOGIN = (By.XPATH, "//button[contains(@class,'42')]")
    CLOSE_BOTTON = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div/button[3]")
    MODAL_CLOSE_SESION = (By.XPATH, "(//button[contains(@class,'39')])[2]")


    def navigate_home(self):
        self.go_to_page("https://qa-account-commizzion-vm.inlazetest.com/login")

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
