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
    #Perfil correo
    confi.select_CONFI_PROFILE_EMAIL_AND_PASSWORD()
    confi.select_CONFI_PROFILE_EMAIL()
    confi.select_CONFI_PROFILE_EMAIL_BUTTONCHECK()
    confi.select_CONFI_PROFILE_EMAIL_BUTTONCONTINUE()
    confi.select_CONFI_PROFILE_EMAIL_BUTTONCANCE()
    confi.text_code()
    confi.get_code1(code1)
    confi.get_code2(code2)
    confi.get_code3(code3)
    confi.get_code4(code4)
    confi.get_code5(code5)
    confi.get_code6(code6)
    confi.select_CONFI_PROFILE_EMAIL_BUTTONNEXT()
    confi.select_CONFI_PROFILE_NEW_EMAIL()
    confi.select_CONFI_PROFILE_NEW_EMAIL_text(email_confi)
    confi.select_CONFI_PROFILE_CONFIRM_EMAIL()
    confi.select_CONFI_PROFILE_CONFIRM_EMAIL_text(email_confi)
    confi.select_CONFI_PROFILE_SAVE_EMAIL()
    confi.text_code_new()
    confi.get_code1_new(code1)
    confi.get_code2_new(code2)
    confi.get_code3_new(code3)
    confi.get_code4_new(code4)
    confi.get_code5_new(code5)
    confi.get_code6_new(code6)
    confi.select_CONFI_PROFILE_EMAIL_NEW_BUTTONNEXT()
    confi.select_CONFI_PROFILE_DIALOG_EMAIL_YES()
    #Perfil contraseña
    confi.select_CONFI_PROFILE_EDIT_PASSWORD()
    confi.select_CONFI_PROFILE_CURRENT_PASSWORD()
    confi.select_CONFI_PROFILE_CURRENT_PASSWORD_text(password_configuracion)
    confi.select_CONFI_PROFILE_NEW_PASSWORD()
    confi.select_CONFI_PROFILE_NEW_PASSWORD_text(password_confi)
    confi.select_CONFI_PROFILE_CONFIRM_PASSWORD()
    confi.select_CONFI_PROFILE_CONFIRM_PASSWORD_text(password_confi)
    confi.select_CONFI_PROFILE_SAVE_PASSWORD()
    confi.select_CONFI_PROFILE_DIALOG_PASSWORD_YES()
    #Perfil Contact and Location Information
    confi.select_CONFI_PROFILE_CONTACT_LOCATION()
    confi.select_CONFI_PROFILE_COUNTRY()
    confi.select_CONFI_PROFILE_NEW_COUNTRY()
    confi.select_CONFI_PROFILE_COUNTRY_CODE()
    confi.select_CONFI_PROFILE_NEW_COUNTRY_CODE()
    confi.select_CONFI_PROFILE_X_PHONE()
    confi.select_CONFI_PROFILE_PHONE()
    confi.select_CONFI_PROFILE_PHONE_text(phone)
    confi.select_CONFI_PROFILE_LANGUAGE()
    confi.select_CONFI_PROFILE_NEW_LANGUAGE()
    confi.select_CONFI_PROFILE_SAVE_CONTACT_LOCATION()
    confi.select_CONFI_PROFILE_CANCEL_CONTACT_LOCATION()
    confi.select_CONFI_PROFILE_DIALOG_CONTACT_LOCATION_YES()
    #Seleccion de canales
    confi.select_CONFIGURATION_CHANNELS()
    confi.select_CONFI_CHANNELS_3_POINTS()
    confi.select_CONFI_CHANNELS_EDIT_CHANNEL1_BUTTON()
    confi.select_CONFI_CHANNELS_EDIT_URL_X()
    confi.select_CONFI_CHANNELS_EDIT_URL(URL_channel)
    confi.select_CONFI_CHANNELS_EDIT_NAME_X()
    confi.select_CONFI_CHANNELS_EDIT_NAME(name_channel)
    confi.select_CONFI_CHANNELS_EDIT_SAVE()
    confi.select_CONFI_CHANNELS_EDIT_CHANNEL1_YES()
    confi.select_CONFI_CHANNELS_ADD_NEW_CHANNEL()
    confi.select_CONFI_CHANNELS_NEW_URL_click()
    confi.select_CONFI_CHANNELS_NEW_URL(url_new_channel)
    confi.select_CONFI_CHANNELS_NEW_NAME_click()
    confi.select_CONFI_CHANNELS_NEW_NAME(name_new_channel)
    confi.select_CONFI_CHANNELS_SAVE_NEW_CHANNEL()
    confi.select_CONFI_CHANNELS_DELETE_CHANNEL()
    confi.select_CONFI_CHANNELS_DELETE_CHANNEL_YES()
    #Seleccion de preferencias paises
    confi.select_CONFIGURATION_PREFERENCES()
    confi.select_CONFI_PREFERENCES_AUDIENCE_COUNTRIES()
    confi.select_CONFI_PREFERENCES_AUDIENCE_COUNTRIES_X()
    confi.select_CONFI_PREFERENCES_AUDIENCE_COUNTRIES_PLACEHOLDER_click()
    confi.select_CONFI_PREFERENCES_AUDIENCE_COUNTRIES_PLACEHOLDER(country_preference)
    confi.select_CONFI_PREFERENCES_AUDIENCE_COUNTRIES_MORE_COUNTRIES()
    confi.select_CONFI_PREFERENCES_AUDIENCE_COUNTRIES_CHIPS()
    confi.select_CONFI_PREFERENCES_AUDIENCE_COUNTRIES_SAVE()
    confi.select_CONFI_PREFERENCES_AUDIENCE_COUNTRIES_YES()
    #Seleccion de preferencias objetivos
    confi.select_CONFI_PREFERENCES_OBJETIVE()
    confi.select_CONFI_PREFERENCES_OBJ_SELECT()
    confi.select_CONFI_PREFERENCES_AUDIENCE_OBJETIVE_SAVE()
    confi.select_CONFI_PREFERENCES_AUDIENCE_OBJETIVE_YES()
    #Configuración ayuda
    confi.select_CONFIGURATION_HELP()

