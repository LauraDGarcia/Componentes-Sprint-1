from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class panelpage(BasePage):
    #Ingreso normal
    SELECT_EMAIL = (By.XPATH, "//button[contains(.,'Correo electrónico')]")
    EMAIL = (By.XPATH, "//input[contains(@name,'email')]")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    BUTTON_C = (By.CLASS_NAME, "page_captcha__auNDN")
    BUTTON_LOGIN = (By.XPATH, "//button[contains(@type,'submit')]")
    #seleccionar la pestaña de campañas y admin
    CAMPAIGNS_AND_MARKET = (By.XPATH, "/html/body/div[1]/div[1]/section/ul[1]/li[2]/button/span[2]")
    CAMPAIGNS = (By.XPATH, "(//span[contains(@class,'i6Cf7')])[3]")
    #Filtros de campañas
    FILTER_DROPDOWN = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div[1]/fieldset/label/div/i")
    FILTER_HIGHEST_INCOME = (By.XPATH, "(//span[contains(@class,'1')])[12]")
    FILTER_LOWEST_INCOME = (By.XPATH, "(//span[contains(@class,'1')])[13]")
    FILTER_HIGHEST_DEPOSIT = (By.XPATH, "(//span[contains(@class,'1')])[14]")
    FILTER_LOWEST_DEPOSIT = (By.XPATH, "(//span[contains(@class,'1')])[15]")
    FILTER_CPA = (By.XPATH, "")
    FILTER_RS = (By.XPATH, "")
    FILTER_TEXTAREA = (By.XPATH, "")
    FILTER = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/button")
    FILTER_CHIPS = (By.XPATH, "")
    FILTER_CLEAR = (By.XPATH, "")
    #Seleccionar y crear link de campañas
    SEE_DETAILS = (By.XPATH, "(//button[contains(@class,'8tKuM')])[1]")
    PROMOTE_CAMPAIGNS_LINK1 = (By.XPATH, "(//button[@type='button'])[2]")
    CHECK_TYC_LINK = (By.XPATH, "//span[@class='_checkbox__icon_1txi3_33']")
    BUTTON_CREATE_LINK = (By.XPATH, "(//button[contains(@class,'oy16')])[2]")
    BUTTON_BACK = (By.XPATH, "(//button[contains(@class,'oy16')])[1]")
    COPY_LINK = (By.XPATH, "//button[contains(@class,'9NXqg ')]")
    BUTTON_FINISH = (By.XPATH, "//button[contains(@class,'v0upz')]")
    REQUEST_LINK2 = (By.XPATH, "//span[contains(.,'Request link')]")
    BUTTON_CLOSE = (By.XPATH, "//span[contains(.,'Close')]")
    BUTTON_COPY_LINK = (By.XPATH, "(//span[contains(.,'Copy link')])[2]")





