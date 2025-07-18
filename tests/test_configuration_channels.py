from Commizzion.configuration_channels import configurationpage
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
    #seleccion de canales 
    confi.select_configuration_channelS() 
    confi.select_confi_channels_3_points() 
    confi.select_confi_channels_edit_channel1_button() 
    confi.select_confi_channels_edit_url_x() 
    confi.select_confi_channels_edit_url(URL_channel) 
    confi.select_confi_channels_edit_name_x() 
    confi.select_confi_channels_edit_name(name_channel) 
    confi.select_confi_channels_edit_save() 
    confi.select_confi_channels_edit_channel1_yes() 
    confi.select_confi_channels_add_new_channel() 
    confi.select_confi_channels_new_url_click() 
    confi.select_confi_channels_new_url(url_new_channel) 
    confi.select_confi_channels_new_name_click() 
    confi.select_confi_channels_new_name(name_new_channel) 
    confi.select_confi_channels_save_new_channel() 
    confi.select_confi_channels_delete_channel() 
    confi.select_confi_channels_delete_channel_yes() 