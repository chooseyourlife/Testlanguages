import time
from selenium.webdriver.common.by import By


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_link_have_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    buttons = browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert len(buttons) > 0, "Button not found"
    assert buttons[0].is_displayed(), "Button is not visible"


