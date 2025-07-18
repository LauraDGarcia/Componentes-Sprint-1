from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class panelpage(BasePage):
    SELECT_EMAIL = (By.XPATH, "//button[contains(.,'Correo electrónico')]")
    EMAIL = (By.XPATH, "//input[contains(@name,'email')]")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    BUTTON_C = (By.CLASS_NAME, "page_captcha__auNDN")
    BUTTON_LOGIN = (By.XPATH, "//button[contains(@type,'submit')]")
    VISUAL_EYE = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div[1]/div/i")
    ICON_BALANCE = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/i")
    FIELD_PERIOD = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[1]/fieldset/label/div/i")
    PERIOD_TODAY = (By.XPATH, "(//span[contains(@class,'1')])[13]") #Sleccion de fechas ya establecidas SE CAMBIO EL NOMBRE
    PERIOD_30DAYS = (By.XPATH, "(//span[contains(@class,'1')])[16]") #Sleccion de fechas ya establecidas SE CAMBIO EL NOMBRE
    CUSTOM_DATE = (By.XPATH, "(//span[contains(@class,'129')])[15]") #Sleccion de fecha personalizada
    PREVIUS_MONTH = (By.XPATH, "//*[@id='calendar-mobile-overlay']/div/div[1]/div[1]/button[1]") #Atras con los meses 
    NEXT_MONTH = (By.XPATH, "//*[@id='calendar-mobile-overlay']/div/div[1]/div[1]/button[2]") #Adelante con los meses 
    PREVIUS_YEAR = (By.XPATH, "//*[@id='calendar-mobile-overlay']/div/div[1]/div[2]/button[1]") #Atras con los años
    NEXT_YEAR = (By.XPATH, "//*[@id='calendar-mobile-overlay']/div/div[1]/div[2]/button[2]") #Adelante con los años
    YEAR_PERIOD = (By.XPATH, "//*[@id='calendar-mobile-overlay']/div/div[1]/div[2]/span") #Seleccion del año y año final 
    NEW_YEAR_PERIOD = (By.XPATH, "//*[@id='calendar-mobile-overlay']/div/div[2]/div[98]") #Seleccion del año donde se seleccionara una fecha inicial
    FINAL_YEAR_PERIOD = (By.XPATH, "//*[@id='calendar-mobile-overlay']/div/div[2]/div[104]") #Año final
    MONTH_PERIOD = (By.XPATH, "//*[@id='calendar-mobile-overlay']/div/div[1]/div[1]/span") #Seleccion del mes
    MONTH_PERIOD_STARTING = (By.XPATH, "//*[@id='calendar-mobile-overlay']/div/div[2]/div[2]") #Slecccion del mes inicial
    MONTH_PERIOD_FINAL = (By.XPATH, "//*[@id='calendar-mobile-overlay']/div/div[2]/div[1]") #Seleccion del mes final
    DAY_PERIOD_STARTING = (By.XPATH, "(//span[contains(@class,'21')])[9]") #Dia inicial en enero
    DAY_PERIOD_FINAL = (By.XPATH, "(//span[contains(@class,'21')])[34]") #Dia final en febrero
    BUTTON_OK_PERIOD = (By.XPATH, "(//button[@type='button'])[7]") #Boton de okay para seleccionar la fecha
    BUTTON_CANCEL_PERIOD = (By.XPATH, "(//button[@type='button'])[6]")#Bopton de cancelar
    BUTTON_RESTORE_PERIOD = (By.XPATH, "(//button[contains(@class,'109')])[1]") #Boton de restaurar 
    CARD_METRICS_EARNINGS = (By.XPATH, "(//div[contains(@class,'5vZ9P')])[1]") #tarjetas de metricas 
    CARD_METRICS_AFFILIATE = (By.XPATH, "(//div[contains(@class,'5vZ9P')])[2]")
    CARD_METRICS_REGISTRATIONS = (By.XPATH, "(//div[contains(@class,'5vZ9P')])[3]")
    CARD_METRICS_FTD = (By.XPATH, "(//div[contains(@class,'5vZ9P')])[4]")
    CARD_METRICS_CPA = (By.XPATH, "(//div[contains(@class,'5vZ9P')])[5]")
    TOOLTIPS_EARNINGS = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[3]/button[1]/div/p[1]/i")
    TOOLTIPS_AFFILIATE = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/span/div/div/div/span[3]/span/i[2]")
    TOOLTIPS_REGISTRATIONS = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[3]/button[2]/div/p[1]/i")
    TOOLTIPS_FTD = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[3]/button[3]/div/p[1]/i")
    TOOLTIPS_CPA = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[3]/button[4]/div/p[1]/i")
    TOOLTIP_ACTUALIZATION = (By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[2]/div/i") ####"$##"
    CLEAR = (By.XPATH, "(//button[contains(@class,'76')])[1]")

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

    #Busqueda en el panel
    def visual_wallet_eye(self):
        self.wait_for_element(self.VISUAL_EYE).click()

    def icon_balance_wallet(self):
        self.wait_for_element(self.ICON_BALANCE).click()

    def main_period(self):
        self.wait_for_element(self.FIELD_PERIOD).click()

     #Seleccion de fechas predeterminadas
    def select_period_today(self):
        self.wait_for_element(self.PERIOD_TODAY).click()

    def select_period_30days(self):
        self.wait_for_element(self.PERIOD_30DAYS).click()


    #Seleccion de fecha por botones
    def select_period_custom(self):
        self.wait_for_element(self.CUSTOM_DATE).click()

    def select_period_yesterday(self):
        self.wait_for_element(self.PERIOD_TODAY).click()

    def select_previous_month(self):
        self.wait_for_element(self.PREVIUS_MONTH).click()

    def select_next_month(self):
        self.wait_for_element(self.NEXT_MONTH).click()

    def select_previous_year(self):
        self.wait_for_element(self.PREVIUS_YEAR).click()

    def select_next_year(self):
        self.wait_for_element(self.NEXT_YEAR).click()

    #Seleccionar de fecha manual 

    def select_year_period(self):
        self.wait_for_element(self.YEAR_PERIOD).click()

    def select_new_year_period(self):
        self.wait_for_element(self.NEW_YEAR_PERIOD).click()

    def select_month_period(self):
        self.wait_for_element(self.MONTH_PERIOD).click()

    def select_month_period_starting(self):
        self.wait_for_element(self.MONTH_PERIOD_STARTING).click()

    def select_day_period_starting(self):
        self.wait_for_element(self.DAY_PERIOD_STARTING).click()  

    def select_year_period(self):
        self.wait_for_element(self.YEAR_PERIOD).click()

    def select_final_year_period(self):
        self.wait_for_element(self.FINAL_YEAR_PERIOD).click() 

    def select_selector_month(self):
        self.wait_for_element(self.MONTH_PERIOD).click()

    def select_month_period_final(self):
        self.wait_for_element(self.MONTH_PERIOD_FINAL).click()

    def select_day_period_final(self):
        self.wait_for_element(self.DAY_PERIOD_FINAL).click()

    def select_button_ok_period(self):
        self.wait_for_element(self.BUTTON_OK_PERIOD).click()

    #Targetas de metricas 
    def select_card_metrics_earnings(self):
        self.wait_for_element(self.CARD_METRICS_EARNINGS).click()

    def select_card_metrics_affiliate(self):
        self.wait_for_element(self.CARD_METRICS_AFFILIATE).click()

    def select_card_metrics_registrations(self):
        self.wait_for_element(self.CARD_METRICS_REGISTRATIONS).click()

    def select_card_metrics_FTD(self):
        self.wait_for_element(self.CARD_METRICS_FTD).click()

    def select_card_metrics_CPA(self):
        self.wait_for_element(self.CARD_METRICS_CPA).click()

    def select_tooltips_earnings(self):
        self.wait_for_element(self.TOOLTIPS_EARNINGS).click()

    def select_tooltips_affiliate(self):
        self.wait_for_element(self.TOOLTIPS_AFFILIATE).click()

    def select_tooltips_registrations(self):
        self.wait_for_element(self.TOOLTIPS_REGISTRATIONS).click()

    def select_tooltips_FTD(self):
        self.wait_for_element(self.TOOLTIPS_FTD).click()

    def select_tooltips_CPA(self):
        self.wait_for_element(self.TOOLTIPS_CPA).click()

    def select_tooltips_actualization(self):
        self.wait_for_element(self.TOOLTIP_ACTUALIZATION).click()

    #Error de diagrama
    def select_button_clear(self):
        self.wait_for_element(self.CLEAR).click()

    

    