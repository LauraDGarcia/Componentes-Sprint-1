from Commizzion.signup import signuppage
from data.data import name
from data.data import lastname
from data.data import new_email
from data.data import phone
from data.data import number
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

def test_form_signup(driver):
    signup = signuppage(driver)
    signup.navigate_home()
    signup.select_button_email()
    signup.select_text_name(name)
    signup.select_text_lastname(lastname)
    signup.select_text_email(new_email)
    signup.code_phone1()
    signup.code_phone2()
    signup.code_phone3()
    signup.code_phone4(phone)
    signup.select_doc_type()
    signup.select_type()
    signup.select_doc_number(number)
    signup.select_password(new_password)
    signup.confirm_password(new_password) 
    signup.select_afuera() ############
    time.sleep(5)
    signup.select_checkbox()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(signup.TYC_CHECKBOX))
    time.sleep(40)
    signup.select_tyc()
    time.sleep(10)
    signup.select_button()
    signup.select_dialog()
    signup.text_code()
    signup.get_code1(code1)
    signup.get_code2(code2)
    signup.get_code3(code3)
    signup.get_code4(code4)
    signup.get_code5(code5)
    signup.get_code6(code6)
    time.sleep(60)
    signup.select_button3()
    #perfilamiento canales
    time.sleep(20)
    signup.select_channel()
    signup.get_link_channel1(channel1_link)
    signup.get_name_channel1(name_channel1)
    signup.select_button_add_channel()
    signup.select_button_edit_details()
    signup.select_button_cancel()
    signup.select_button_next()
    #Perfilamiento tipo de usuario 
    signup.select_tooltip_user()
    signup.select_tooltip_other()
    #signup.select_text_field
    #signup.select_text_field_text(textfield)
    signup.select_next_button()
    #Perfilamiento de trafico
    signup.select_chip()
    signup.select_chips_other()
    signup.select_chips_text
    signup.select_chips_text_text(textfield)
    signup.select_button_next_seven()
    #Perfilamiento de pais
    signup.select_countries_america() 
    signup.select_countries_europa()
    signup.select_countries_asia()
    signup.select_countries_africa()
    signup.select_button_next7()
    #Perfilamiento de objetivos 
    signup.select_chip_objetive()
    signup.select_button_finish()