from selenium.webdriver.common.by import By

class MyAccountPage:
    def __init__(self, driver):
        self.driver = driver

        # Elementos da página
        self.paragraph = (By.TAG_NAME, "p")
        self.link_logout = (By.XPATH, "//a[text()='Logout']")

    def get_paragraph_text(self):
        return self.driver.find_element(*self.paragraph).text
    
    def highlight_paragraph_text(self):
        paragraph_text_element = self.driver.find_element(*self.paragraph)
        self.driver.execute_script("arguments[0].style.border='3px solid red'", paragraph_text_element)  
    
    def click_login_register(self):
        self.driver.find_element(*self.link_logout)
     
    def is_logout_link_present(self):
        return bool(self.driver.find_elements(*self.link_logout))
    
    def highlight_logout_link_present(self):
        if self.is_logout_link_present():
            logout_link_element = self.driver.find_element(*self.link_logout)
            self.driver.execute_script("arguments[0].style.border='3px solid red'", logout_link_element)     
