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

    #Seleccion de canales
    def select_configuration_channelS(self):
        self.wait_for_element(self.CONFIGURATION_CHANNELS).click()

    def select_confi_channels_3_points(self):
        self.wait_for_element(self.CONFI_CHANNELS_3_POINTS).click()

    def select_confi_channels_edit_channel1_button(self):
        self.wait_for_element(self.CONFI_CHANNELS_EDIT_CHANNEL1_BUTTON).click()

    def select_confi_channels_edit_url_x(self):
        self.wait_for_element(self.CONFI_CHANNELS_EDIT_URL_X).click()

    def select_confi_channels_edit_url(self, URL):
        element = self.wait_for_element(self.CONFI_CHANNELS_EDIT_URL)
        element.clear() 
        element.send_keys(URL) 

    def select_confi_channels_edit_name_x(self):
        self.wait_for_element(self.CONFI_CHANNELS_EDIT_NAME_X).click()

    def select_confi_channels_edit_name(self, name):
        element = self.wait_for_element(self.CONFI_CHANNELS_EDIT_NAME)
        element.clear() 
        element.send_keys(name) 

    def select_confi_channels_edit_save(self):
        self.wait_for_element(self.CONFI_CHANNELS_EDIT_SAVE).click()

    def select_confi_channels_edit_cancel(self):
        self.wait_for_element(self.CONFI_CHANNELS_EDIT_CANCEL).click()

    def select_confi_channels_edit_channel1_yes(self):
        self.wait_for_element(self.CONFI_CHANNELS_EDIT_CHANNEL1_YES).click()

    def select_confi_channels_edit_channel1_not(self):
        self.wait_for_element(self.CONFI_CHANNELS_EDIT_CHANNEL1_NOT).click()

    def select_confi_channels_add_new_channel(self):
        self.wait_for_element(self.CONFI_CHANNELS_ADD_NEW_CHANNEL).click()

    def select_confi_channels_new_url_click(self):
        self.wait_for_element(self.CONFI_CHANNELS_NEW_URL).click()

    def select_confi_channels_new_url(self, URL):
        element = self.wait_for_element(self.CONFI_CHANNELS_NEW_URL)
        element.clear() 
        element.send_keys(URL) 

    def select_confi_channels_new_name_click(self):
        self.wait_for_element(self.CONFI_CHANNELS_NEW_NAME).click()

    def select_confi_channels_new_name(self, name):
        element = self.wait_for_element(self.CONFI_CHANNELS_NEW_NAME)
        element.clear() 
        element.send_keys(name) 

    def select_confi_channels_save_new_channel(self):
        self.wait_for_element(self.CONFI_CHANNELS_SAVE_NEW_CHANNEL).click()

    def select_confi_channels_cancel_new_channel(self):
        self.wait_for_element(self.CONFI_CHANNELS_CANCEL_NEW_CHANNEL).click()

    def select_confi_channels_delete_channel(self):
        self.wait_for_element(self.CONFI_CHANNELS_DELETE_CHANNEL).click()

    def select_confi_channels_delete_channel_yes(self):
        self.wait_for_element(self.CONFI_CHANNELS_DELETE_CHANNEL_YES).click()

    def select_confi_channels_delete_channel_not(self):
        self.wait_for_element(self.CONFI_CHANNELS_DELETE_CHANNEL_NOT).click()