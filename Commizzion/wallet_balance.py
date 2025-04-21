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
    #Boton de wallet
    button_wallet = (By.XPATH, "(//span[contains(@class,'i6Cf7')])[6]")
    button_balance = (By.XPATH, "(//span[contains(@class,'i6Cf7')])[7]")
    button_eye_balance = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[3]/div[1]/div[1]/div[1]/button")
    icon_total_balance = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[1]/div[1]/div/i/svg")
    icon_incoming_balance = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[1]/div/i/svg")
    icon_value_receive = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[3]/div[1]/div/i/svg")