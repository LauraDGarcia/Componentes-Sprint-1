from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class campaignspage(BasePage):
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
    CONFI_PROFILE_COUNTRY = (By.XPATH, "/html/body/div[4]/div[3]/form/div[2]/fieldset[1]/label/div/i[2]")
    CONFI_PROFILE_NEW_COUNTRY = (By.XPATH, "//span[contains(.,'Colombia')]")
    CONFI_PROFILE_COUNTRY_CODE = (By.XPATH, "/html/body/div[4]/div[3]/form/div[2]/span/fieldset[1]/label/div/i[2]")
    CONFI_PROFILE_NEW_COUNTRY_CODE = (By.XPATH, "(//span[contains(.,'+57')])[2]")
    CONFI_PROFILE_X_PHONE = (By.XPATH, "/html/body/div[4]/div[3]/form/div[2]/span/fieldset[2]/label/div/i")
    CONFI_PROFILE_PHONE = (By.XPATH, "//input[@name='phone']")
    CONFI_PROFILE_LANGUAGE = (By.XPATH, "/html/body/div[4]/div[3]/form/div[2]/fieldset[2]/label/div/i")
    CONFI_PROFILE_NEW_LANGUAGE = (By.XPATH, "(//li[contains(@class,'1 undefined')])[1]")
    CONFI_PROFILE_SAVE_CONTACT_LOCATION  = (By.XPATH, "//button[contains(@class,'42')]")
    CONFI_PROFILE_CANCEL_CONTACT_LOCATION  = (By.XPATH, "//button[contains(@class,'76')]")
    CONFI_PROFILE_DIALOG_CONTACT_LOCATION_YES = (By.XPATH, "//button[contains(@class,'163')]")
    CONFI_PROFILE_DIALOG_CONTACT_LOCATION_NOT = (By.XPATH, "//button[contains(@class,'224')]")
    #Seleccion de canales
    CONFIGURATION_CHANNELS = (By.XPATH, "(//span[contains(@class,'1')])[17]")
    CONFI_CHANNELS_3_POINTS = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/main/div/section/div[1]/div[1]/div[5]/div/button")
    CONFI_CHANNELS_EDIT_CHANNEL1_BUTTON = (By.XPATH, "(//span[contains(@class,'137')])[15]")
    CONFI_CHANNELS_EDIT_URL_X = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/main/div/section/div[1]/div[2]/div/div/section/form/div[1]/div[1]/fieldset/label/div/i")
    CONFI_CHANNELS_EDIT_URL = (By.XPATH, "//input[@name='url']")
    CONFI_CHANNELS_EDIT_NAME_X = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/main/div/section/div[1]/div[2]/div/div/section/form/div[1]/div[2]/fieldset/label/div/i")
    CONFI_CHANNELS_EDIT_NAME = (By.XPATH, "//input[@name='name']")
    CONFI_CHANNELS_EDIT_SAVE = (By.XPATH, "//span[contains(.,'Save')]")
    CONFI_CHANNELS_EDIT_CANCEL = (By.XPATH, "//span[contains(.,'Cancel')]")
    CONFI_CHANNELS_EDIT_CHANNEL1_YES = (By.XPATH, "//button[contains(@class,'163')]")
    CONFI_CHANNELS_EDIT_CHANNEL1_NOT = (By.XPATH, "//button[contains(@class,'224')]")
    CONFI_CHANNELS_ADD_NEW_CHANNEL = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/main/div/section/div[2]/div/div[4]/div/button")
    CONFI_CHANNELS_NEW_URL = (By.XPATH, "(//input[@name='url'])[2]")
    CONFI_CHANNELS_NEW_NAME = (By.XPATH, "(//input[@name='name'])[2]")
    CONFI_CHANNELS_SAVE_NEW_CHANNEL = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/main/div/section/div[2]/section/form/div[2]/button[2]")
    CONFI_CHANNELS_CANCEL_NEW_CHANNEL = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/main/div/section/div[2]/section/form/div[2]/button[2]")
    CONFI_CHANNELS_DELETE_CHANNEL = (By.XPATH, "(//span[contains(@class,'137')])[16]")
    #Sleccion de preferencias
    CONFIGURATION_PREFERENCES = (By.XPATH, "(//span[contains(@class,'73')])[3]")
    CONFI_PREFERENCES_AUDIENCE_COUNTRIES = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/section/div[2]/div[1]/div/button")
    CONFI_PREFERENCES_AUDIENCE_COUNTRIES_X = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/section/div[2]/div[2]/div[1]/div/label[1]/span/i")
    CONFI_PREFERENCES_AUDIENCE_COUNTRIES_PLACEHOLDER = (By.XPATH, "//input[contains(@placeholder,'Search country')]")
    CONFI_PREFERENCES_AUDIENCE_COUNTRIES_MORE_COUNTRIES = (By.XPATH, "//button[contains(@class,'76')]")
    CONFI_PREFERENCES_AUDIENCE_COUNTRIES_CHIPS = (By.XPATH, "//button[contains(@class,'76')]")
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
    CONFIGURATION_HELP = (By.XPATH, "")
    CONFI_HELP_CALL = (By.XPATH, "")
    CONFI_HELP_CHAT = (By.XPATH, "")
    CONFI_HELP_POLICIES_TYC = (By.XPATH, "")
    CONFI_HELP_POLICIES_PRIVACY_POLICY = (By.XPATH, "")
    CONFI_HELP_POLICIES_ISO = (By.XPATH, "")

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

