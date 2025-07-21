import time
import pytest
from selenium.webdriver.common.by import By


def test_add_to_basket_button_exists(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    time.sleep(30)  # для визуальной проверки текста кнопки при запуске с разными языками

    # Ищем кнопку добавления в корзину
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")

    # Проверяем, что кнопка отображается
    assert add_to_basket_button.is_displayed(), "Add to basket button is not displayed"
