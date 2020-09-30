from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()

    def should_add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), \
            "basket link is not present"

    def should_be_price_of_product_equal_to_price_in_basket(self):
        productPriceInBasket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        productPrice = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert  productPriceInBasket == productPrice, "Price of book are not equal to basket price"

    def should_be_name_about_product_in_basket_equal_to_product_name(self):
        productName = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        productNameInBasket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE_ADD_TO_BASKET).text
        assert productName == productNameInBasket, "Name of product isn`t the same as product name in basket"
