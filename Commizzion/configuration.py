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
    CONFI_PROFILE_EMAIL = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/section/div[2]/div/span[2]/span[2]/button")
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
    CONFI_PROFILE_NEW_PASSWORD = (By.XPATH, "(//div[contains(@class,'7')])[5]")
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
    #Seleccion de canales
    CONFIGURATION_CHANNELS = (By.XPATH, "(//span[contains(@class,'1')])[18]")
    CONFI_CHANNELS_3_POINTS = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/main/div/section/div[1]/div[1]/div[5]/div/button")
    CONFI_CHANNELS_EDIT_CHANNEL1_BUTTON = (By.XPATH, "(//span[contains(@class,'137')])[15]")
    CONFI_CHANNELS_EDIT_URL_X = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/main/div/section/div[1]/div[2]/div/div/section/form/div[1]/div[1]/fieldset/label/div/i")
    CONFI_CHANNELS_EDIT_URL = (By.XPATH, "//input[@name='url']")
    CONFI_CHANNELS_EDIT_NAME_X = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/main/div/section/div[1]/div[2]/div/div/section/form/div[1]/div[2]/fieldset/label/div/i")
    CONFI_CHANNELS_EDIT_NAME = (By.XPATH, "//input[@name='name']")
    CONFI_CHANNELS_EDIT_SAVE = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/main/div/section/div[1]/div[2]/div/div/section/form/div[2]/button[2]")
    CONFI_CHANNELS_EDIT_CANCEL = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/main/div/section/div[2]/div[2]/div/div/section/form/div[2]/button[1]")
    CONFI_CHANNELS_EDIT_CHANNEL1_YES = (By.XPATH, "//button[contains(@class,'163')]")
    CONFI_CHANNELS_EDIT_CHANNEL1_NOT = (By.XPATH, "//button[contains(@class,'224')]")
    CONFI_CHANNELS_ADD_NEW_CHANNEL = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/main/div/section/div[3]/div/div[4]/div/button")
    CONFI_CHANNELS_NEW_URL = (By.XPATH, "(//input[@name='url'])[2]")
    CONFI_CHANNELS_NEW_NAME = (By.XPATH, "(//input[@name='name'])[2]")
    CONFI_CHANNELS_SAVE_NEW_CHANNEL = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/main/div/section/div[2]/section/form/div[2]/button[2]")
    CONFI_CHANNELS_CANCEL_NEW_CHANNEL = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/main/div/section/div[2]/section/form/div[2]/button[2]")
    CONFI_CHANNELS_DELETE_CHANNEL = (By.XPATH, "(//span[contains(@class,'137')])[16]")
    CONFI_CHANNELS_DELETE_CHANNEL_YES = (By.XPATH, "//button[contains(@class,'158')]")
    CONFI_CHANNELS_DELETE_CHANNEL_NOT = (By.XPATH, "//button[contains(@class,'220')]")
    #Sleccion de preferencias
    CONFIGURATION_PREFERENCES = (By.XPATH, "(//span[contains(@class,'73')])[3]")
    CONFI_PREFERENCES_AUDIENCE_COUNTRIES = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/section/div[2]/div[1]/div/button")
    CONFI_PREFERENCES_AUDIENCE_COUNTRIES_X = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/section/div[2]/div[2]/div[1]/div/label[1]/span/i")
    CONFI_PREFERENCES_AUDIENCE_COUNTRIES_PLACEHOLDER = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/section/div[2]/div[2]/div[2]/fieldset/label/div/div")
    CONFI_PREFERENCES_AUDIENCE_COUNTRIES_MORE_COUNTRIES = (By.XPATH, "//button[contains(@class,'76')]")
    CONFI_PREFERENCES_AUDIENCE_COUNTRIES_CHIPS = (By.XPATH, "(//span[contains(@class,'153')])[29]")
    CONFI_PREFERENCES_AUDIENCE_COUNTRIES_SAVE = (By.XPATH, "//button[contains(@class,'42')]")
    CONFI_PREFERENCES_AUDIENCE_COUNTRIES_CANCEL = (By.XPATH, "(//button[contains(@class,'58')])[4]")
    CONFI_PREFERENCES_AUDIENCE_COUNTRIES_YES = (By.XPATH, "//button[contains(@class,'163')]")
    CONFI_PREFERENCES_AUDIENCE_COUNTRIES_NOT = (By.XPATH, "//button[contains(@class,'224')]")
    CONFI_PREFERENCES_OBJETIVE = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/section/div[3]/div[1]/div/button")
    CONFI_PREFERENCES_OBJ_SELECT = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/section/div[3]/div[2]/div[1]/div[1]")
    CONFI_PREFERENCES_AUDIENCE_OBJETIVE_SAVE = (By.XPATH, "(//button[contains(@class,'42')])[2]")
    CONFI_PREFERENCES_AUDIENCE_OBJETIVE_CANCEL = (By.XPATH, "(//button[contains(@class,'58')])[5]")
    CONFI_PREFERENCES_AUDIENCE_OBJETIVE_YES = (By.XPATH, "//button[contains(@class,'163')]")
    CONFI_PREFERENCES_AUDIENCE_OBJETIVE_NOT = (By.XPATH, "//button[contains(@class,'224')]")
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

    #Perfil correo
    def select_CONFI_PROFILE_LOGIN_DATA(self):
        self.wait_for_element(self.CONFI_PROFILE_LOGIN_DATA).click()

    def select_CONFI_PROFILE_EMAIL(self):
        self.wait_for_element(self.CONFI_PROFILE_EMAIL).click()

    def select_CONFI_PROFILE_EMAIL_BUTTONCHECK(self):
        self.wait_for_element(self.CONFI_PROFILE_EMAIL_BUTTONCHECK).click()

    def select_CONFI_PROFILE_EMAIL_BUTTONCONTINUE(self):
        self.wait_for_element(self.CONFI_PROFILE_EMAIL_BUTTONCONTINUE).click()

    def select_CONFI_PROFILE_EMAIL_BUTTONCANCE(self):
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

    def select_CONFI_PROFILE_EMAIL_RESENDCODE(self):
        self.wait_for_element(self.CONFI_PROFILE_EMAIL_RESENDCODE).click()

    def select_CONFI_PROFILE_EMAIL_HAVENT_RECEIVED(self):
        self.wait_for_element(self.CONFI_PROFILE_EMAIL_HAVENT_RECEIVED).click()

    def select_CONFI_PROFILE_EMAIL_BUTTONNEXT(self):
        self.wait_for_element(self.CONFI_PROFILE_EMAIL_BUTTONNEXT).click()

    def select_CONFI_PROFILE_EMAIL_BUTTON_CANCEL(self):
        self.wait_for_element(self.CONFI_PROFILE_EMAIL_BUTTON_CANCEL).click()

    def select_CONFI_PROFILE_NEW_EMAIL(self):
        self.wait_for_element(self.CONFI_PROFILE_NEW_EMAIL).click()

    def select_CONFI_PROFILE_NEW_EMAIL(self, email):
        element = self.wait_for_element(self.CONFI_PROFILE_NEW_EMAIL)
        element.clear() 
        element.send_keys(email)

    def select_CONFI_PROFILE_CONFIRM_EMAIL(self):
        self.wait_for_element(self.CONFI_PROFILE_CONFIRM_EMAIL).click()

    def select_CONFI_PROFILE_NEW_EMAIL(self, email):
        element = self.wait_for_element(self.CONFI_PROFILE_CONFIRM_EMAIL)
        element.clear() 
        element.send_keys(email)

    def select_CONFI_PROFILE_SAVE_EMAIL(self):
        self.wait_for_element(self.CONFI_PROFILE_SAVE_EMAIL).click()

    def select_CONFI_PROFILE_CANCEL_EMAIL(self):
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

    def select_CONFI_PROFILE_EMAIL_NEW_RESENDCODE(self):
        self.wait_for_element(self.CONFI_PROFILE_EMAIL_NEW_RESENDCODE).click()

    def select_CONFI_PROFILE_EMAIL_NEW_HAVENT_RECEIVED(self):
        self.wait_for_element(self.CONFI_PROFILE_EMAIL_NEW_HAVENT_RECEIVED).click()

    def select_CONFI_PROFILE_EMAIL_NEW_BUTTONNEXT(self):
        self.wait_for_element(self.CONFI_PROFILE_EMAIL_NEW_BUTTONNEXT).click()

    def select_CONFI_PROFILE_EMAIL_NEW_BUTTON_CANCEL(self):
        self.wait_for_element(self.CONFI_PROFILE_EMAIL_NEW_BUTTON_CANCEL).click()

    def select_CONFI_PROFILE_DIALOG_EMAIL_YES(self):
        self.wait_for_element(self.CONFI_PROFILE_DIALOG_EMAIL_YES).click()

    def select_CONFI_PROFILE_DIALOG_EMAIL_NOT(self):
        self.wait_for_element(self.CONFI_PROFILE_DIALOG_EMAIL_NOT).click()

    #Perfil contraseña
    def select_CONFI_PROFILE_EDIT_PASSWORD(self):
        self.wait_for_element(self.CONFI_PROFILE_EDIT_PASSWORD).click()

    def select_CONFI_PROFILE_CURRENT_PASSWORD(self):
        self.wait_for_element(self.CONFI_PROFILE_CURRENT_PASSWORD).click()

    def select_CONFI_PROFILE_CURRENT_PASSWORD_text(self, password):
        element = self.wait_for_element(self.CONFI_PROFILE_CURRENT_PASSWORD)
        element.clear() 
        element.send_keys(password)

    def select_CONFI_PROFILE_NEW_PASSWORD(self):
        self.wait_for_element(self.CONFI_PROFILE_NEW_PASSWORD).click()

    def select_CONFI_PROFILE_NEW_PASSWORD_text(self, newpassword):
        element = self.wait_for_element(self.CONFI_PROFILE_NEW_PASSWORD)
        element.clear() 
        element.send_keys(newpassword)   

    def select_CONFI_PROFILE_CONFIRM_PASSWORD(self):
        self.wait_for_element(self.CONFI_PROFILE_CONFIRM_PASSWORD).click() 

    def select_CONFI_PROFILE_CONFIRM_PASSWORD_text(self, newpassword):
        element = self.wait_for_element(self.CONFI_PROFILE_CONFIRM_PASSWORD)
        element.clear() 
        element.send_keys(newpassword) 

    def select_CONFI_PROFILE_SAVE_PASSWORD(self):
        self.wait_for_element(self.CONFI_PROFILE_SAVE_PASSWORD).click()

    def select_CONFI_PROFILE_CANCEL_PASSWORD(self):
        self.wait_for_element(self.CONFI_PROFILE_CANCEL_PASSWORD).click()

    def select_CONFI_PROFILE_DIALOG_PASSWORD_YES(self):
        self.wait_for_element(self.CONFI_PROFILE_DIALOG_PASSWORD_YES).click()

    def select_CONFI_PROFILE_DIALOG_PASSWORD_NOT(self):
        self.wait_for_element(self.CONFI_PROFILE_DIALOG_PASSWORD_NOT).click()

    #Perfil Contact and Location Information
    def select_CONFI_PROFILE_CONTACT_LOCATION(self):
        self.wait_for_element(self.CONFI_PROFILE_CONTACT_LOCATION).click()

    def select_CONFI_PROFILE_COUNTRY(self):
        self.wait_for_element(self.CONFI_PROFILE_COUNTRY).click()

    def select_CONFI_PROFILE_NEW_COUNTRY(self):
        self.wait_for_element(self.CONFI_PROFILE_NEW_COUNTRY).click()

    def select_CONFI_PROFILE_COUNTRY_CODE(self):
        self.wait_for_element(self.CONFI_PROFILE_COUNTRY_CODE).click()

    def select_CONFI_PROFILE_NEW_COUNTRY_CODE(self):
        self.wait_for_element(self.CONFI_PROFILE_NEW_COUNTRY_CODE).click()

    def select_CONFI_PROFILE_X_PHONE(self):
        self.wait_for_element(self.CONFI_PROFILE_X_PHONE).click()

    def select_CONFI_PROFILE_PHONE(self):
        self.wait_for_element(self.CONFI_PROFILE_PHONE).click()

    def select_CONFI_PROFILE_PHONE_text(self, phone):
        element = self.wait_for_element(self.CONFI_PROFILE_PHONE)
        element.clear() 
        element.send_keys(phone) 

    def select_CONFI_PROFILE_LANGUAGE(self):
        self.wait_for_element(self.CONFI_PROFILE_LANGUAGE).click()

    def select_CONFI_PROFILE_NEW_LANGUAGE(self):
        self.wait_for_element(self.CONFI_PROFILE_NEW_LANGUAGE).click()

    def select_CONFI_PROFILE_SAVE_CONTACT_LOCATION(self):
        self.wait_for_element(self.CONFI_PROFILE_SAVE_CONTACT_LOCATION).click()

    def select_CONFI_PROFILE_CANCEL_CONTACT_LOCATION(self):
        self.wait_for_element(self.CONFI_PROFILE_CANCEL_CONTACT_LOCATION).click()

    def select_CONFI_PROFILE_DIALOG_CONTACT_LOCATION_YES(self):
        self.wait_for_element(self.CONFI_PROFILE_DIALOG_CONTACT_LOCATION_YES).click()

    def select_CONFI_PROFILE_DIALOG_CONTACT_LOCATION_NOT(self):
        self.wait_for_element(self.CONFI_PROFILE_DIALOG_CONTACT_LOCATION_NOT).click()

    #Seleccion de canales
    def select_CONFIGURATION_CHANNELS(self):
        self.wait_for_element(self.CONFIGURATION_CHANNELS).click()

    def select_CONFI_CHANNELS_3_POINTS(self):
        self.wait_for_element(self.CONFI_CHANNELS_3_POINTS).click()

    def select_CONFI_CHANNELS_EDIT_CHANNEL1_BUTTON(self):
        self.wait_for_element(self.CONFI_CHANNELS_EDIT_CHANNEL1_BUTTON).click()

    def select_CONFI_CHANNELS_EDIT_URL_X(self):
        self.wait_for_element(self.CONFI_CHANNELS_EDIT_URL_X).click()

    def select_CONFI_CHANNELS_EDIT_URL(self, URL):
        element = self.wait_for_element(self.CONFI_CHANNELS_EDIT_URL)
        element.clear() 
        element.send_keys(URL) 

    def select_CONFI_CHANNELS_EDIT_NAME_X(self):
        self.wait_for_element(self.CONFI_CHANNELS_EDIT_NAME_X).click()

    def select_CONFI_CHANNELS_EDIT_NAME(self, name):
        element = self.wait_for_element(self.CONFI_CHANNELS_EDIT_NAME)
        element.clear() 
        element.send_keys(name) 

    def select_CONFI_CHANNELS_EDIT_SAVE(self):
        self.wait_for_element(self.CONFI_CHANNELS_EDIT_SAVE).click()

    def select_CONFI_CHANNELS_EDIT_CANCEL(self):
        self.wait_for_element(self.CONFI_CHANNELS_EDIT_CANCEL).click()

    def select_CONFI_CHANNELS_EDIT_CHANNEL1_YES(self):
        self.wait_for_element(self.CONFI_CHANNELS_EDIT_CHANNEL1_YES).click()

    def select_CONFI_CHANNELS_EDIT_CHANNEL1_NOT(self):
        self.wait_for_element(self.CONFI_CHANNELS_EDIT_CHANNEL1_NOT).click()

    def select_CONFI_CHANNELS_ADD_NEW_CHANNEL(self):
        self.wait_for_element(self.CONFI_CHANNELS_ADD_NEW_CHANNEL).click()

    def select_CONFI_CHANNELS_NEW_URL_click(self):
        self.wait_for_element(self.CONFI_CHANNELS_NEW_URL).click()

    def select_CONFI_CHANNELS_NEW_URL(self, URL):
        element = self.wait_for_element(self.CONFI_CHANNELS_NEW_URL)
        element.clear() 
        element.send_keys(URL) 

    def select_CONFI_CHANNELS_NEW_NAME_click(self):
        self.wait_for_element(self.CONFI_CHANNELS_NEW_NAME).click()

    def select_CONFI_CHANNELS_NEW_NAME(self, name):
        element = self.wait_for_element(self.CONFI_CHANNELS_NEW_NAME)
        element.clear() 
        element.send_keys(name) 

    def select_CONFI_CHANNELS_SAVE_NEW_CHANNEL(self):
        self.wait_for_element(self.CONFI_CHANNELS_SAVE_NEW_CHANNEL).click()

    def select_CONFI_CHANNELS_CANCEL_NEW_CHANNEL(self):
        self.wait_for_element(self.CONFI_CHANNELS_CANCEL_NEW_CHANNEL).click()

    def select_CONFI_CHANNELS_DELETE_CHANNEL(self):
        self.wait_for_element(self.CONFI_CHANNELS_DELETE_CHANNEL).click()

    def select_CONFI_CHANNELS_DELETE_CHANNEL_YES(self):
        self.wait_for_element(self.CONFI_CHANNELS_DELETE_CHANNEL_YES).click()

    def select_CONFI_CHANNELS_DELETE_CHANNEL_NOT(self):
        self.wait_for_element(self.CONFI_CHANNELS_DELETE_CHANNEL_NOT).click()

    #Seleccion de preferencias paises
    def select_CONFIGURATION_PREFERENCES(self):
        self.wait_for_element(self.CONFIGURATION_PREFERENCES).click()

    def select_CONFI_PREFERENCES_AUDIENCE_COUNTRIES(self):
        self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_COUNTRIES).click()

    def select_CONFI_PREFERENCES_AUDIENCE_COUNTRIES_X(self):
        self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_COUNTRIES_X).click()

    def select_CONFI_PREFERENCES_AUDIENCE_COUNTRIES_PLACEHOLDER_click(self):
        self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_COUNTRIES_PLACEHOLDER).click()

    def select_CONFI_PREFERENCES_AUDIENCE_COUNTRIES_PLACEHOLDER(self, country):
        element = self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_COUNTRIES_PLACEHOLDER)
        element.clear() 
        element.send_keys(country) 

    def select_CONFI_PREFERENCES_AUDIENCE_COUNTRIES_MORE_COUNTRIES(self):
        self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_COUNTRIES_MORE_COUNTRIES).click()

    def select_CONFI_PREFERENCES_AUDIENCE_COUNTRIES_CHIPS(self):
        self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_COUNTRIES_CHIPS).click()

    def select_CONFI_PREFERENCES_AUDIENCE_COUNTRIES_SAVE(self):
        self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_COUNTRIES_SAVE).click()

    def select_CONFI_PREFERENCES_AUDIENCE_COUNTRIES_CANCEL(self):
        self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_COUNTRIES_CANCEL).click()

    def select_CONFI_PREFERENCES_AUDIENCE_COUNTRIES_YES(self):
        self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_COUNTRIES_YES).click()

    def select_CONFI_PREFERENCES_AUDIENCE_COUNTRIES_NOT(self):
        self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_COUNTRIES_NOT).click()

    #Seleccion de preferencias objetivos
    def select_CONFI_PREFERENCES_OBJETIVE(self):
        self.wait_for_element(self.CONFI_PREFERENCES_OBJETIVE).click()

    def select_CONFI_PREFERENCES_OBJ_SELECT(self):
        self.wait_for_element(self.CONFI_PREFERENCES_OBJ_SELECT).click()

    def select_CONFI_PREFERENCES_AUDIENCE_OBJETIVE_SAVE(self):
        self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_OBJETIVE_SAVE).click()

    def select_CONFI_PREFERENCES_AUDIENCE_OBJETIVE_CANCEL(self):
        self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_OBJETIVE_CANCEL).click()

    def select_CONFI_PREFERENCES_AUDIENCE_OBJETIVE_YES(self):
        self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_OBJETIVE_YES).click()

    def select_CONFI_PREFERENCES_AUDIENCE_OBJETIVE_NOT(self):
        self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_OBJETIVE_NOT).click()

    #Configuración ayuda
    def select_CONFIGURATION_HELP(self):
        self.wait_for_element(self.CONFIGURATION_HELP).click()

    def select_CONFI_HELP_CALL(self):
        self.wait_for_element(self.CONFI_HELP_CALL).click()

    def select_CONFI_HELP_CHAT(self):
        self.wait_for_element(self.CONFI_HELP_CHAT).click()

    def select_CONFI_HELP_POLICIES_TYC(self):
        self.wait_for_element(self.CONFI_HELP_POLICIES_TYC).click()

    def select_CONFI_HELP_POLICIES_PRIVACY_POLICY(self):
        self.wait_for_element(self.CONFI_HELP_POLICIES_PRIVACY_POLICY).click()

    def select_CONFI_HELP_POLICIES_ISO(self):
        self.wait_for_element(self.CONFI_HELP_POLICIES_ISO).click()
    
    