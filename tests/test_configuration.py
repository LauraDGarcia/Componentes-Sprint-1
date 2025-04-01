from Commizzion.configuration import configurationpage
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

#Haria falta el ingresar a la cuenta

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
    #perfil correo 
    confi.select_confi_profile_email_and_password() 
    confi.select_confi_profile_email() 
    confi.select_confi_profile_email_buttoncheck() 
    confi.select_confi_profile_email_buttoncontinue() 
    confi.select_confi_profile_email_buttoncance() 
    confi.text_code() 
    confi.get_code1(code1) 
    confi.get_code2(code2) 
    confi.get_code3(code3) 
    confi.get_code4(code4) 
    confi.get_code5(code5) 
    confi.get_code6(code6) 
    confi.select_confi_profile_email_buttonnext() 
    confi.select_confi_profile_new_email() 
    confi.select_confi_profile_new_email_text(email_confi) 
    confi.select_confi_profile_confirm_email() 
    confi.select_confi_profile_confirm_email_text(email_confi) 
    confi.select_confi_profile_save_email() 
    confi.text_code_new() 
    confi.get_code1_new(code1) 
    confi.get_code2_new(code2) 
    confi.get_code3_new(code3) 
    confi.get_code4_new(code4) 
    confi.get_code5_new(code5) 
    confi.get_code6_new(code6) 
    confi.select_confi_profile_email_new_buttonnext() 
    confi.select_confi_profile_dialog_email_yes() 
    #perfil contraseña 
    confi.select_confi_profile_email_and_password() 
    confi.select_confi_profile_current_password() 
    confi.select_confi_profile_current_password_text(password_configuracion) 
    confi.select_confi_profile_new_password() 
    confi.select_confi_profile_new_password_text(password_confi) 
    confi.select_confi_profile_confirm_password() 
    confi.select_confi_profile_confirm_password_text(password_confi) 
    confi.select_confi_profile_save_password() 
    confi.select_confi_profile_dialog_password_yes() 
    #perfil contact and location information 
    confi.select_confi_profile_contact_location() 
    confi.select_confi_profile_country() 
    confi.select_confi_profile_new_country() 
    confi.select_confi_profile_country_code() 
    confi.select_confi_profile_new_country_code() 
    confi.select_confi_profile_x_phone() 
    confi.select_confi_profile_phone() 
    confi.select_confi_profile_phone_text(phone) 
    confi.select_confi_profile_language() 
    confi.select_confi_profile_new_language() 
    confi.select_confi_profile_save_contact_location() 
    confi.select_confi_profile_cancel_contact_location() 
    confi.select_confi_profile_dialog_contact_location_yes() 
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
    #configuración ayuda 
    confi.select_configuration_help() 