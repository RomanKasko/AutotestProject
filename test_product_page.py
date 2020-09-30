from .pages.product_page import ProductPage, ProductPageLocators

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    page.is_element_present(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET_MESSAGE)
    page.should_be_price_of_product_equal_to_price_in_basket()
    page.should_be_name_about_product_in_basket_equal_to_product_name()
    page.should_add_product_to_basket()
