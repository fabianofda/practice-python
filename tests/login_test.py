from tests.base_test import BaseTest
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage

class TestLogin(BaseTest):

    def test_fazer_login_com_sucesso(self):
        self.visit("/my-account")

        login_page = LoginPage(self.driver)
        my_account_page = MyAccountPage(self.driver)

        login_page.login(self.email, self.password)

        my_account_page.highlight_paragraph_text()

        assert "Hello teste12341 (not teste12341? Sign out)" == my_account_page.get_paragraph_text()
        
    
    def test_tentativa_de_login_sem_sucesso(self):
        self.visit("/my-account")
        login_page = LoginPage(self.driver)
        login_page.login(self.email_inv, self.pass_invalido)

        login_page.highlight_alert_message_displayed()

        assert login_page.is_alert_message_displayed()
        assert "Error: The password you entered for the username teste@teste.com is incorrect. Lost your password?" == login_page.get_alert_message()


    def test_realizar_registro_com_sucesso(self):
        self.visit("/my-account")

        login_page = LoginPage(self.driver)
        my_account_page = MyAccountPage(self.driver)

        login_page.register(self.reg_mail, self.reg_pass)

        my_account_page.highlight_logout_link_present()
        
        assert my_account_page.is_logout_link_present()

        
