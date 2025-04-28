from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class balancepage(BasePage):
    #Ingreso normal
    select_email = (By.XPATH, "(//button[contains(@class,'NyLay')])[1]") 
    email = (By.XPATH, "//input[contains(@name,'email')]") 
    password = (By.XPATH, "//input[@type='password']") 
    button_c = (By.CLASS_NAME, "page_captcha__auNDN") 
    button_login = (By.XPATH, "//button[contains(@type,'submit')]") 
    #Salida de la cuenta
    CLOSE_BOTTON = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div/button[3]")
    MODAL_CLOSE_SESION = (By.XPATH, "(//button[contains(@class,'39')])[2]")
    #Boton de wallet
    button_wallet = (By.XPATH, "//span[contains(.,'Wallet')]")
    button_balance = (By.XPATH, "/html/body/div[1]/div[1]/section/ul[1]/li[5]/ul/button[1]")
    #Cuenta con saldo
    button_eye_balance = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[3]/div[1]/div[1]/div[1]/button")
    icon_total_balance = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[1]/div[1]/div/i")
    icon_incoming_balance = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[1]/div/i")
    icon_value_receive = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[3]/div[1]/div/i")
    icon_lapz_button = (By. XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[3]/div[3]/div/div[2]/button")
    button_co_to_historu = (By. XPATH, "(//button[contains(@class,'76')])[1]")
    #Cuenta sin saldo
    modal_add_account_button_yes = (By. XPATH, "//button[contains(@class,'BdnJe')]")
    modal_add_account_button_not = (By. XPATH, "//button[contains(@class,'ipDe5')]")
    modal_add_account_button_X = (By. XPATH, "/html/body/div[7]/div[3]/div/div[1]/div/button/i")
    Button_add_account = (By. XPATH, "//button[contains(@class,'QJRal')]")

    def navigate_home(self): 
        self.go_to_page("https://qa-account-commizzion-vm.inlazetest.com/login") 

     #inicio de sesión  

    def wait_for_element(self, locator): 
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))   

    def select_button_email(self): 
        self.wait_for_element(self.select_email).click() 

    def select_text_email(self): 
        self.wait_for_element(self.email).click() 

    def text_email(self, email): 
        element = self.wait_for_element(self.email)  # corregido 
        element.clear()  
        element.send_keys(email) 

    def select_text_password(self): 
        self.wait_for_element(self.password).click() 

    def text_password(self, password): 
        element = self.wait_for_element(self.password) 
        element.send_keys(password) 

    def select_checkbox(self): 
        checkbox_element = self.wait_for_element(self.button_c) 
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.button_c))  # esperar que sea clickeable 
        checkbox_element.click()  

    def select_button_login(self): 
        self.wait_for_element(self.button_login).click()

    #Dirigirse a wallet y despues a saldo
    def select_button_wallet(self):
        self.wait_for_element(self.button_wallet).click()

    def select_button_balance(self):
        self.wait_for_element(self.button_balance).click()

    def select_button_eye_balance(self):
        self.wait_for_element(self.button_eye_balance).click()

    def select_icon_total_balance(self):
        self.wait_for_element(self.icon_total_balance).click()

    def select_icon_incoming_balance(self):
        self.wait_for_element(self.icon_incoming_balance).click()

    def select_icon_value_receive(self):
        self.wait_for_element(self.icon_value_receive).click()

    def select_icon_lapz_button(self):
        self.wait_for_element(self.icon_lapz_button).click()

    def select_button_co_to_historu(self):
        self.wait_for_element(self.button_co_to_historu).click()

    #Cuenta sin saldo
    def select_modal_add_account_button_yes(self):
        self.wait_for_element(self.modal_add_account_button_yes).click()

    def select_modal_add_account_button_not(self):
        self.wait_for_element(self.modal_add_account_button_not).click()

    def select_modal_add_account_button_X(self):
        self.wait_for_element(self.modal_add_account_button_X).click()

    def select_Button_add_account(self):
        self.wait_for_element(self.Button_add_account).click()

    #Salida de la cuenta 
    def select_button_close(self):
        self.wait_for_element(self.CLOSE_BOTTON).click()

    def select_button_modal(self):
        self.wait_for_element(self.MODAL_CLOSE_SESION).click()