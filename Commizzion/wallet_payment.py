from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class paymentpage(BasePage):
    #Ingreso normal
    select_email = (By.XPATH, "(//button[contains(@class,'NyLay')])[1]") 
    email = (By.XPATH, "//input[contains(@name,'email')]") 
    password = (By.XPATH, "//input[@type='password']") 
    button_c = (By.CLASS_NAME, "page_captcha__auNDN") 
    button_login = (By.XPATH, "//button[contains(@type,'submit')]") 
    #Salidad de la cuenta
    CLOSE_BOTTON = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div/button[3]")
    MODAL_CLOSE_SESION = (By.XPATH, "(//button[contains(@class,'39')])[2]")
    #Boton de wallet
    button_wallet = (By.XPATH, "//span[contains(.,'Wallet')]")
    payment_history = (By. XPATH, "/html/body/div[1]/div[1]/section/ul[1]/li[5]/ul/button[2]")
    drop_down = (By. XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div/h3/button/span/div/div[2]/i/svg/path")
    receipt = (By. XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div/div[4]/button")
    expand_history_button = (By. XPATH, "(//button[contains(@class,'76')])[2]")
    request_help_button = (By. XPATH, "(//button[contains(@class,'76')])[3]")
    no_history_modal = (By. XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/button")

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

    #Salida de la cuenta
    def select_button_close(self):
        self.wait_for_element(self.CLOSE_BOTTON).click()

    def select_button_modal(self):
        self.wait_for_element(self.MODAL_CLOSE_SESION).click()

    
    #ir a historial de pagos 
    def select_button_wallet(self):
        self.wait_for_element(self.button_wallet).click()

    def select_payment_history(self):
        self.wait_for_element(self.payment_history).click()

    def select_drop_down(self):
        self.wait_for_element(self.drop_down).click()

    def select_receipt(self):
        self.wait_for_element(self.receipt).click()

    def select_expand_history_button(self):
        self.wait_for_element(self.expand_history_button).click()

    def select_request_help_button(self):
        self.wait_for_element(self.request_help_button).click()

    #Sin historial
    def select_no_history_modal(self):
        self.wait_for_element(self.no_history_modal).click()