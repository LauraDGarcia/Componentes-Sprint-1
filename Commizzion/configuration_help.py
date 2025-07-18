from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class configurationpage(BasePage):
    #Ingreso normal
    SELECT_EMAIL = (By.XPATH, "//button[contains(.,'Correo electrónico')]")
    EMAIL = (By.XPATH, "//input[contains(@name,'email')]")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    BUTTON_C = (By.CLASS_NAME, "page_captcha__auNDN")
    BUTTON_LOGIN = (By.XPATH, "//button[contains(@type,'submit')]")
    #seleccionar la pestaña de configuración
    CONFIGURATION = (By.XPATH, "(//span[contains(@class,'vDxV3')])[1]")
    #Configuración ayuda
    CONFIGURATION_HELP = (By.XPATH, "(//span[contains(@class,'73')])[4]")
    CONFI_HELP_CALL = (By.XPATH, "(//button[contains(@class,'58')])[4]")
    CONFI_HELP_CHAT = (By.XPATH, "(//button[contains(@class,'58')])[5]")
    CONFI_HELP_POLICIES_TYC = (By.XPATH, "(//button[contains(@class,'76')])[1]")
    CONFI_HELP_POLICIES_PRIVACY_POLICY = (By.XPATH, "(//button[contains(@class,'76')])[2]")
    CONFI_HELP_POLICIES_ISO = (By.XPATH, "(//button[contains(@class,'76')])[3]")

    def navigate_home(self):
        self.go_to_page("https://qa-account-commizzion-vm.inlazetest.com/login") #YUna cuenta ya ingresada, si no poner los del login

    #Inicio de sesión 
    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))  
    
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

    def select_checkbox(self):
        checkbox_element = self.wait_for_element(self.BUTTON_C)
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.BUTTON_C))  # Esperar que sea clickeable
        checkbox_element.click() 

    def select_button_login(self):
        self.wait_for_element(self.BUTTON_LOGIN).click()

    #Ir a configuración

    def select_configuration(self):
        self.wait_for_element(self.CONFIGURATION).click()

    

    #Configuración ayuda
    def select_configuration_help(self):
        self.wait_for_element(self.CONFIGURATION_HELP).click()

    def select_confi_help_call(self):
        self.wait_for_element(self.CONFI_HELP_CALL).click()

    def select_confi_help_chat(self):
        self.wait_for_element(self.CONFI_HELP_CHAT).click()

    def select_confi_help_policies_tyc(self):
        self.wait_for_element(self.CONFI_HELP_POLICIES_TYC).click()

    def select_confi_help_policies_privacy_policy(self):
        self.wait_for_element(self.CONFI_HELP_POLICIES_PRIVACY_POLICY).click()

    def select_confi_help_policies_iso(self):
        self.wait_for_element(self.CONFI_HELP_POLICIES_ISO).click()
    