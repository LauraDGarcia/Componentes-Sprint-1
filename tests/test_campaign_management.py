from Commizzion.campaign_management import managementpage
from data.data import email_Campaña
from data.data import password_campaña
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#ingresar a la cuenta
def test_management(driver):
    managemen = managementpage(driver)
    managemen.navigate_home()
    #Ingreso
    managemen.select_button_email() 
    managemen.select_text_email()
    managemen.text_email(email_Campaña) 
    managemen.select_text_password()
    managemen.text_password(password_campaña)
    time.sleep(5)
    managemen.select_checkbox()  
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(managemen.button_login))
    managemen.select_button_login()
    #seleccionar campañas
    managemen.select_campaigns_and_market() 
    managemen.select_management() 
    #selccion de filtros  
    managemen.select_filter_dropdown() 
    managemen.select_filter_highest_income() 
    time.sleep(10) 
    managemen.select_filter_dropdown() 
    managemen.select_filter_lowest_income() 
    time.sleep(10) 
    managemen.select_filter_dropdown() 
    managemen.select_filter_highest_deposit() 
    time.sleep(10) 
    managemen.select_filter_dropdown() 
    managemen.select_filter_lowest_deposit() 
    time.sleep(10) 
    managemen.select_filter_clear() 
    managemen.select_filter_cpa() 
    time.sleep(10) 
    managemen.select_filter_clear() 
    managemen.select_filter_rs() 
    time.sleep(10) 
    managemen.select_filter_clear() 
    managemen.select_filter_textarea_manual_click() 
    time.sleep(5) 
    managemen.select_filter_textarea_manual("México") 
    time.sleep(10) 
    managemen.select_filter_textarea_select() 
    time.sleep(10) 
    managemen.select_filter_textarea_x() 
    time.sleep(5) 
    managemen.select_filter_textarea_manual_click() 
    managemen.select_filter_placeholder_status() 
    time.sleep(10) 
    managemen.select_filter_textarea_x() 
    managemen.select_filter_textarea_manual_click() 
    managemen.select_filter_placeholder_countries() 
    time.sleep(10) 
    managemen.select_filter_textarea_x() 
    managemen.select_filter_textarea_manual_click() 
    managemen.select_filter_placeholder_operator() 
    time.sleep(10) 
    managemen.select_filter_textarea_x() 
    managemen.select_filter_chips() 
    managemen.select_filter_chips_active() 
    managemen.select_filter_chips_x() 
    managemen.select_filter_chips_closed() 
    managemen.select_filter_chips_x() 
    managemen.select_filter_chips_suspended() 
    managemen.select_filter_chips_x() 
    managemen.select_filter_chips_argentina() 
    managemen.select_filter_chips_x() 
    managemen.select_filter_chips_888sport() 
    managemen.select_filter_chips_x() 
    time.sleep(10) 
    managemen.select_filter_chips_active() 
    managemen.select_filter_chips_status() 
    managemen.select_filter_chips_argentina() 
    managemen.select_filter_chips_more_countries() 
    managemen.select_filter_chips_spain() 
    managemen.select_filter_chips_fewer_countries() 
    managemen.select_filter_chips_countries() 
    managemen.select_filter_chips_888sport() 
    managemen.select_filter_chips_more_operators() 
    managemen.select_filter_chips_1win() 
    managemen.select_filter_chips_fewer_operators() 
    managemen.select_filter_chips_operator() 
    managemen.select_filter_chips_apply() 
    managemen.select_filter_clear() 
    #seleccionar link  
    managemen.select_see_details() 
    managemen.select_promote_campaigns_link1() 
    managemen.select_check_tyc_link() 
    managemen.select_button_create_link() 
    managemen.select_copy_link() 
    time.sleep(5) 
    managemen.select_button_finish() 
    managemen.select_request_link2_desde_elmas() 
    managemen.select_button_close() 
    managemen.select_button_copy_link() 
    managemen.select_button_final() 

 

   