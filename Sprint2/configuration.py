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
    CONFIGURATION_PROFILE = (By.XPATH, "(//span[contains(@class,'1')])[17]")
    CONFI_PROFILE_LOGIN_DATA = (By.XPATH, "")
    CONFI_PROFILE_EMAIL = (By.XPATH, "")
    CONFI_PROFILE_EMAIL_BUTTONCHECK = (By.XPATH, "")
    CONFI_PROFILE_EMAIL_BUTTONCONTINUE = (By.XPATH, "")
    CONFI_PROFILE_EMAIL_BUTTONCANCEL = (By.XPATH, "")
    CONFI_PROFILE_EMAIL_CODE = (By.XPATH, "")
    CONFI_PROFILE_EMAIL_BUTTONNEXT = (By.XPATH, "")
    CONFI_PROFILE_EMAIL_BUTTON_CANCEL = (By.XPATH, "")
    CONFI_PROFILE_NEW_EMAIL = (By.XPATH, "")
    CONFI_PROFILE_CONFIRM_EMAIL = (By.XPATH, "")