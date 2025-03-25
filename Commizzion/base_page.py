from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains 
from selenium.webdriver.support.wait import WebDriverWait

import pyautogui

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
 
    def go_to_page(self, url):
        self.driver.get(url)
 
    def wait_for_element(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    ##def wait_for_element(self, locator, timeout=10):
        ##return WebDriverWait(self.driver, timeout).until(
            ##lambda driver: driver.find_element(*locator))

    # elementos adicionales

    def click(self, locator):
        self.wait_for_element(locator).click()  #Para dar click

    def type_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text) #Para ingrear textos

    def select_dropdown_by_visible_text(self, locator, text): #desplegable del codigo de telefono
        dropdowm = Select(self.wait_for_element(locator))
        dropdowm.select_by_visible_text(text)

    #def select_dropdown_by_index(self, locator, index): #desplegable del codigo de telefono
        #dropdowm = Select(self.wait_for_element(locator))
        #dropdowm.select_by_index(index)   

    def select_checkbox(self, locator):
        checkbox = self.wait_for_element(locator)
        if not checkbox.is_selected():
            checkbox.click()   #Para seleccionar los TYC Y EL RECATCHA

    def click_scroll(self, locator):
        element = self.wait_for_element(locator)
        element.click()
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_scroll2(self, locator):
        self.wait_for_element(locator).click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
       
    def click_close_popup(self, locator):
        self.wait_for_element(locator).click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        pyautogui.press('alt+f4')

    def click_scroll2(self, locator):
        self.wait_for_element(locator).click()
        self.driver.execute_script("window.scrollTo(0,1550)")

    def move_to_and_click(self, by_locator):
        """ Mueve el cursor al elemento y hace clic en él """
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(by_locator)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()  # Moverse al elemento
        element.click()

