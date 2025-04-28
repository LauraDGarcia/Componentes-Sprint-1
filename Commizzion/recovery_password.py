from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class recoverypage(BasePage):
    #GOOGLE_EMAIL = (By.XPATH, "//span[contains(.,'Google')]")
    #SELECT_ACCOUNT = (By.XPATH, "")
    #NEXT_BUTTON_ONE = (By.XPATH, "")
    #CANCEL_BUTTON_ONE = (By.XPATH, "")
    SELECT_EMAIL = (By.XPATH, "(//button[contains(@class,'NyLay')])[1]")
    FORGOT_PASSWORD = (By.XPATH, "//a[contains(@class,'yGGaR')]")
    RECOVERY_EMAIL = (By.XPATH, "//input[@placeholder='abc@mail.com']")
    SEND_CODE_button = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/form/button")
    DIALOG = (By.XPATH, "//*[@id='_button--standard_9pqly_1']")
    CODEONE = (By.XPATH, "//input[contains(@id,'otp-input-0')]")
    CODETWO = (By.XPATH, "//input[contains(@id,'otp-input-1')]")
    CODETHREE = (By.XPATH, "//input[contains(@id,'otp-input-2')]")
    CODEFOUR = (By.XPATH, "//input[contains(@id,'otp-input-3')]")
    CODEFIVE = (By.XPATH, "//input[contains(@id,'otp-input-4')]")
    CODESIX = (By.XPATH, "//input[contains(@id,'otp-input-5')]")
    RESEND_CODE = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/article/button[1]")
    CODE_NOT_YET_RECEIVED = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/article/button[2]")
    NEXT_BUTTON = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/button[1]")
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

    def select_recovery(self):
        self.wait_for_element(self.FORGOT_PASSWORD).click()

    def select_mail(self):
        self.wait_for_element(self.RECOVERY_EMAIL).click()

    def text_mail_recovery(self, email):
        element = self.wait_for_element(self.RECOVERY_EMAIL)
        element.clear()
        element.send_keys(email)

    def select_button_code(self):
        self.wait_for_element(self.SEND_CODE_button).click()

    def select_dialog(self):
        self.wait_for_element(self.DIALOG).click()

    def text_code(self):
        self.wait_for_element(self.CODEONE).click()

    def get_code1(self, code1):
        element = self.wait_for_element(self.CODEONE)
        element.clear() 
        element.send_keys(code1)

    def get_code2(self, code2):
        element = self.wait_for_element(self.CODETWO)
        element.clear() 
        element.send_keys(code2)

    def get_code3(self, code3):
        element = self.wait_for_element(self.CODETHREE)
        element.clear() 
        element.send_keys(code3)

    def get_code4(self, code4):
        element = self.wait_for_element(self.CODEFOUR)
        element.clear() 
        element.send_keys(code4)

    def get_code5(self, code5):
        element = self.wait_for_element(self.CODEFIVE)
        element.clear() 
        element.send_keys(code5)
        
    def get_code6(self, code6):
        element = self.wait_for_element(self.CODESIX)
        element.clear() 
        element.send_keys(code6)
        
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

    def change_password(self):
        self.wait_for_element(self.CHANGE).click()

    def button_RETURN(self):
        self.wait_for_element(self.RETURN).click()