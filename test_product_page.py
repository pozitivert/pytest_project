import time
import pytest
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import string
import secrets

# def test_guest_can_add_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = BasketPage(browser, link)
#     page.open()
#     # page.should_be_empty_basket()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.product_added()
#     # time.sleep(600)

# @pytest.mark.parametrize('link', [pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1", marks=pytest.mark.skip),
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2", marks=pytest.mark.skip),
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3", marks=pytest.mark.skip),
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4", marks=pytest.mark.skip),
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5", marks=pytest.mark.skip),
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6", marks=pytest.mark.skip),
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.skip),
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8", marks=pytest.mark.skip),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
# def test_guest_can_add_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/"
#     page = ProductPage(browser, link)
#     page.open()
#     time.sleep(2)
#     page.add_to_basket()
#     time.sleep(6000)
#
#
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = BasketPage(browser, link)
#     page.open()
#     time.sleep(2)
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.product_added()
#     page.should_not_be_success_message()
#
#
# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = BasketPage(browser, link)
#     page.open()
#     time.sleep(2)
#     page.should_not_be_success_message()
#
#
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = BasketPage(browser, link)
#     page.open()
#     time.sleep(2)
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.product_added()
#     page.success_message_should_disappear()


# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = BasketPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#
#
# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = BasketPage(browser, link)
#     page.open()
#     page.go_to_login_page()


# def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = BasketPage(browser, link)
#     page.open()
#     page.go_to_basket()
#     page.should_be_empty_basket()
#     page.check_should_be_empty_basket_message()
#
#
# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/"
#     page = BasketPage(browser, link)
#     page.open()
#     page.go_to_basket()
#     page.should_be_empty_basket()
#     page.check_should_be_empty_basket_message()


@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        _characters = string.ascii_letters + string.digits + string.punctuation
        email = str(time.time()) + "@fakemail.org"
        password = ''.join(secrets.choice(_characters) for _ in range(10))
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        time.sleep(5)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        time.sleep(2)
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = BasketPage(browser, link)
        page.open()
        time.sleep(2)
        page.add_to_basket()
        page.product_added()