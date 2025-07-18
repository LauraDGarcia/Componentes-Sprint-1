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
    #Seleccion del perfil
    CONFIGURATION_PROFILE = (By.XPATH, "(//span[contains(@class,'1')])[17]")
    CONFI_PROFILE_LOGIN_DATA = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/section/div[2]/span/button")
    CONFI_PROFILE_EMAIL_AND_PASSWORD = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/section/div[2]/span/button/i")
    CONFI_PROFILE_EMAIL = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/section/div[2]/div/span[2]/span[2]/button/i")
    CONFI_PROFILE_EMAIL_BUTTONCHECK = (By.XPATH, "//input[contains(@type,'checkbox')]")
    CONFI_PROFILE_EMAIL_BUTTONCONTINUE = (By.XPATH, "//button[@class='_label-large_16ofa_137 _button_e9d1m_1 _button--filled_e9d1m_42']")
    CONFI_PROFILE_EMAIL_BUTTONCANCEL = (By.XPATH, "//button[contains(@class,'76')]")
    CONFI_PROFILE_EMAIL_CODEONE = (By.XPATH, "//input[contains(@id,'otp-input-0')]")
    CONFI_PROFILE_EMAIL_CODETWO = (By.XPATH, "//input[contains(@id,'otp-input-1')]")
    CONFI_PROFILE_EMAIL_CODETHREE = (By.XPATH, "//input[contains(@id,'otp-input-2')]")
    CONFI_PROFILE_EMAIL_CODEFOUR = (By.XPATH, "//input[contains(@id,'otp-input-3')]")
    CONFI_PROFILE_EMAIL_CODEFIVE = (By.XPATH, "//input[contains(@id,'otp-input-4')]")
    CONFI_PROFILE_EMAIL_CODESIX = (By.XPATH, "//input[contains(@id,'otp-input-5')]")
    CONFI_PROFILE_EMAIL_RESENDCODE = (By.XPATH, "(//button[contains(@class,'76')])[1]")
    CONFI_PROFILE_EMAIL_HAVENT_RECEIVED = (By.XPATH, "(//a[contains(@target,'blank')])[2]")
    CONFI_PROFILE_EMAIL_BUTTONNEXT = (By.XPATH, "//button[contains(@class,'42')]")
    CONFI_PROFILE_EMAIL_BUTTON_CANCEL = (By.XPATH, "(//button[contains(@class,'76')])[2]")
    CONFI_PROFILE_NEW_EMAIL = (By.XPATH, "(//input[@type='email'])[1]")
    CONFI_PROFILE_CONFIRM_EMAIL = (By.XPATH, "(//input[@type='email'])[2]")
    CONFI_PROFILE_SAVE_EMAIL = (By.XPATH, "//button[contains(@class,'42')]")
    CONFI_PROFILE_CANCEL_EMAIL = (By.XPATH, "//button[contains(@class,'76')]")
    CONFI_PROFILE_EMAIL_NEW_CODEONE = (By.XPATH, "//input[contains(@id,'otp-input-0')]")
    CONFI_PROFILE_EMAIL_NEW_CODETWO = (By.XPATH, "//input[contains(@id,'otp-input-1')]")
    CONFI_PROFILE_EMAIL_NEW_CODETHREE = (By.XPATH, "//input[contains(@id,'otp-input-2')]")
    CONFI_PROFILE_EMAIL_NEW_CODEFOUR = (By.XPATH, "//input[contains(@id,'otp-input-3')]")
    CONFI_PROFILE_EMAIL_NEW_CODEFIVE = (By.XPATH, "//input[contains(@id,'otp-input-4')]")
    CONFI_PROFILE_EMAIL_NEW_CODESIX = (By.XPATH, "//input[contains(@id,'otp-input-5')]")
    CONFI_PROFILE_EMAIL_NEW_RESENDCODE = (By.XPATH, "(//button[contains(@class,'76')])[1]")
    CONFI_PROFILE_EMAIL_NEW_HAVENT_RECEIVED = (By.XPATH, "(//a[contains(@target,'blank')])[2]")
    CONFI_PROFILE_EMAIL_NEW_BUTTONNEXT = (By.XPATH, "//button[contains(@class,'42')]")
    CONFI_PROFILE_EMAIL_NEW_BUTTON_CANCEL = (By.XPATH, "(//button[contains(@class,'76')])[2]")
    CONFI_PROFILE_DIALOG_EMAIL_YES = (By.XPATH, "//button[contains(@class,'163')]")
    CONFI_PROFILE_DIALOG_EMAIL_NOT = (By.XPATH, "//button[contains(@class,'224')]")
    CONFI_PROFILE_EDIT_PASSWORD = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/section/div[2]/div/span[2]/span[4]/button")
    CONFI_PROFILE_CURRENT_PASSWORD = (By.XPATH, "//input[@name='password']")
    CONFI_PROFILE_NEW_PASSWORD = (By.XPATH, "(//input[@type='password'])[2]")
    CONFI_PROFILE_CONFIRM_PASSWORD = (By.XPATH, "(//div[contains(@class,'7')])[6]")
    CONFI_PROFILE_SAVE_PASSWORD = (By.XPATH, "//button[contains(@class,'42')]")
    CONFI_PROFILE_CANCEL_PASSWORD = (By.XPATH, "//button[contains(@class,'76')]")
    CONFI_PROFILE_DIALOG_PASSWORD_YES = (By.XPATH, "//button[contains(@class,'163')]")
    CONFI_PROFILE_DIALOG_PASSWORD_NOT = (By.XPATH, "//button[contains(@class,'224')]")
    CONFI_PROFILE_CONTACT_LOCATION = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/section/div[3]/span/button")
    CONFI_PROFILE_COUNTRY = (By.XPATH, "/html/body/div[3]/div[3]/form/div[2]/fieldset[1]/label/div/i[2]")
    CONFI_PROFILE_NEW_COUNTRY = (By.XPATH, "//span[contains(.,'Colombia')]")
    CONFI_PROFILE_COUNTRY_CODE = (By.XPATH, "/html/body/div[3]/div[3]/form/div[2]/span/fieldset[1]/label/div/i[2]")
    CONFI_PROFILE_NEW_COUNTRY_CODE = (By.XPATH, "(//span[contains(.,'+57')])[2]")
    CONFI_PROFILE_X_PHONE = (By.XPATH, "/html/body/div[3]/div[3]/form/div[2]/span/fieldset[2]/label/div/i")
    CONFI_PROFILE_PHONE = (By.XPATH, "//input[@name='phone']")
    CONFI_PROFILE_LANGUAGE = (By.XPATH, "/html/body/div[3]/div[3]/form/div[2]/fieldset[2]/label/div/i")
    CONFI_PROFILE_NEW_LANGUAGE = (By.XPATH, "(//li[contains(@class,'1 undefined')])[1]")
    CONFI_PROFILE_SAVE_CONTACT_LOCATION  = (By.XPATH, "//button[contains(@class,'42')]")
    CONFI_PROFILE_CANCEL_CONTACT_LOCATION  = (By.XPATH, "//button[contains(@class,'76')]")
    CONFI_PROFILE_DIALOG_CONTACT_LOCATION_YES = (By.XPATH, "//button[contains(@class,'163')]")
    CONFI_PROFILE_DIALOG_CONTACT_LOCATION_NOT = (By.XPATH, "//button[contains(@class,'224')]")

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

    #Perfil correo
    def select_confi_profile_login_data(self):
        self.wait_for_element(self.CONFI_PROFILE_LOGIN_DATA).click()

    def select_confi_profile_email_and_password(self):
        self.wait_for_element(self. CONFI_PROFILE_EMAIL_AND_PASSWORD).click()

    def select_confi_profile_email(self):
        self.wait_for_element(self.CONFI_PROFILE_EMAIL).click()

    def select_confi_profile_email_buttoncheck(self):
        self.wait_for_element(self.CONFI_PROFILE_EMAIL_BUTTONCHECK).click()

    def select_confi_profile_email_buttoncontinue(self):
        self.wait_for_element(self.CONFI_PROFILE_EMAIL_BUTTONCONTINUE).click()

    def select_confi_profile_email_buttoncance(self):
        self.wait_for_element(self.CONFI_PROFILE_EMAIL_BUTTONCANCEL).click()

    def text_code(self):
        self.wait_for_element(self.CONFI_PROFILE_EMAIL_CODEONE).click()

    def get_code1(self, code1):
        element = self.wait_for_element(self.CONFI_PROFILE_EMAIL_CODEONE)
        element.clear() 
        element.send_keys(code1)

    def get_code2(self, code2):
        element = self.wait_for_element(self.CONFI_PROFILE_EMAIL_CODETWO)
        element.clear() 
        element.send_keys(code2)

    def get_code3(self, code3):
        element = self.wait_for_element(self.CONFI_PROFILE_EMAIL_CODETHREE)
        element.clear() 
        element.send_keys(code3)

    def get_code4(self, code4):
        element = self.wait_for_element(self.CONFI_PROFILE_EMAIL_CODEFOUR)
        element.clear() 
        element.send_keys(code4)

    def get_code5(self, code5):
        element = self.wait_for_element(self.CONFI_PROFILE_EMAIL_CODEFIVE)
        element.clear() 
        element.send_keys(code5)
        
    def get_code6(self, code6):
        element = self.wait_for_element(self.CONFI_PROFILE_EMAIL_CODESIX)
        element.clear() 
        element.send_keys(code6)

    def select_confi_profile_email_resendcode(self):
        self.wait_for_element(self.CONFI_PROFILE_EMAIL_RESENDCODE).click()

    def select_confi_profile_email_havent_received(self):
        self.wait_for_element(self.CONFI_PROFILE_EMAIL_HAVENT_RECEIVED).click()

    def select_confi_profile_email_buttonnext(self):
        self.wait_for_element(self.CONFI_PROFILE_EMAIL_BUTTONNEXT).click()

    def select_confi_profile_email_button_cancel(self):
        self.wait_for_element(self.CONFI_PROFILE_EMAIL_BUTTON_CANCEL).click()

    def select_confi_profile_new_email(self):
        self.wait_for_element(self.CONFI_PROFILE_NEW_EMAIL).click()

    def select_confi_profile_new_email_text(self, email):
        element = self.wait_for_element(self.CONFI_PROFILE_NEW_EMAIL)
        element.clear() 
        element.send_keys(email)

    def select_confi_profile_confirm_email(self):
        self.wait_for_element(self.CONFI_PROFILE_CONFIRM_EMAIL).click()

    def select_confi_profile_confirm_email_text(self, email):
        element = self.wait_for_element(self.CONFI_PROFILE_CONFIRM_EMAIL)
        element.clear() 
        element.send_keys(email)

    def select_confi_profile_save_email(self):
        self.wait_for_element(self.CONFI_PROFILE_SAVE_EMAIL).click()

    def select_confi_profile_cancel_email(self):
        self.wait_for_element(self.CONFI_PROFILE_CANCEL_EMAIL).click()

    def text_code_new(self):
        self.wait_for_element(self.CONFI_PROFILE_EMAIL_NEW_CODEONE).click()

    def get_code1_new(self, code1):
        element = self.wait_for_element(self.CONFI_PROFILE_EMAIL_NEW_CODEONE)
        element.clear() 
        element.send_keys(code1)

    def get_code2_new(self, code2):
        element = self.wait_for_element(self.CONFI_PROFILE_EMAIL_NEW_CODETWO)
        element.clear() 
        element.send_keys(code2)

    def get_code3_new(self, code3):
        element = self.wait_for_element(self.CONFI_PROFILE_EMAIL_NEW_CODETHREE)
        element.clear() 
        element.send_keys(code3)

    def get_code4_new(self, code4):
        element = self.wait_for_element(self.CONFI_PROFILE_EMAIL_NEW_CODEFOUR)
        element.clear() 
        element.send_keys(code4)

    def get_code5_new(self, code5):
        element = self.wait_for_element(self.CONFI_PROFILE_EMAIL_NEW_CODEFIVE)
        element.clear() 
        element.send_keys(code5)
        
    def get_code6_new(self, code6):
        element = self.wait_for_element(self.CONFI_PROFILE_EMAIL_NEW_CODESIX)
        element.clear() 
        element.send_keys(code6)

    def select_confi_profile_email_new_resendcode(self):
        self.wait_for_element(self.CONFI_PROFILE_EMAIL_NEW_RESENDCODE).click()

    def select_confi_profile_email_new_havent_received(self):
        self.wait_for_element(self.CONFI_PROFILE_EMAIL_NEW_HAVENT_RECEIVED).click()

    def select_confi_profile_email_new_buttonnext(self):
        self.wait_for_element(self.CONFI_PROFILE_EMAIL_NEW_BUTTONNEXT).click()

    def select_confi_profile_email_new_button_cancel(self):
        self.wait_for_element(self.CONFI_PROFILE_EMAIL_NEW_BUTTON_CANCEL).click()

    def select_confi_profile_dialog_email_yes(self):
        self.wait_for_element(self.CONFI_PROFILE_DIALOG_EMAIL_YES).click()

    def select_confi_profile_dialog_email_not(self):
        self.wait_for_element(self.CONFI_PROFILE_DIALOG_EMAIL_NOT).click()

    #Perfil contraseña
    def select_confi_profile_email_and_password(self):
        self.wait_for_element(self.CONFI_PROFILE_EDIT_PASSWORD).click()

    def select_confi_profile_current_password(self):
        self.wait_for_element(self.CONFI_PROFILE_CURRENT_PASSWORD).click()

    def select_confi_profile_current_password_text(self, password):
        element = self.wait_for_element(self.CONFI_PROFILE_CURRENT_PASSWORD)
        element.clear() 
        element.send_keys(password)

    def select_confi_profile_new_password(self):
        self.wait_for_element(self.CONFI_PROFILE_NEW_PASSWORD).click()

    def select_confi_profile_new_password_text(self, newpassword):
        element = self.wait_for_element(self.CONFI_PROFILE_NEW_PASSWORD)
        element.clear() 
        element.send_keys(newpassword)   

    def select_confi_profile_confirm_password(self):
        self.wait_for_element(self.CONFI_PROFILE_CONFIRM_PASSWORD).click() 

    def select_confi_profile_confirm_password_text(self, newpassword):
        element = self.wait_for_element(self.CONFI_PROFILE_CONFIRM_PASSWORD)
        element.clear() 
        element.send_keys(newpassword) 

    def select_confi_profile_save_password(self):
        self.wait_for_element(self.CONFI_PROFILE_SAVE_PASSWORD).click()

    def select_confi_profile_cancel_password(self):
        self.wait_for_element(self.CONFI_PROFILE_CANCEL_PASSWORD).click()

    def select_confi_profile_dialog_password_yes(self):
        self.wait_for_element(self.CONFI_PROFILE_DIALOG_PASSWORD_YES).click()

    def select_confi_profile_dialog_password_not(self):
        self.wait_for_element(self.CONFI_PROFILE_DIALOG_PASSWORD_NOT).click()

    #Perfil Contact and Location Information
    def select_confi_profile_contact_location(self):
        self.wait_for_element(self.CONFI_PROFILE_CONTACT_LOCATION).click()

    def select_confi_profile_country(self):
        self.wait_for_element(self.CONFI_PROFILE_COUNTRY).click()

    def select_confi_profile_new_country(self):
        self.wait_for_element(self.CONFI_PROFILE_NEW_COUNTRY).click()

    def select_confi_profile_country_code(self):
        self.wait_for_element(self.CONFI_PROFILE_COUNTRY_CODE).click()

    def select_confi_profile_new_country_code(self):
        self.wait_for_element(self.CONFI_PROFILE_NEW_COUNTRY_CODE).click()

    def select_confi_profile_x_phone(self):
        self.wait_for_element(self.CONFI_PROFILE_X_PHONE).click()

    def select_confi_profile_phone(self):
        self.wait_for_element(self.CONFI_PROFILE_PHONE).click()

    def select_confi_profile_phone_text(self, phone):
        element = self.wait_for_element(self.CONFI_PROFILE_PHONE)
        element.clear() 
        element.send_keys(phone) 

    def select_confi_profile_language(self):
        self.wait_for_element(self.CONFI_PROFILE_LANGUAGE).click()

    def select_confi_profile_new_language(self):
        self.wait_for_element(self.CONFI_PROFILE_NEW_LANGUAGE).click()

    def select_confi_profile_save_contact_location(self):
        self.wait_for_element(self.CONFI_PROFILE_SAVE_CONTACT_LOCATION).click()

    def select_confi_profile_cancel_contact_location(self):
        self.wait_for_element(self.CONFI_PROFILE_CANCEL_CONTACT_LOCATION).click()

    def select_confi_profile_dialog_contact_location_yes(self):
        self.wait_for_element(self.CONFI_PROFILE_DIALOG_CONTACT_LOCATION_YES).click()

    def select_confi_profile_dialog_contact_location_not(self):
        self.wait_for_element(self.CONFI_PROFILE_DIALOG_CONTACT_LOCATION_NOT).click()

    