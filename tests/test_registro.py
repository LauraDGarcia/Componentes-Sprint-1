from Commizzion.signin import signinpage
from data.data import name
from data.data import lastname
from data.data import new_email
from data.data import phone
from data.data import new_password
from data.data import code1
from data.data import code2
from data.data import code3
from data.data import code4
from data.data import code5
from data.data import code6
from data.data import channel1_link
from data.data import name_channel1
from data.data import textfield
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_form_signin(driver):
    signin = signinpage(driver)
    signin.navigate_home()
    signin.select_button_email()
    signin.select_text_name(name)
    signin.select_text_lastname(lastname)
    signin.select_text_email(new_email)
    signin.code_phone1()
    signin.code_phone2()
    signin.code_phone3()
    signin.code_phone4(phone)
    signin.select_password(new_password)
    signin.confirm_password(new_password) 
    signin.select_afuera() ############
    time.sleep(5)
    signin.select_checkbox()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(signin.TYC_CHECKBOX))
    time.sleep(40)
    signin.select_tyc()
    time.sleep(10)
    signin.select_button()
    signin.text_code()
    signin.get_code1(code1)
    signin.get_code2(code2)
    signin.get_code3(code3)
    signin.get_code4(code4)
    signin.get_code5(code5)
    signin.get_code6(code6)
    time.sleep(60)
    signin.select_button3()
    #perfilamiento canales
    signin.select_channel()
    signin.get_link_channel1(channel1_link)
    signin.get_name_channel1(name_channel1)
    signin.select_button_add_channel()
    signin.select_button_edit_details()
    signin.select_button_cancel()
    signin.select_button_next()
    #Perfilamiento tipo de usuario 
    signin.select_tooltip_user()
    signin.select_tooltip_other()
    signin.select_text_field(textfield)
    signin.select_next_button()
    #Perfilamiento de trafico
    signin.select_chip()
    signin.select_chips_other()
    signin.select_chips_text(textfield)
    signin.select_button_next_seven()
    #Perfilamiento de pais
    signin.select_countries_america()
    signin.select_countries_europa()
    signin.select_countries_asia()
    signin.select_countries_africa()
    signin.select_button_back3()
    signin.select_button_next7()
    #Perfilamiento de objetivos 
    signin.select_chip_objetive()
    signin.select_button_back()
    signin.select_button_finish()
    #