from Commizzion.configuration_preferences import configurationpage
from data.data import email_configuracion
from data.data import password_configuracion
from data.data import email_confi 
from data.data import password_confi
from data.data import code1
from data.data import code2
from data.data import code3
from data.data import code4
from data.data import code5
from data.data import code6
from data.data import phone
from data.data import URL_channel
from data.data import name_channel
from data.data import url_new_channel
from data.data import name_new_channel
from data.data import country_preference
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_configuration(driver):
    confi = configurationpage(driver)
    confi.navigate_home()
    #Ingreso
    confi.select_button_email() 
    confi.select_text_email()
    confi.text_email(email_configuracion)
    confi.select_text_password()
    confi.text_password(password_configuracion)
    time.sleep(5)
    confi.select_checkbox()  
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(confi.BUTTON_LOGIN))
    confi.select_button_login()
    #ir a configuracion
    confi.select_configuration()
    #seleccion de preferencias paises 
    confi.select_configuration_preferences() 
    confi.select_confi_preferences_audience_countries() 
    confi.select_confi_preferences_audience_countries_x() 
    confi.select_confi_preferences_audience_countries_placeholder_click() 
    confi.select_confi_preferences_audience_countries_placeholder(country_preference) 
    confi.select_confi_preferences_audience_countries_more_countries() 
    confi.select_confi_preferences_audience_countries_chips() 
    confi.select_confi_preferences_audience_countries_save() 
    confi.select_confi_preferences_audience_countries_yes() 
    #seleccion de preferencias objetivos 
    confi.select_confi_preferences_objetive() 
    confi.select_confi_preferences_obj_select() 
    confi.select_confi_preferences_audience_objetive_save() 
    confi.select_confi_preferences_audience_objetive_yes() 