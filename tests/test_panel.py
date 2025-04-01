from Commizzion.panel import panelpage
from data.data import email_panel
from data.data import password_panel
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Haria falta el ingresar a la cuenta

def test_panel_actions(driver):
    panel = panelpage(driver)
    panel.navigate_home()
    #panel
    panel.select_button_email() 
    panel.select_text_email()
    panel.text_email(email_panel) # ingresar correo 
    panel.select_text_password()
    panel.text_password(password_panel)  # Ingresar contraseña
    time.sleep(5)
    panel.select_checkbox()  # Resolver CAPTCHA manualmente  buscar como no hacerlo manual
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(panel.BUTTON_LOGIN))
    panel.select_button_login()
    #Panel
    panel.visual_wallet_eye()
    panel.icon_balance_wallet()
    panel.icon_earned_wallet()
    panel.icon_paid_wallet()
    panel.main_period()                                
    panel.select_period_yesterday()
    panel.main_period()
    panel.select_period_last_month()
    panel.main_period()
    panel.select_period_custom()
    panel.select_previous_month()
    panel.select_next_month()
    panel.select_previous_year()
    panel.select_next_year()
    panel.select_year_period() 
    panel.select_foldout_year() 
    panel.select_new_year_period() 
    panel.select_month_period() 
    panel.select_foldout_month() 
    panel.select_month_period_starting() 
    panel.select_day_period_starting()   
    panel.select_year_period() 
    panel.select_final_year_period()  
    time.sleep(5) 
    panel.select_selector_month() 
    panel.select_month_period_final() 
    time.sleep(5) 
    panel.select_day_period_final() 
    panel.select_button_ok_period() 
    panel.select_card_metrics_earnings() 
    panel.select_card_metrics_affiliate() 
    panel.select_card_metrics_registrations() 
    panel.select_card_metrics_FTD() 
    panel.select_card_metrics_CPA() 
    panel.select_tooltips_earnings() 
    panel.select_tooltips_affiliate() 
    panel.select_tooltips_registrations() 
    panel.select_tooltips_FTD() 
    panel.select_tooltips_CPA() 
    #panel.select_tooltip_actualization() ### 
    panel.select_previous_comparison_earnings()  
    #panel.select_previous_comparison_affiliate() ##tener en cuenta cuando si hay ganancias por afiliado 
    panel.select_previous_comparison_registrations() 
    panel.select_previous_comparison_FTD() 
    panel.select_previous_comparison_CPA() 
