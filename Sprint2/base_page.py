from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
 
    def go_to_page(self, url):
        self.driver.get(url)
 
    def wait_for_element(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    
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
            
    def type_text(self,locator,text):   
        element=self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def type_text2(self,locator,text):   
        element=self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)      


