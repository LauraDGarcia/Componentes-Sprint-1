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
    #seleccionar la pestaña de campañas y admin
    CAMPAIGNS_AND_MARKET = (By.XPATH, "/html/body/div[1]/div[1]/section/ul[1]/li[2]/button")
    CAMPAIGNS = (By.XPATH, "/html/body/div[1]/div[1]/section/ul[1]/li[2]/ul/button[1]")
    #Filtros de campañas
    FILTER_DROPDOWN = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div[1]/fieldset/label/div/i")
    FILTER_HIGHEST_INCOME = (By.XPATH, "(//span[contains(@class,'1')])[12]")
    FILTER_LOWEST_INCOME = (By.XPATH, "(//span[contains(@class,'1')])[13]")
    FILTER_HIGHEST_DEPOSIT = (By.XPATH, "(//span[contains(@class,'1')])[14]")
    FILTER_LOWEST_DEPOSIT = (By.XPATH, "(//span[contains(@class,'1')])[15]")
    FILTER_CPA = (By.XPATH, "//span[@class='_label-medium_1mvuk_129 _typography_1mvuk_1'][contains(.,'CPA')]")
    FILTER_RS = (By.XPATH, "(//span[contains(.,'RS')])[2]")
    FILTER_TEXTAREA_MANUAL = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/fieldset/label/div/div/input")
    FILTER_TEXTAREA_SELECT = (By.XPATH, "(//span[contains(.,'México')])[1]")
    FILTER_PLACEHOLDER_STATUS = (By.XPATH, "(//span[contains(@class,'_label-large_1mvuk_113 _typography_1mvuk_1')])[15]")
    FILTER_PLACEHOLDER_COUNTRIES = (By.XPATH, "(//span[contains(@class,'1')])[38]")
    FILTER_PLACEHOLDER_OPERATOR = (By.XPATH, "(//span[contains(@class,'1')])[60]")
    FILTER_TEXTAREA_X = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/fieldset/label/div/i[2]")
    FILTER = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/button")
    FILTER_CHIPS_X = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/section/div[2]/div[2]/div[2]/label/span/i")
    FILTER_CHIPS_STATUS = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/section/div[2]/div[3]/div[1]/div[1]/button")
    FILTER_CHIPS_ACTIVE = (By.XPATH, "(//span[contains(@class,'34')])[3]")
    FILTER_CHIPS_CLOSED = (By.XPATH, "(//span[contains(@class,'1')])[161]")
    FILTER_CHIPS_SUSPENDED = (By.XPATH, "(//span[contains(@class,'34')])[5]")
    FILTER_CHIPS_COUNTRIES = (By.XPATH, "(//button[contains(@class,'76')])[3]")
    FILTER_CHIPS_ARGENTINA = (By.XPATH, "(//span[contains(@class,'1')])[163]")
    FILTER_CHIPS_SPAIN = (By.XPATH, "(//span[contains(@class,'34')])[20]")
    FILTER_CHIPS_MORE_COUNTRIES = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/section/div[2]/div[3]/div[2]/button")
    FILTER_CHIPS_FEWER_COUNTRIES = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/section/div[2]/div[3]/div[2]/button")
    FILTER_CHIPS_OPERATOR = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/section/div[2]/div[3]/div[3]/div[1]/button")
    FILTER_CHIPS_888SPORT = (By.XPATH, "(//span[contains(@class,'1')])[237]")
    FILTER_CHIPS_1WIN = (By.XPATH, "(//span[contains(@class,'34')])[82]")
    FILTER_CHIPS_MORE_OPERATORS = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/section/div[2]/div[3]/div[3]/button")
    FILTER_CHIPS_FEWER_OPERATORS = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/section/div[2]/div[3]/div[3]/button")
    FILTER_CHIPS_APPLY = (By.XPATH, "//button[contains(@class,'42')]")
    FILTER_CLEAR = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/button[1]")
    #Seleccionar y crear link de campañas
    SEE_DETAILS = (By.XPATH, "(//button[contains(@class,'8tKuM')])[1]")
    PROMOTE_CAMPAIGNS_LINK1 = (By.XPATH, "(//button[@type='button'])[2]")
    CHECK_TYC_LINK = (By.XPATH, "//span[@class='_checkbox__icon_1txi3_33']")
    BUTTON_CREATE_LINK = (By.XPATH, "(//button[contains(@class,'oy16')])[2]")
    BUTTON_BACK = (By.XPATH, "(//button[contains(@class,'oy16')])[1]")
    COPY_LINK = (By.XPATH, "//button[contains(@class,'9NXqg ')]")
    BUTTON_FINISH = (By.XPATH, "//button[contains(@class,'v0upz')]")
    REQUEST_LINK2_DESDE_ELMAS = (By.XPATH, "/html/body/div[1]/div[2]/div[3]/article/div[2]/div[2]/div[2]")
    BUTTON_CLOSE = (By.XPATH, "(//button[contains(@class,'oy16')])[1]")
    BUTTON_COPY_LINK = (By.XPATH, "/html/body/div[1]/div[2]/div[3]/article/div[2]/div[2]/div[1]/button")
    BUTTON_FINAL = (By.XPATH, "/html/body/div[1]/div[2]/div[3]/article/div[3]/div/div/button[1]")

    def navigate_home(self):
        self.go_to_page("https://qa-account-commizzion-vm.inlazetest.com/login")

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

    #Seleccionar campañas

    def select_CAMPAIGNS_AND_MARKET(self):
        self.wait_for_element(self.CAMPAIGNS_AND_MARKET).click()

    def select_CAMPAIGNS(self):
        self.wait_for_element(self.CAMPAIGNS).click()

    #Poner filtros 

    def select_FILTER_DROPDOWN(self):
        self.wait_for_element(self.FILTER_DROPDOWN).click()

    def select_FILTER_HIGHEST_INCOME(self):
        self.wait_for_element(self.FILTER_HIGHEST_INCOME).click()

    def select_FILTER_LOWEST_INCOME(self):
        self.wait_for_element(self.FILTER_LOWEST_INCOME).click()

    def select_FILTER_HIGHEST_DEPOSIT(self):
        self.wait_for_element(self.FILTER_HIGHEST_DEPOSIT).click()

    def select_FILTER_LOWEST_DEPOSIT(self):
        self.wait_for_element(self.FILTER_LOWEST_DEPOSIT).click()

    def select_FILTER_CLEAR(self):
        self.wait_for_element(self.FILTER_CLEAR).click()

    def select_FILTER_CPA(self):
        self.wait_for_element(self.FILTER_CPA).click()

    def select_FILTER_RS(self):
        self.wait_for_element(self.FILTER_RS).click()

    def select_FILTER_TEXTAREA_MANUAL_click(self):
        self.wait_for_element(self.FILTER_TEXTAREA_MANUAL).click()

    def select_FILTER_TEXTAREA_MANUAL(self, pais):
        element = self.wait_for_element(self.FILTER_TEXTAREA_MANUAL) 
        element.clear() 
        element.send_keys(pais)

    def select_FILTER_TEXTAREA_SELECT(self):
        self.wait_for_element(self.FILTER_TEXTAREA_SELECT).click()

    def select_FILTER_TEXTAREA_X(self):
        self.wait_for_element(self.FILTER_TEXTAREA_X).click()
    
    def select_FILTER_TEXTAREA_MANUAL_click(self):
        self.wait_for_element(self.FILTER_TEXTAREA_MANUAL).click()

    def select_FILTER_PLACEHOLDER_STATUS(self):
        self.wait_for_element(self.FILTER_PLACEHOLDER_STATUS).click()

    def select_FILTER_PLACEHOLDER_COUNTRIES(self):
        self.wait_for_element(self.FILTER_PLACEHOLDER_COUNTRIES).click()

    def select_FILTER_PLACEHOLDER_OPERATOR(self):
        self.wait_for_element(self.FILTER_PLACEHOLDER_OPERATOR).click()

    def select_FILTER_CHIPS(self):
        self.wait_for_element(self.FILTER).click()

    def select_FILTER_CHIPS_X(self):
        self.wait_for_element(self.FILTER_CHIPS_X).click()

    def select_FILTER_CHIPS_ACTIVE(self):
        self.wait_for_element(self.FILTER_CHIPS_ACTIVE).click()

    def select_FILTER_CHIPS_CLOSED(self):
        self.wait_for_element(self.FILTER_CHIPS_CLOSED).click()

    def select_FILTER_CHIPS_SUSPENDED(self):
        self.wait_for_element(self.FILTER_CHIPS_SUSPENDED).click()

    def select_FILTER_CHIPS_STATUS(self):
        self.wait_for_element(self.FILTER_CHIPS_STATUS).click()

    def select_FILTER_CHIPS_ARGENTINA(self):
        self.wait_for_element(self.FILTER_CHIPS_ARGENTINA).click()

    def select_FILTER_CHIPS_MORE_COUNTRIES(self):
        self.wait_for_element(self.FILTER_CHIPS_MORE_COUNTRIES).click()

    def select_FILTER_CHIPS_SPAIN(self):
        self.wait_for_element(self.FILTER_CHIPS_SPAIN).click()

    def select_FILTER_CHIPS_FEWER_COUNTRIES(self):
        self.wait_for_element(self.FILTER_CHIPS_FEWER_COUNTRIES).click()

    def select_FILTER_CHIPS_COUNTRIES(self):
        self.wait_for_element(self.FILTER_CHIPS_COUNTRIES).click()

    def select_FILTER_CHIPS_888SPORT(self):
        self.wait_for_element(self.FILTER_CHIPS_888SPORT).click()

    def select_FILTER_CHIPS_MORE_OPERATORS(self):
        self.wait_for_element(self.FILTER_CHIPS_MORE_OPERATORS).click()

    def select_FILTER_CHIPS_1WIN(self):
        self.wait_for_element(self.FILTER_CHIPS_1WIN).click()

    def select_FILTER_CHIPS_FEWER_OPERATORS(self):
        self.wait_for_element(self.FILTER_CHIPS_FEWER_OPERATORS).click()

    def select_FILTER_CHIPS_OPERATOR(self):
        self.wait_for_element(self.FILTER_CHIPS_OPERATOR).click()

    def select_FILTER_CHIPS_APPLY(self):
        self.wait_for_element(self.FILTER_CHIPS_APPLY).click()

    #Adquirir link de campañas 
    def select_SEE_DETAILS(self):
        self.wait_for_element(self.SEE_DETAILS).click()

    def select_PROMOTE_CAMPAIGNS_LINK1(self):
        self.wait_for_element(self.PROMOTE_CAMPAIGNS_LINK1).click()

    def select_CHECK_TYC_LINK(self):
        self.wait_for_element(self.CHECK_TYC_LINK).click()

    def select_BUTTON_CREATE_LINK(self):
        self.wait_for_element(self.BUTTON_CREATE_LINK).click()

    def select_COPY_LINK(self):
        self.wait_for_element(self.COPY_LINK).click()

    def select_BUTTON_FINISH(self):
        self.wait_for_element(self.BUTTON_FINISH).click()

    def select_REQUEST_LINK2_DESDE_ELMAS(self):
        self.wait_for_element(self.REQUEST_LINK2_DESDE_ELMAS).click()

    def select_BUTTON_CLOSE(self):
        self.wait_for_element(self.BUTTON_CLOSE).click()

    def select_BUTTON_COPY_LINK(self):
        self.wait_for_element(self.BUTTON_COPY_LINK).click()

    def select_BUTTON_FINAL(self):
        self.wait_for_element(self.BUTTON_FINAL).click()