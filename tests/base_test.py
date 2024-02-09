import os
import logging
import time
from selenium import webdriver
from dotenv import load_dotenv
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BaseTest:
    BASE_URL = "https://practice.automationtesting.in"
    
    def visit(self, rota):
        self.driver.get(self.BASE_URL + rota)

    def setup_method(self):
        logging.basicConfig(level=logging.INFO)

        load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")
        self.email_inv = os.getenv("EMAIL_INV")
        self.pass_invalido = os.getenv("PASS_INVALIDO")
        self.reg_pass = os.getenv("REG_PASS")
        self.reg_mail = Faker().email()  # Você pode criar o email diretamente aqui

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(30)
        self.driver.set_window_size(1340, 1024)

    def wait_until_page_loaded(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.ID, "footer")))
    

    def screenshot(self, test_name):
        suite_name = self.get_suite_name()
        screenshots_dir = os.path.join("screenshots", f"{suite_name}_test")
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        self.wait_until_page_loaded()
        
        full_page_screenshot_filename = os.path.join(screenshots_dir, f"{test_name}.png")
        self.driver.execute_script("document.body.style.overflow = 'hidden';")
        self.driver.save_screenshot(full_page_screenshot_filename)
        self.driver.execute_script("document.body.style.overflow = 'auto';")

    def get_suite_name(self):
        return type(self).__name__.replace("Test", "").lower()
    
    def teardown_method(self, method):
        test_name = method.__name__
        self.screenshot(test_name)
        time.sleep(2)
        self.driver.quit()

    def highlight_element(self, element):
        # Adicione uma borda ao elemento para destacá-lo
        self.driver.execute_script("arguments[0].style.border='3px solid red'", element)

    def remove_highlight(self, element):
        # Remova a borda após destacar o elemento
        self.driver.execute_script("arguments[0].style.border=''", element)
