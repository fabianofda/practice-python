from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from tests.base_test import BaseTest

class ShopPage:
    def __init__(self, driver):
        self.driver = driver

        self.BASE_URL = BaseTest.BASE_URL

        # Elementos da página
        self.product_items = (By.CSS_SELECTOR, ".products li")
        self.slider = (By.XPATH, "(//*[@class='ui-slider-handle ui-corner-all ui-state-default'])[2]")
        self.price_filter_button = (By.XPATH, "//*[@id='woocommerce_price_filter-2']/form/div/div[2]/button")
        self.category_link = (By.CSS_SELECTOR, ".product-categories li.cat-item-21 a")
        self.products_table = (By.CSS_SELECTOR, "ul.products")
        self.product_prices = (By.CSS_SELECTOR, ".price .woocommerce-Price-amount")

    def get_products_table(self):
        return self.driver.find_element(*self.products_table)
    
    def highlight_products_table(self):
        products_table_element = self.get_products_table()
        self.driver.execute_script("arguments[0].style.border='3px solid red'", products_table_element)
    
    def get_product_prices(self):
        price_elements = self.driver.find_elements(*self.product_prices)
        return price_elements
    
    def highlight_product_prices(self):
        price_elements = self.driver.find_elements(*self.product_prices)

        for price_element in price_elements:
            # self.scroll_to_element(price_element)
            self.driver.execute_script("arguments[0].style.border='3px solid red'", price_element)
    
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    def get_product_items(self):
        return self.driver.find_elements(*self.product_items)

    def filter_by_price(self):
        self._drag_slider()
        self.driver.find_element(*self.price_filter_button).click()

    def filter_by_category(self):
        self.driver.find_element(*self.category_link).click()

    def _drag_slider(self):
        slider = self.driver.find_element(*self.slider)
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(slider, -200, 0).perform()

    def highlight_slider(self):
        slider_wrapper_element = self.driver.find_element(By.CLASS_NAME, "price_slider_wrapper")
        self.driver.execute_script("arguments[0].style.border='3px solid red'", slider_wrapper_element)
