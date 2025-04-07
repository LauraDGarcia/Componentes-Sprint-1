from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class signinpage(BasePage):
    #EMAIL_GOOGLE = (By.XPATH, "")
    #SELECT_ACCOUNT = (By.XPATH, "")
    #NEXT_BUTTON_ONE = (By.XPATH, "")
    #CANCEL_BUTTON_ONE = (By.XPATH, "")
    SELECT_EMAIL = (By.XPATH, "//span[contains(.,'Usar correo electrónico')]")
    NAME = (By.XPATH, "//input[contains(@name,'name')]")
    LASTNAME = (By.XPATH, "//input[contains(@name,'lastName')]")
    EMAIL = (By.XPATH, "//input[contains(@name,'email')]")
    PHONE_INDICATOR = (By.XPATH, "(//div[contains(@class,'7')])[5]")
    NUMBER_INDICATOR = (By.XPATH, "//li[contains(.,'+57')]")
    PHONE = (By.XPATH, "//input[contains(@name,'phoneNumber')]")
    PASSWORD = (By.XPATH, "//input[contains(@name,'password')]")
    CONFIRM_PASSWORD = (By.XPATH, "//input[contains(@name,'confirmPassword')]") 
    CLICKAFUERA = (By.XPATH, "//section[contains(@class,'3947j')]")  #######
    CHECKBOX_C= (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/section/form/div[2]") #######
    TYC_CHECKBOX = (By.XPATH, "//input[@type='checkbox']")
    NEXT_BUTTON_TWO = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/section/form/button")
    #verificación de correo
    DIALOG = (By.XPATH, "//*[@id='_button--standard_9pqly_1']")
    CODEONE = (By.XPATH, "//input[contains(@id,'otp-input-0')]")
    CODETWO = (By.XPATH, "//input[contains(@id,'otp-input-1')]")
    CODETHREE = (By.XPATH, "//input[contains(@id,'otp-input-2')]")
    CODEFOUR = (By.XPATH, "//input[contains(@id,'otp-input-3')]")
    CODEFIVE = (By.XPATH, "//input[contains(@id,'otp-input-4')]")
    CODESIX = (By.XPATH, "//input[contains(@id,'otp-input-5')]")
    RESEND_CODE = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/article/button[1]")
    CODE_NOT_YET_RECEIVED = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/article/button[2]")
    NEXT_BUTTON_THREE = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/article/div/button")
    #Stepper canal de comunicación
    ADD_CHANNEL1 = (By.XPATH, "/html/body/div[1]/div/div/div/div/div/section/div[2]/div/div/div[1]/button")
    LINK_CHANNEL1 = (By.XPATH, "//input[@placeholder='https://']")
    CHANNEL_NAME =(By.XPATH, "(//input[@type='url'])[2]")
    ADD_CHANNEL_BUTTON = (By.XPATH, "//button[contains(@class,'VAYNO')]")
    CANCEL_BUTTON_TWO = (By.XPATH, "//button[contains(@class,'wmtDK')]")
    NEXT_BUTTON_FOUR = (By.XPATH, "(//button[contains(@class,'42')])[2]")
    EDIT_DETAILS1 = (By.XPATH, "(//button[contains(@class,'q')])[6]")
    #Tipo de usuario
    TOOLTIP_USER = (By.XPATH, "(//p[contains(@class,'')])[4]")
    TOOLTIP_OTHER_ONE = (By.XPATH, "/html/body/div[1]/div/div/div/div/div/section/div[2]/div/div[1]/div[5]")
    TEXT_FIELD = (By.XPATH, "//textarea[contains(@maxlength,'100')]")
    BACK_BUTTON_ONE = (By.XPATH, "//button[contains(@class,'76')]")
    NEXT_BUTTON_FIVE = (By.XPATH, "//button[contains(@class,'42')]")
    #Queremos saber más
    CHIPS = (By.XPATH, "(//span[contains(@class,'1')])[12]")
    CHIP_OTHER_TWO = (By.XPATH, "(//span[contains(@class,'1')])[22]")
    CHIP_TEXT_FIELD = (By.XPATH, "//textarea[@maxlength='100']")
    BACK_BUTTON_TWO = (By.XPATH, "//button[contains(@class,'76')]")
    NEXT_BUTTON_SIX = (By.XPATH, "//button[contains(@class,'42')]")
    #paises de audiencia
    COUNTRIES_CHIPS_AMERICA = (By.XPATH, "(//span[contains(@class,'1')])[34]")
    COUNTRIES_CHIPS_EUROPA = (By.XPATH, "(//span[contains(@class,'1')])[46]")
    COUNTRIES_CHIPS_ASIA = (By.XPATH, "(//span[contains(@class,'1')])[54]")
    COUNTRIES_CHIPS_AFRICA = (By.XPATH, "(//span[contains(@class,'1')])[56]")
    BACK_BUTTON_THREE = (By.XPATH, "(//button[contains(@class,'76')])[2]")
    NEXT_BUTTON_SEVEN = (By.XPATH, "//button[contains(@class,'42')]")
    #Objetivos
    CHIP_OBJETIVES = (By.XPATH, "/html/body/div[1]/div/div/div/div/div/section/div[2]/div/div/div[1]")
    BACK_BUTTON_FOUR = (By.XPATH, "//button[contains(@class,'76')]")
    SAVE_BUTTON = (By.XPATH, "//button[contains(@class,'42 finalize-button')]")
    
    def navigate_home(self):
        self.go_to_page("https://qa-account-commizzion-vm.inlazetest.com/register")

    def  select_dropdown(self, locator, index):
        self.select_dropdown_by_visible_text(self.localizador ) 

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))      

    #Crear cuanta con google
    def select_email_google(self):
        self.wait_for_element(self.EMAIL_GOOGLE).click()

    def select_google(self):
        self.wait_for_element(self.SELECT_ACCOUNT)


    #Crear cuenta con correo y llenado de formulario
    def select_button_email(self):
        self.wait_for_element(self.SELECT_EMAIL).click()

    def select_text_name(self, name):
        self.wait_for_element(self.NAME).click()
        element = self.wait_for_element(self.NAME)
        element.clear() 
        element.send_keys(name)

    def select_text_lastname(self, lastname):
        self.wait_for_element(self.LASTNAME).click()
        element = self.wait_for_element(self.LASTNAME) 
        element.clear() 
        element.send_keys(lastname)

    def select_text_email(self, new_email):
        self.wait_for_element(self.EMAIL).click()
        element = self.wait_for_element(self.EMAIL)
        element.clear() 
        element.send_keys(new_email)
    
    def code_phone1(self):
        self.wait_for_element(self.PHONE_INDICATOR).click()

    def code_phone2(self):
        self.wait_for_element(self.NUMBER_INDICATOR).click()

    def code_phone3(self):
        self.wait_for_element(self.PHONE).click()

    def code_phone4(self, phone):
        element = self.wait_for_element(self.PHONE)
        element.clear() 
        element.send_keys(phone)  

    def select_password(self, new_password):
        self.wait_for_element(self.PASSWORD).click()
        element = self.wait_for_element(self.PASSWORD)
        element.clear() 
        element.send_keys(new_password)

    def confirm_password(self, new_password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CONFIRM_PASSWORD)
        )
        element = self.wait_for_element(self.CONFIRM_PASSWORD)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.clear() 
        element.send_keys(new_password) 

    def select_afuera(self):
        self.wait_for_element(self.CLICKAFUERA).click() 

    def select_checkbox(self):
        checkbox_element = self.wait_for_element(self.CHECKBOX_C)
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.CHECKBOX_C))  # Esperar que sea clickeable
        checkbox_element.click() 

    def select_tyc(self):
        tyc = self.wait_for_element(self.TYC_CHECKBOX)
        self.driver.execute_script("window.scrollTo(0,1550)", tyc)
        tyc.click()

    def select_button(self):
        self.wait_for_element(self.NEXT_BUTTON_TWO).click()

    #Verificación de correo
    def select_dialog(self):
        self.wait_for_element(self.DIALOG).click()
        
    def text_code(self):
        self.wait_for_element(self.CODEONE).click()

    def get_code1(self, code1):
        element = self.wait_for_element(self.CODEONE)
        element.clear() 
        element.send_keys(code1)

    def get_code2(self, code2):
        element = self.wait_for_element(self.CODETWO)
        element.clear() 
        element.send_keys(code2)

    def get_code3(self, code3):
        element = self.wait_for_element(self.CODETHREE)
        element.clear() 
        element.send_keys(code3)

    def get_code4(self, code4):
        element = self.wait_for_element(self.CODEFOUR)
        element.clear() 
        element.send_keys(code4)

    def get_code5(self, code5):
        element = self.wait_for_element(self.CODEFIVE)
        element.clear() 
        element.send_keys(code5)
        
    def get_code6(self, code6):
        element = self.wait_for_element(self.CODESIX)
        element.clear() 
        element.send_keys(code6)

    def select_button3(self):
        self.wait_for_element(self.NEXT_BUTTON_THREE).click()

    #Perfilamiento canales 
    def select_channel(self):
        self.wait_for_element(self.ADD_CHANNEL1).click()

    def get_link_channel1(self, channel1_link):
        self.wait_for_element(self.LINK_CHANNEL1).click()
        element = self.wait_for_element(self.LINK_CHANNEL1)
        element.clear() 
        element.send_keys(channel1_link)

    def get_name_channel1(self, name_channel1):
        self.wait_for_element(self.CHANNEL_NAME).click()
        element = self.wait_for_element(self.CHANNEL_NAME)
        element.clear() 
        element.send_keys(name_channel1)

    def select_button_add_channel(self):
        #self.wait_for_element(self.ADD_CHANNEL_BUTTON).click()
        button_channel = self.wait_for_element(self.ADD_CHANNEL_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView()", button_channel)
        button_channel.click()

    def select_button_edit_details(self):
        self.wait_for_element(self.EDIT_DETAILS1).click()

    def select_button_cancel(self):
        self.wait_for_element(self.CANCEL_BUTTON_TWO).click()

    def select_button_next(self):
        self.wait_for_element(self.NEXT_BUTTON_FOUR).click()

    #Perfilamiento tipo de usuario 

    def select_tooltip_user(self):
        self.wait_for_element(self.TOOLTIP_USER).click()

    def select_tooltip_other(self):
        self.wait_for_element(self.TOOLTIP_OTHER_ONE).click()

    def select_text_field(self, text):
        self.wait_for_element(self.TEXT_FIELD).click()
        element = self.wait_for_element(self.TEXT_FIELD)
        element.clear() 
        element.send_keys(text)

    def select_next_button(self):
        self.wait_for_element(self.NEXT_BUTTON_FIVE).click()

    #Perfilamiento de trafico

    def select_chip(self):
        self.wait_for_element(self.CHIPS).click()

    def select_chips_other(self):
        self.wait_for_element(self.CHIP_OTHER_TWO).click()

    def select_chips_text(self, text):
        self.wait_for_element(self.CHIP_TEXT_FIELD).click()
        element = self.wait_for_element(self.TEXT_FIELD)
        element.clear() 
        element.send_keys(text)

    def select_button_next_seven(self):
        self.wait_for_element(self.NEXT_BUTTON_SIX).click()

    #Perfilamiento de pais

    def select_countries_america(self): #####aca voy porque no cargo el restante del codigo porque flaypo
        self.wait_for_element(self.COUNTRIES_CHIPS_AMERICA).click()

    def select_countries_europa(self):
        self.wait_for_element(self.COUNTRIES_CHIPS_EUROPA).click()

    def select_countries_asia(self):
        self.wait_for_element(self.COUNTRIES_CHIPS_ASIA).click()

    def select_countries_africa(self):
        self.wait_for_element(self.COUNTRIES_CHIPS_AFRICA).click()

    def select_button_back3(self):
        self.wait_for_element(self.BACK_BUTTON_THREE).click()

    def select_button_next7(self):
        self.wait_for_element(self.NEXT_BUTTON_SEVEN).click()

    #Perfilamiento de objetivos 

    def select_chip_objetive(self):
        self.wait_for_element(self.CHIP_OBJETIVES).click()

    def select_button_back(self):
        self.wait_for_element(self.BACK_BUTTON_FOUR).click()

    def select_button_finish(self):
        self.wait_for_element(self.SAVE_BUTTON).click
