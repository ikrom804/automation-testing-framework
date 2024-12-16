from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_field = "username"  # Замените на реальный селектор
        self.password_field = "password"  # Замените на реальный селектор
        self.login_button = "login"      # Замените на реальный селектор

    def login(self, username, password):
        self.driver.find_element("id", self.username_field).send_keys(username)
        self.driver.find_element("id", self.password_field).send_keys(password)
        self.driver.find_element("id", self.login_button).click()
