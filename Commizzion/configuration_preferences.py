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
    #Sleccion de preferencias
    CONFIGURATION_PREFERENCES = (By.XPATH, "(//span[contains(@class,'73')])[3]")
    CONFI_PREFERENCES_AUDIENCE_COUNTRIES = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/section/div[2]/div[1]/div/button")
    CONFI_PREFERENCES_AUDIENCE_COUNTRIES_X = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/section/div[2]/div[2]/div[1]/div/label[1]/span/i")
    CONFI_PREFERENCES_AUDIENCE_COUNTRIES_PLACEHOLDER = (By.XPATH, "//input[contains(@placeholder,'Buscar país')]")
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

    #Seleccion de preferencias paises
    def select_configuration_preferences(self):
        self.wait_for_element(self.CONFIGURATION_PREFERENCES).click()

    def select_confi_preferences_audience_countries(self):
        self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_COUNTRIES).click()

    def select_confi_preferences_audience_countries_x(self):
        self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_COUNTRIES_X).click()

    def select_confi_preferences_audience_countries_placeholder_click(self):
        self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_COUNTRIES_PLACEHOLDER).click()

    def select_confi_preferences_audience_countries_placeholder(self, country):
        element = self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_COUNTRIES_PLACEHOLDER)
        element.clear() 
        element.send_keys(country) 

    def select_confi_preferences_audience_countries_more_countries(self):
        self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_COUNTRIES_MORE_COUNTRIES).click()

    def select_confi_preferences_audience_countries_chips(self):
        self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_COUNTRIES_CHIPS).click()

    def select_confi_preferences_audience_countries_save(self):
        self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_COUNTRIES_SAVE).click()

    def select_confi_preferences_audience_countries_cancel(self):
        self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_COUNTRIES_CANCEL).click()

    def select_confi_preferences_audience_countries_yes(self):
        self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_COUNTRIES_YES).click()

    def select_confi_preferences_audience_countries_not(self):
        self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_COUNTRIES_NOT).click()

    #Seleccion de preferencias objetivos
    def select_confi_preferences_objetive(self):
        self.wait_for_element(self.CONFI_PREFERENCES_OBJETIVE).click()

    def select_confi_preferences_obj_select(self):
        self.wait_for_element(self.CONFI_PREFERENCES_OBJ_SELECT).click()

    def select_confi_preferences_audience_objetive_save(self):
        self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_OBJETIVE_SAVE).click()

    def select_confi_preferences_audience_objetive_cancel(self):
        self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_OBJETIVE_CANCEL).click()

    def select_confi_preferences_audience_objetive_yes(self):
        self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_OBJETIVE_YES).click()

    def select_confi_preferences_audience_objetive_not(self):
        self.wait_for_element(self.CONFI_PREFERENCES_AUDIENCE_OBJETIVE_NOT).click()