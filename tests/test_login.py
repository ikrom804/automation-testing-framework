from pages.login_page import LoginPage

def test_valid_login(browser):
    login_page = LoginPage(browser)
    login_page.open("https://example.com/login")  # Замените на реальный URL
    login_page.login("valid_user", "valid_password")
    assert "Dashboard" in browser.title  # Проверьте реальное условие
