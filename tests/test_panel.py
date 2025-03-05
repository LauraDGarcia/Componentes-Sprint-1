from Sprint2.panel import panelpage
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
    panel.select_YEAR_PERIOD()
    panel.select_FOLDOUT_YEAR()
    panel.select_NEW_YEAR_PERIOD()
    panel.select_MONTH_PERIOD()
    panel.select_FOLDOUT_MONTH()
    panel.select_MONTH_PERIOD_STARTING()
    panel.select_DAY_PERIOD_STARTING()  
    panel.select_YEAR_PERIOD()
    panel.select_FINAL_YEAR_PERIOD() 
    time.sleep(5)
    panel.select_SELECTOR_MONTH()
    panel.select_MONTH_PERIOD_FINAL()
    time.sleep(5)
    panel.select_DAY_PERIOD_FINAL()
    panel.select_BUTTON_OK_PERIOD()
    panel.select_CARD_METRICS_EARNINGS()
    panel.select_CARD_METRICS_AFFILIATE()
    panel.select_CARD_METRICS_REGISTRATIONS()
    panel.select_CARD_METRICS_FTD()
    panel.select_CARD_METRICS_CPA()
    panel.select_TOOLTIPS_EARNINGS()
    panel.select_TOOLTIPS_AFFILIATE()
    panel.select_TOOLTIPS_REGISTRATIONS()
    panel.select_TOOLTIPS_FTD()
    panel.select_TOOLTIPS_CPA()
    #panel.select_TOOLTIP_ACTUALIZATION() ###
    panel.select_PREVIOUS_COMPARISON_EARNINGS() 
    #panel.select_PREVIOUS_COMPARISON_AFFILIATE() ##Tener en cuenta cuando si hay ganancias por afiliado
    panel.select_PREVIOUS_COMPARISON_REGISTRATIONS()
    panel.select_PREVIOUS_COMPARISON_FTD()
    panel.select_PREVIOUS_COMPARISON_CPA()
    #
