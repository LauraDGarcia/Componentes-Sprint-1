from Sprint2.campaigns import campaignspage
from data.data import email_Campaña
from data.data import password_campaña
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Haria falta el ingresar a la cuenta

def test_panel_actions(driver):
    campaigns = campaignspage(driver)
    campaignspage.navigate_home()
    #Ingreso
    campaigns.select_button_email() 
    campaigns.select_text_email()
    campaigns.text_email(email_Campaña) 
    campaigns.select_text_password()
    campaigns.text_password(password_campaña)
    #seleccionar campañas
    campaigns.select_CAMPAIGNS_AND_MARKET()
    campaigns.select_CAMPAIGNS()
    #Selccion de filtros 
    campaigns.select_FILTER_DROPDOWN()
    campaigns.select_FILTER_HIGHEST_INCOME()
    campaigns.select_FILTER_DROPDOWN()
    campaigns.select_FILTER_LOWEST_INCOME()
    campaigns.select_FILTER_DROPDOWN()
    campaigns.select_FILTER_HIGHEST_DEPOSIT()
    campaigns.select_FILTER_DROPDOWN()
    campaigns.select_FILTER_LOWEST_DEPOSIT()
    campaigns.select_FILTER_CLEAR()
    campaigns.select_FILTER_CPA()
    campaigns.select_FILTER_CLEAR()
    campaigns.select_FILTER_RS()
    campaigns.select_FILTER_CLEAR()
    #seleccionar link 
    campaigns.select_SEE_DETAILS()
    campaigns.select_PROMOTE_CAMPAIGNS_LINK1()
    campaigns.select_CHECK_TYC_LINK()
    campaigns.select_BUTTON_CREATE_LINK()
    campaigns.select_COPY_LINK()
    campaigns.select_BUTTON_FINISH()
    campaigns.select_REQUEST_LINK2_DESDE_ELMAS()
    campaigns.select_BUTTON_CLOSE()
    campaigns.select_BUTTON_COPY_LINK()
    campaigns.select_BUTTON_FINAL()
    
