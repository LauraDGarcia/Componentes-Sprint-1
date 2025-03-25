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
    VISUAL_EYE = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/span/div/div/span/button")
    ICON_BALANCE = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/span/div/div/div/span[1]/span/i[2]")
    ICON_EARNED = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/span/div/div/div/span[2]/span/i[2]") 
    ICON_PAID = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/span/div/div/div/span[3]/span/i[2]")
    FIELD_PERIOD = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[1]/span/fieldset/label/div/i")
    PERIOD_YESTERDAY = (By.XPATH, "(//span[contains(@class,'1')])[13]") #Sleccion de fechas ya establecidas
    PERIOD_LAST_MONTH = (By.XPATH, "(//span[contains(@class,'1')])[16]") #Sleccion de fechas ya establecidas
    CUSTOM_DATE = (By.XPATH, "(//span[contains(@class,'1')])[17]") #Sleccion de fecha personalizada
    PREVIUS_MONTH = (By.XPATH, "//*[@id='calendar-mobile-overlay']/div/div[1]/div[1]/button[1]") #Atras con los meses 
    NEXT_MONTH = (By.XPATH, "//*[@id='calendar-mobile-overlay']/div/div[1]/div[1]/button[2]") #Adelante con los meses 
    PREVIUS_YEAR = (By.XPATH, "//*[@id='calendar-mobile-overlay']/div/div[1]/div[2]/button[1]") #Atras con los años
    NEXT_YEAR = (By.XPATH, "//*[@id='calendar-mobile-overlay']/div/div[1]/div[2]/button[2]") #Adelante con los años
    YEAR_PERIOD = (By.XPATH, "//*[@id='calendar-mobile-overlay']/div/div[1]/div[2]/span") #Seleccion del año y año final 
    FOLDOUT_YEAR = (By.XPATH, "//*[@id='calendar-mobile-overlay']/div/div[1]/div[2]/i") #Desplegable del año
    NEW_YEAR_PERIOD = (By.XPATH, "//*[@id='calendar-mobile-overlay']/div/div[2]/div[98]") #Seleccion del año donde se seleccionara una fecha inicial
    FINAL_YEAR_PERIOD = (By.XPATH, "//*[@id='calendar-mobile-overlay']/div/div[2]/div[104]") #Año final
    MONTH_PERIOD = (By.XPATH, "//*[@id='calendar-mobile-overlay']/div/div[1]/div[1]/span") #Seleccion del mes
    FOLDOUT_MONTH = (By.XPATH, "//*[@id='calendar-mobile-overlay']/div/div[1]/div[1]/i") #Desplegable del mes
    MONTH_PERIOD_STARTING = (By.XPATH, "//*[@id='calendar-mobile-overlay']/div/div[2]/div[2]") #Slecccion del mes inicial
    MONTH_PERIOD_FINAL = (By.XPATH, "//*[@id='calendar-mobile-overlay']/div/div[2]/div[1]") #Seleccion del mes final
    DAY_PERIOD_STARTING = (By.XPATH, "(//div[contains(@class,'27')])[3]") #Dia inicial en enero
    DAY_PERIOD_FINAL = (By.XPATH, "(//div[contains(@class,'27')])[16]") #Dia final en febrero
    BUTTON_OK_PERIOD = (By.XPATH, "(//span[contains(.,'OK')])[2]") #Boton de okay para seleccionar la fecha
    BUTTON_CANCEL_PERIOD = (By.XPATH, "(//span[contains(@class,'10')])[3]")#Bopton de cancelar
    BUTTON_RESTORE_PERIOD = (By.XPATH, "(//span[contains(@class,'10')])[2]") #Boton de restaurar 
    CARD_METRICS_EARNINGS = (By.XPATH, "(//div[contains(@class,'5vZ9P')])[1]") #tarjetas de metricas 
    CARD_METRICS_AFFILIATE = (By.XPATH, "(//div[contains(@class,'5vZ9P')])[2]")
    CARD_METRICS_REGISTRATIONS = (By.XPATH, "(//div[contains(@class,'5vZ9P')])[3]")
    CARD_METRICS_FTD = (By.XPATH, "(//div[contains(@class,'5vZ9P')])[4]")
    CARD_METRICS_CPA = (By.XPATH, "(//div[contains(@class,'5vZ9P')])[5]")
    TOOLTIPS_EARNINGS = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/button[1]/div/p[1]/i")
    TOOLTIPS_AFFILIATE = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/button[2]/div/p[1]/i")
    TOOLTIPS_REGISTRATIONS = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/button[3]/div/p[1]/i")
    TOOLTIPS_FTD = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/button[4]/div/p[1]/i")
    TOOLTIPS_CPA = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/button[5]/div/p[1]/i")
    TOOLTIP_ACTUALIZATION = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[1]/span/span/i/svg") ####"$##"
    REFRESH_DATA = (By.XPATH, "//span[contains(.,'Refresh data')]")
    PREVIOUS_COMPARISON_EARNINGS = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/button[1]/div/span/i")
    PREVIOUS_COMPARISON_AFFILIATE = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/button[2]/div/span/i")
    PREVIOUS_COMPARISON_REGISTRATIONS = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/button[3]/div/span/i")
    PREVIOUS_COMPARISON_FTD = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/button[4]/div/span/i")
    PREVIOUS_COMPARISON_CPA = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/button[5]/div/span/i")

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

    def icon_earned_wallet(self):
        self.wait_for_element(self.ICON_EARNED).click()

    def icon_paid_wallet(self):
        self.wait_for_element(self.ICON_PAID).click()

    def main_period(self):
        self.wait_for_element(self.FIELD_PERIOD).click()

     #Seleccion de fechas predeterminadas
    def select_period_yesterday(self):
        self.wait_for_element(self.PERIOD_YESTERDAY).click()

    def select_period_last_month(self):
        self.wait_for_element(self.PERIOD_LAST_MONTH).click()


    #Seleccion de fecha por botones
    def select_period_custom(self):
        self.wait_for_element(self.CUSTOM_DATE).click()

    def select_period_yesterday(self):
        self.wait_for_element(self.PERIOD_YESTERDAY).click()

    def select_previous_month(self):
        self.wait_for_element(self.PREVIUS_MONTH).click()

    def select_next_month(self):
        self.wait_for_element(self.NEXT_MONTH).click()

    def select_previous_year(self):
        self.wait_for_element(self.PREVIUS_YEAR).click()

    def select_next_year(self):
        self.wait_for_element(self.NEXT_YEAR).click()

    #Seleccionar de fecha manual 

    def select_YEAR_PERIOD(self):
        self.wait_for_element(self.YEAR_PERIOD).click()

    def select_FOLDOUT_YEAR(self):
        self.wait_for_element(self.FOLDOUT_YEAR).click()

    def select_NEW_YEAR_PERIOD(self):
        self.wait_for_element(self.NEW_YEAR_PERIOD).click()

    def select_MONTH_PERIOD(self):
        self.wait_for_element(self.MONTH_PERIOD).click()

    def select_FOLDOUT_MONTH(self):
        self.wait_for_element(self.FOLDOUT_MONTH).click()

    def select_MONTH_PERIOD_STARTING(self):
        self.wait_for_element(self.MONTH_PERIOD_STARTING).click()

    def select_DAY_PERIOD_STARTING(self):
        self.wait_for_element(self.DAY_PERIOD_STARTING).click()  

    def select_YEAR_PERIOD(self):
        self.wait_for_element(self.YEAR_PERIOD).click()

    def select_FINAL_YEAR_PERIOD(self):
        self.wait_for_element(self.FINAL_YEAR_PERIOD).click() 

    def select_SELECTOR_MONTH(self):
        self.wait_for_element(self.MONTH_PERIOD).click()

    def select_MONTH_PERIOD_FINAL(self):
        self.wait_for_element(self.MONTH_PERIOD_FINAL).click()  #####

    def select_DAY_PERIOD_FINAL(self):
        self.wait_for_element(self.DAY_PERIOD_FINAL).click()

    def select_BUTTON_OK_PERIOD(self):
        self.wait_for_element(self.BUTTON_OK_PERIOD).click()

    #Targetas de metricas 
    def select_CARD_METRICS_EARNINGS(self):
        self.wait_for_element(self.CARD_METRICS_EARNINGS).click()

    def select_CARD_METRICS_AFFILIATE(self):
        self.wait_for_element(self.CARD_METRICS_AFFILIATE).click()

    def select_CARD_METRICS_REGISTRATIONS(self):
        self.wait_for_element(self.CARD_METRICS_REGISTRATIONS).click()

    def select_CARD_METRICS_FTD(self):
        self.wait_for_element(self.CARD_METRICS_FTD).click()

    def select_CARD_METRICS_CPA(self):
        self.wait_for_element(self.CARD_METRICS_CPA).click()

    def select_TOOLTIPS_EARNINGS(self):
        self.wait_for_element(self.TOOLTIPS_EARNINGS).click()

    def select_TOOLTIPS_AFFILIATE(self):
        self.wait_for_element(self.TOOLTIPS_AFFILIATE).click()

    def select_TOOLTIPS_REGISTRATIONS(self):
        self.wait_for_element(self.TOOLTIPS_REGISTRATIONS).click()

    def select_TOOLTIPS_FTD(self):
        self.wait_for_element(self.TOOLTIPS_FTD).click()

    def select_TOOLTIPS_CPA(self):
        self.wait_for_element(self.TOOLTIPS_CPA).click()

    def select_TOOLTIP_ACTUALIZATION(self):
        self.wait_for_element(self.TOOLTIP_ACTUALIZATION).click()

    def select_PREVIOUS_COMPARISON_EARNINGS(self):
        self.wait_for_element(self.PREVIOUS_COMPARISON_EARNINGS).click()

    def select_PREVIOUS_COMPARISON_AFFILIATE(self):
        self.wait_for_element(self.PREVIOUS_COMPARISON_AFFILIATE).click()

    def select_PREVIOUS_COMPARISON_REGISTRATIONS(self):
        self.wait_for_element(self.PREVIOUS_COMPARISON_REGISTRATIONS).click()

    def select_PREVIOUS_COMPARISON_FTD(self):
        self.wait_for_element(self.PREVIOUS_COMPARISON_FTD).click()

    def select_PREVIOUS_COMPARISON_CPA(self):
        self.wait_for_element(self.PREVIOUS_COMPARISON_CPA).click()

    #Error de diagrama

    def select_button_REFRESH_DATA(self):
        self.wait_for_element(self.REFRESH_DATA).click()

    #

    