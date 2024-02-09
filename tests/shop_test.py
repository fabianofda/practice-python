from tests.base_test import BaseTest
from pages.shop_page import ShopPage

class TestShop(BaseTest):

    def test_filtrar_produto_por_preco(self):
        self.visit("/shop")

        self.shop_page = ShopPage(self.driver)

        self.shop_page.filter_by_price()
        
        self.shop_page.highlight_product_prices()

        price_elements = self.shop_page.get_product_prices()
    
        for price_element in price_elements:
            price_text = price_element.text.strip()
            assert price_text == "₹150.00"


    def test_filtrar_produto_por_categoria(self):
        self.visit("/shop")

        self.shop_page = ShopPage(self.driver)
        self.shop_page.filter_by_category()

        self.shop_page.highlight_products_table()

        item_count = len(self.shop_page.get_product_items())
        assert item_count == 3

   


  
    
 
    


