from selenium.webdriver.common.by import By
from .base_page import BasePage

class signinpage(BasePage):
    EMAIL_GOOGLE = (By.XPATH, "")
    SELECT_ACCOUNT = (By.XPATH, "")
    NEXT_BUTTON_ONE = (By.XPATH, "")
    CANCEL_BUTTON_ONE = (By.XPATH, "")
    SELECT_EMAIL = (By.XPATH, "")
    NAME = (By.XPATH, "")
    LASTNAME = (By.XPATH, "")
    EMAIL = (By.XPATH, "")
    PHONE_INDICATOR = (By.XPATH, "")
    PHONE = (By.XPATH, "")
    PASSWORD = (By.XPATH, "")
    CONFIRM_PASSWORD = (By.XPATH, "")
    CAPTCHA_CHECKBOX = (By.XPATH, "")
    TYC_CHECKBOX = (By.XPATH, "")
    NEXT_BUTTON_TWO = (By.XPATH, "")
    #verificación de correo
    DIALOG = (By.XPATH, "")
    CODE = (By.XPATH, "")
    RESEND_CODE = (By.XPATH, "")
    CODE_NOT_YET_RECEIVED = (By.XPATH, "")
    NEXT_BUTTON_THREE = (By.XPATH, "")
    #Stepper canal de comunicación
    ADD_NETWORKS = (By.XPATH, "")
    LINK = (By.XPATH, "")
    CHANNEL_NAME =(By.XPATH, "")
    ADD_CHANNEL_BUTTON = (By.XPATH, "")
    CANCEL_BUTTON_TWO = (By.XPATH, "")
    NEXT_BUTTON_FOUR = (By.XPATH, "")
    #Tipo de usuario
    TOOLTIP_USER = (By.XPATH, "")
    TOOLTIP_OTHER_ONE = (By.XPATH, "")
    TEXT_FIELD = (By.XPATH, "")
    PREVIOUS_BUTTON_ONE = (By.XPATH, "")
    NEXT_BUTTON_FIVE = (By.XPATH, "")
    #Queremos saber más
    CHIPS = (By.XPATH, "")
    TOOLTIP_OTHER_TWO = (By.XPATH, "")
    PREVIOUS_BUTTON_TWO = (By.XPATH, "")
    NEXT_BUTTON_SIX = (By.XPATH, "")
    #paises de audiencia
    COUNTRIES_CHIPS_AMERICA = (By.XPATH, "")
    COUNTRIES_CHIPS_EUROPA = (By.XPATH, "")
    COUNTRIES_CHIPS_ASIA = (By.XPATH, "")
    COUNTRIES_CHIPS_AFRICA = (By.XPATH, "")
    PREVIOUS_BUTTON_THREE = (By.XPATH, "")
    NEXT_BUTTON_SEVEN = (By.XPATH, "")
    #Objetivos
    CHIPOBJETIVES = (By.XPATH, "")
    PREVIOUS_BUTTON_FOUR = (By.XPATH, "")
    SAVE_BUTTON = (By.XPATH, "")
    
    def navigate_home(self):
        self.go_to_page("##poner la url correspóndiente cuando llegue el momento##")

    def  select_dropdown(self, locator, index):
        self.select_dropdown_by_visible_text(self.localizador )       

    #Crear cuanta con google


    #Crear cuenta con correo y llenado de formulario


    #Verificación de correo


    #Perfilamiento canales 


    #Perfilamiento tipo de usuario 


    #Perfilamiento de trafico


    #Perfilamiento de pais


    #Perfilamiento de objetivos 


