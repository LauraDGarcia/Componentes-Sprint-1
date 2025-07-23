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
    #modal para llenar los
    MODAL_ACEPT = (By.XPATH, "(//button[contains(@class,'70')])[2]")
    MODAL_REJECT = (By.XPATH, "(//button[contains(@class,'70')])[1]")
    #seleccionar la pestaña de configuración
    CONFIGURATION = (By.XPATH, "(//span[contains(@class,'vDxV3')])[1]")
    #ir a cuentas
    ACCOUNT = (By.XPATH, "(//span[contains(@class,'65')])[2]")
    #Documentos
    DOCUMENTS = (By.XPATH, "(//button[contains(@class,'nq')])[1]")
    NATURAL = (By.XPATH, "(//div[contains(@class,'L39ya')])[1]")
    LEGAL = (By.XPATH, "(//div[contains(@class,'L39ya')])[2]")
    FRONT_DOC = (By.XPATH, "(//p[contains(@class,'51')])[1]")
    BACK_DOC = (By.XPATH, "(//p[contains(@class,'51')])[2]")
    SELFIE = (By.XPATH, "(//p[contains(@class,'51')])[3]")
    BUTTON_SAVE1 = (By.XPATH, "//button[contains(@class,'42')]")
    BUTTON_BACK1 = (By.XPATH, "//button[contains(@class,'76')]")
    MODAL1 = (By.XPATH, "//button[contains(@class,'216')]")
    #Info legal 
    LEGAL_INFO = (By.XPATH, "(//button[contains(@class,'nq')])[2]")
    DOC_TYPE = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/div/div/form/div[1]/fieldset[2]/div[1]/label/div/i")
    TYPE_DOC = (By.XPATH, "(//span[contains(@class,'129')])[11]")
    DOC_NUMBER = (By.XPATH, "(//input[@type='text'])[1]")
    ISSUE_DATA = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/div/div/form/div[1]/fieldset[4]/label/div/div")
    DATA_DAY = (By.XPATH, "(//span[contains(@tabindex,'0')])[11]") 
    DATA_YEAR_DROP_DOWN = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/div/div/form/div[1]/fieldset[4]/div/div[1]/div[2]/span/i")
    YEAR_2024 = (By.XPATH, "//span[contains(.,'2024')]")
    DATA_YEAR_BACK = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/div/div/form/div[1]/fieldset[4]/div/div[1]/div[2]/button[1]")
    DATA_MONTH_DROP_DOWN = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/div/div/form/div[1]/fieldset[4]/div/div[1]/div[1]/span/i")
    MONTH_APRIL = (By.XPATH, "//span[contains(.,'April')]")
    DATA_MONTH_BACK = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/div/div/form/div[1]/fieldset[4]/div/div[1]/div[1]/button[1]")
    BUTTON_APPLY = (By.XPATH, "(//button[contains(@class,'42')])[1]")
    BUTTON_CANCEL = (By.XPATH, "(//button[contains(@class,'109')])[2]")
    BUTTON_RESTORE = (By.XPATH, "(//button[contains(@class,'109')])[1]")
    REGISTRATION_NUMBER_USER_LEGAL = (By.XPATH, "(//input[@type='text'])[3]")
    COMPANY_NAME_USER_LEGAL = (By.XPATH, "(//input[@type='text'])[4]")
    BILLING_COUNTRY = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/section/section/section/div/div/div/form/div[1]/fieldset[5]/div[1]/label/div/i[2]")
    STATE = (By.XPATH, "(//input[@type='text'])[5]")
    CITY = (By.XPATH, "(//input[@type='text'])[6]")
    ADDERSS = (By.XPATH, "(//input[@type='text'])[7]")
    POSTAL_CODE = (By.XPATH, "(//input[@type='text'])[8]")
    BUTTON_SAVE2 = (By.XPATH, "//button[contains(@class,'42')]")
    BUTTON_BACK2 = (By.XPATH, "//button[contains(@class,'76')]")
    MODAL2 = (By.XPATH, "//button[contains(@class,'153')]")
    #Cuwntas de pago
    PAYMENT_ACCOUNT = (By.XPATH, "(//button[contains(@class,'nq')])[3]")
    #Cuentas bancarias
    BANK_ACCOUNT = (By.XPATH, "(//div[@class='MuiBox-root mui-inlaze-rk3tja'])[1]")
    CUSTOM_NAME_BANK = (By.XPATH, "(//input[@name='customName'])[1]")
    BANK = (By.XPATH, "//input[@name='bankName']")
    ACCOUNT_TYPE = (By.XPATH, "//input[@name='accountType']")
    TYPE_ACCOUNT = (By.XPATH, "(//span[contains(@class,'129')])[9]")
    ACCOUNT_NUMBER = (By.XPATH, "//input[@name='accountNumber']")
    PAYMENT_METHOD = (By.XPATH, "(//input[@name='currency'])[1]")
    PAYMENT_EURO = (By.XPATH, "(//span[contains(@class,'129')])[17]")
    UPLOAD_FILE = (By.XPATH, "//p[contains(@class,'51')]")
    CHECK_CONFIRM1 = (By.XPATH, "(//input[@type='checkbox'])[1]")
    BUTTON_SAVE3 = (By.XPATH, "//button[contains(@class,'42')]")
    BUTTON_BACK3 = (By.XPATH, "//button[contains(@class,'76')]")
    MODAL_CONFIRT_CONTINUE = (By.XPATH, "(//button[contains(@class,'42')])[2]")
    MODAL_CONFIRM_EDIT = (By.XPATH, "(//button[contains(@class,'76')])[2]")
    #Cripto
    CRIPTO = (By.XPATH, "(//div[@class='MuiBox-root mui-inlaze-rk3tja'])[2]")
    CUSTOM_NAME_CRIPTO = (By.XPATH, "(//input[contains(@name,'customName')])[2]")
    CURRENCY_PAYMENT = (By.XPATH, "(//input[contains(@name,'currency')])[2]")
    PAYMENT_CURRENCY = (By.XPATH, "(//span[contains(@class,'129')])[27]")
    NETWORK = (By.XPATH, "//input[contains(@name,'network')]")
    NETWORK_ETHE = (By.XPATH, "(//span[contains(@class,'129')])[29]")
    WALLET = (By.XPATH, "//input[contains(@name,'walletId')]")
    CHECK_CONFIRM2 = (By.XPATH, "(//input[@type='checkbox'])[2]")
    BUTTON_SAVE4 = (By.XPATH, "//button[contains(@class,'42')]")
    BUTTON_BACK4 = (By.XPATH, "//button[contains(@class,'76')]")
    MODAL_CONFIRT_CONTINUE = (By.XPATH, "(//button[contains(@class,'42')])[2]")
    MODAL_CONFIRM_EDIT = (By.XPATH, "(//button[contains(@class,'76')])[2]")
    MODAL_CODE1 = (By.XPATH, "(//input[@type='text'])[1]")
    MODAL_CODE2 = (By.XPATH, "(//input[@type='text'])[2]")
    MODAL_CODE3 = (By.XPATH, "(//input[@type='text'])[3]")
    MODAL_CODE4 = (By.XPATH, "(//input[@type='text'])[4]")
    MODAL_CODE5 = (By.XPATH, "(//input[@type='text'])[5]")
    MODAL_CODE6 = (By.XPATH, "(//input[@type='text'])[6]")
    BUTTON_SEND = (By.XPATH, "/html/body/div[3]/div[3]/div[3]/button[2]")
    BUTTON_BACK5 = (By.XPATH, "(//button[contains(@class,'76')])[3]")
    BUTTON_SEND_CODE = (By.XPATH, "(//button[contains(@class,'76')])[2]")
    MODAL3 = (By.XPATH, "(//button[contains(@class,'42')])[2]")
    TASKS_COMPLETED = (By.XPATH, "//button[contains(@class,'228')]")


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
    #Ir a cuentas
    def select_account(self):
        self.wait_for_element(self.ACCOUNT).click()

    def select_docuemnts(self):
        self.wait_for_element(self.DOCUMENTS).click()

    def select_natural(self):
        self.wait_for_element(self.NATURAL).click()

    def select_legal(self):
        self.wait_for_element(self.LEGAL).click()

    def select_front_doc(self):
        self.wait_for_element(self.FRONT_DOC).click()#cargar dato

    def select_back_doc(self):
        self.wait_for_element(self.BACK_DOC).click()#cargar dato

    def select_selfie(self):
        self.wait_for_element(self.SELFIE).click()#cargar dato

    def select_button_save1(self):
        self.wait_for_element(self.BUTTON_SAVE1).click()

    def select_button_back1(self):
        self.wait_for_element(self.BUTTON_BACK1).click()

    def select_modal1(self):
        self.wait_for_element(self.MODAL1).click()
    
    #Info legal
    def select_info_legal(self):
        self.wait_for_element(self.LEGAL_INFO).click()

    def select_doc_type(self):
        self.wait_for_element(self.DOC_TYPE).click()

    def select_type_doc(self):
        self.wait_for_element(self.TYPE_DOC).click()

    def select_doc_number(self):
        self.wait_for_element(self.DOC_NUMBER).click()

    def text_doc_number(self, number):
        element = self.wait_for_element(self.DOC_NUMBER) 
        element.clear() 
        element.send_keys(number)

    def select_date(self):
        self.wait_for_element(self.ISSUE_DATA).click()

    def select_data_year_drow(self):
        self.wait_for_element(self.DATA_YEAR_DROP_DOWN).click()

    def select_year_2024(self):
        self.wait_for_element(self.YEAR_2024).click()

    def select_data_year(self):
        self.wait_for_element(self.DATA_YEAR_BACK).click()

    def select_data_month_drow(self):
        self.wait_for_element(self.DATA_MONTH_DROP_DOWN).click()

    def select_month_april(self):
        self.wait_for_element(self.MONTH_APRIL).click()

    def select_data_month(self):
        self.wait_for_element(self.DATA_MONTH_BACK).click()

    def select_data_day(self):
        self.wait_for_element(self.DATA_DAY).click()

    def select_button_apply(self):
        self.wait_for_element(self.BUTTON_APPLY).click()

    def select_button_cancel(self):
        self.wait_for_element(self.BUTTON_CANCEL).click()

    def select_button_restore(self):
        self.wait_for_element(self.BUTTON_RESTORE).click()

    def select_registration_number_user_legal(self):
        self.wait_for_element(self.REGISTRATION_NUMBER_USER_LEGAL).click()

