from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class managementpage(BasePage):
    #Ingreso normal
    select_email = (By.XPATH, "(//button[contains(@class,'NyLay')])[1]") 
    email = (By.XPATH, "//input[contains(@name,'email')]") 
    password = (By.XPATH, "//input[@type='password']") 
    button_c = (By.CLASS_NAME, "page_captcha__auNDN") 
    button_login = (By.XPATH, "//button[contains(@type,'submit')]") 
    #seleccionar la pestaña de campañas y admin 
    campaigns_and_market = (By.XPATH, "/html/body/div[1]/div[1]/section/ul[1]/li[2]/button") 
    management =(By.XPATH, "/html/body/div[1]/div[1]/section/ul[1]/li[2]/ul/button[2]") 
    #filtros de campañas 
    filter_dropdown = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div[1]/fieldset/label/div/i") 
    filter_highest_income = (By.XPATH, "(//span[contains(@class,'1')])[13]") 
    filter_lowest_income = (By.XPATH, "(//span[contains(@class,'1')])[14]") 
    filter_highest_deposit = (By.XPATH, "(//span[contains(@class,'1')])[15]") 
    filter_lowest_deposit = (By.XPATH, "(//span[contains(@class,'1')])[16]") 
    filter_cpa = (By.XPATH, "(//span[contains(.,'cpa')])[2]") 
    filter_rs = (By.XPATH, "(//span[contains(.,'rs')])[2]") 
    filter_textarea_manual = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/fieldset/label/div/div/input") 
    filter_textarea_select = (By.XPATH, "(//span[contains(.,'mexico')])[1]") 
    filter_placeholder_status = (By.XPATH, "(//span[@class='_label-large_1mvuk_113 _typography_1mvuk_1'])[6]")#no sale el estado 
    filter_placeholder_countries = (By.XPATH, "(//span[contains(@class,'1')])[38]") 
    filter_placeholder_operator = (By.XPATH, "(//span[contains(@class,'1')])[60]") 
    filter_textarea_x = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/fieldset/label/div/i[2]") 
    filter = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/button") 
    filter_chips_x = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/section/div[2]/div[2]/div[2]/label/span/i") 
    filter_chips_status = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/section/div[2]/div[3]/div[1]/div[1]/button") 
    filter_chips_active = (By.XPATH, "(//span[contains(@class,'34')])[3]") 
    filter_chips_closed = (By.XPATH, "(//span[contains(@class,'1')])[161]") 
    filter_chips_suspended = (By.XPATH, "(//span[contains(@class,'34')])[5]") 
    filter_chips_countries = (By.XPATH, "(//button[contains(@class,'76')])[3]") 
    filter_chips_argentina = (By.XPATH, "(//span[contains(.,'argentina')])[3]") 
    filter_chips_spain = (By.XPATH, "(//span[contains(@class,'34')])[20]") 
    filter_chips_more_countries = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/section/div[2]/div[3]/div[2]/button") 
    filter_chips_fewer_countries = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/section/div[2]/div[3]/div[2]/button") 
    filter_chips_operator = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/section/div[2]/div[3]/div[3]/div[1]/button") 
    filter_chips_888sport = (By.XPATH, "(//span[contains(.,'888sport')])[3]") 
    filter_chips_1win = (By.XPATH, "(//span[contains(@class,'34')])[82]") 
    filter_chips_more_operators = (By.XPATH, "(//button[contains(@class,'76')])[5]") 
    filter_chips_fewer_operators = (By.XPATH, "(//button[contains(@class,'76')])[5]") 
    filter_chips_apply = (By.XPATH, "//button[contains(@class,'42')]") 
    filter_clear = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/button[1]") #/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/button[1] 
    #seleccionar y crear link de campañas 
    see_details = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/button") 
    request_link1 = (By.XPATH, "/html/body/div[1]/div[2]/div[4]/article/div[3]/div/div/button[2]") 
    check_tyc_link = (By.XPATH, "//span[@class='_checkbox__icon_1txi3_33']") 
    button_create_link = (By.XPATH, "(//button[contains(@class,'m5pud')])[2]") 
    button_back = (By.XPATH, "(//button[contains(@class,'m5pud')])[1]") 
    copy_link = (By.XPATH, "//button[contains(@class,'k7fqh ')]") 
    button_finish = (By.XPATH, "//button[contains(.,'finish')]") 
    request_link2_desde_elmas = (By.XPATH, "/html/body/div[1]/div[2]/div[4]/article/div[2]/div[2]/div[3]") 
    button_close = (By.XPATH, "(//button[contains(@class,'m5pud')])[1]") 
    button_copy_link = (By.XPATH, "/html/body/div[1]/div[2]/div[4]/article/div[2]/div[2]/div[1]/div[2]/button") 
    button_final = (By.XPATH, "/html/body/div[1]/div[2]/div[3]/article/div[3]/div/div/button[1]") 

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

    #seleccionar campañas 
    def select_campaigns_and_market(self): 
        self.wait_for_element(self.campaigns_and_market).click() 

    def select_management(self): 
        self.wait_for_element(self.management).click() 

    #poner filtros  
    def select_filter_dropdown(self): 
        self.wait_for_element(self.filter_dropdown).click() 

    def select_filter_highest_income(self): 
        self.wait_for_element(self.filter_highest_income).click() 

    def select_filter_lowest_income(self): 
        self.wait_for_element(self.filter_lowest_income).click() 

    def select_filter_highest_deposit(self): 
        self.wait_for_element(self.filter_highest_deposit).click() 

    def select_filter_lowest_deposit(self): 
        self.wait_for_element(self.filter_lowest_deposit).click() 

    def select_filter_clear(self): 
        self.wait_for_element(self.filter_clear).click() 

    def select_filter_cpa(self): 
        self.wait_for_element(self.filter_cpa).click() 

    def select_filter_rs(self): 
        self.wait_for_element(self.filter_rs).click() 

    def select_filter_textarea_manual_click(self): 
        self.wait_for_element(self.filter_textarea_manual).click() 

    def select_filter_textarea_manual(self, pais): 
        element = self.wait_for_element(self.filter_textarea_manual)  
        element.clear()  
        element.send_keys(pais) 

    def select_filter_textarea_select(self): 
        self.wait_for_element(self.filter_textarea_select).click() 

    def select_filter_textarea_x(self): 
        self.wait_for_element(self.filter_textarea_x).click() 

    def select_filter_textarea_manual_click(self): 
        self.wait_for_element(self.filter_textarea_manual).click() 

    def select_filter_placeholder_status(self): 
        self.wait_for_element(self.filter_placeholder_status).click() 

    def select_filter_placeholder_countries(self): 
        self.wait_for_element(self.filter_placeholder_countries).click() 

    def select_filter_placeholder_operator(self): 
        self.wait_for_element(self.filter_placeholder_operator).click() 

    def select_filter_chips(self): 
        self.wait_for_element(self.filter).click() 

    def select_filter_chips_x(self): 
        self.wait_for_element(self.filter_chips_x).click() 

    def select_filter_chips_active(self): 
        self.wait_for_element(self.filter_chips_active).click() 

    def select_filter_chips_closed(self): 
        self.wait_for_element(self.filter_chips_closed).click() 

    def select_filter_chips_suspended(self): 
        self.wait_for_element(self.filter_chips_suspended).click() 

    def select_filter_chips_status(self): 
        self.wait_for_element(self.filter_chips_status).click() 

    def select_filter_chips_argentina(self): 
        self.wait_for_element(self.filter_chips_argentina).click() 

    def select_filter_chips_more_countries(self): 
        self.wait_for_element(self.filter_chips_more_countries).click() 

    def select_filter_chips_spain(self): 
        self.wait_for_element(self.filter_chips_spain).click() 

    def select_filter_chips_fewer_countries(self): 
        self.wait_for_element(self.filter_chips_fewer_countries).click() 

    def select_filter_chips_countries(self): 
        self.wait_for_element(self.filter_chips_countries).click() 

    def select_filter_chips_888sport(self): 
        self.wait_for_element(self.filter_chips_888sport).click() 

    def select_filter_chips_more_operators(self): 
        self.wait_for_element(self.filter_chips_more_operators).click() 

    def select_filter_chips_1win(self): 
        self.wait_for_element(self.filter_chips_1win).click() 

    def select_filter_chips_fewer_operators(self): 
        self.wait_for_element(self.filter_chips_fewer_operators).click() 


    def select_filter_chips_operator(self): 
        self.wait_for_element(self.filter_chips_operator).click() 

    def select_filter_chips_apply(self): 
        self.wait_for_element(self.filter_chips_apply).click() 

    #adquirir link de campañas  
    def select_see_details(self): 
        self.wait_for_element(self.see_details).click() 

    def select_promote_campaigns_link1(self): 
        self.wait_for_element(self.request_link1).click() 

    def select_check_tyc_link(self): 
        self.wait_for_element(self.check_tyc_link).click() 

    def select_button_create_link(self): 
        self.wait_for_element(self.button_create_link).click() 

    def select_copy_link(self): 
        self.wait_for_element(self.copy_link).click() 

    def select_button_finish(self): 
        self.wait_for_element(self.button_finish).click() 

    def select_request_link2_desde_elmas(self): 
        self.wait_for_element(self.request_link2_desde_elmas).click() 

    def select_button_close(self): 
        self.wait_for_element(self.button_close).click() 

    def select_button_copy_link(self): 
        self.wait_for_element(self.button_copy_link).click() 

    def select_button_final(self): 
        self.wait_for_element(self.button_final).click() 
