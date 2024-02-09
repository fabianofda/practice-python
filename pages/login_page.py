from selenium.webdriver.common.by import By
from tests.base_test import BaseTest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
import time

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.BASE_URL = BaseTest.BASE_URL

        # Elementos da página
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.email_input = (By.CSS_SELECTOR, "#reg_email")
        self.reg_password_input = (By.CSS_SELECTOR, "#reg_password")

        self.login_button = (By.NAME, "login")
        self.login_register = (By.CSS_SELECTOR, "input[value='Register']")
        self.alert_message = (By.XPATH, "//li[contains(., 'Error: The password you entered for the username')]")

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def get_alert_message(self):
        return self.driver.find_element(*self.alert_message).text if self.is_alert_message_displayed() else None
    
    def visit_my_account(self, rota):
        self.driver.get(self.BASE_URL + rota)

    def register(self, email, password):
        self.enter_email_input(email)
        self.enter_reg_password_input(password)
        self.click_login_register()

    def enter_email_input(self, email):
        email_input = self.driver.find_element(*self.email_input)
        self.type_slowly(email_input, email)

    def enter_reg_password_input(self, password):
        password_input = self.driver.find_element(*self.reg_password_input)
        self.type_slowly(password_input, password)

    def click_login_register(self):
        wait = WebDriverWait(self.driver, 10)
        self.login_register_element = wait.until(EC.visibility_of_element_located(self.login_register))
        self.login_register_element.click()

    def type_slowly(self, element, text):
        for char in text:
            element.send_keys(char)
            time.sleep(0.1)

    def is_alert_message_displayed(self):
            return self.driver.find_elements(*self.alert_message)

    def highlight_alert_message_displayed(self):
            alert_message_element = self.driver.find_element(*self.alert_message)
            self.driver.execute_script("arguments[0].style.border='3px solid red'", alert_message_element)   