import time
from selenium.webdriver.common.by import By


def test_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(20)
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button, "Error! No add to basket button!"
