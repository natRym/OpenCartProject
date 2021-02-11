from selenium.webdriver.common.by import By
from src.framework.BasePage import BasePage


class MainPage(BasePage):
    """
    Main Page
    """

    def __init__(self):
        super().__init__(type=By.XPATH, locator='//*[@id="content"]/h3', name='Main Page')

    def top_bar(self):
        super().__init__(type=By.ID, locator='top', name='Top Bar')

    def logo(self):
        super().__init__(type=By.ID, locator='logo', name='Logo')

    def search_field(self):
        super().__init__(type=By.ID, locator='search', name='Search Field')

    def search_button(self):
        super().__init__(type=By.ID, locator='button', name='Search Button')

    def cart_button(self):
        super().__init__(type=By.ID, locator='cart', name='Cart Button')

    def categories_bar(self):
        super().__init__(type=By.CLASS_NAME, locator='nav navbar-nav', name='Categories Bar')

    def promo_block(self):
        super().__init__(type=By.CLASS_NAME, locator='swiper-viewport', name='Promo Block')

    def featured_block(self):
        super().__init__(type=By.CLASS_NAME, locator='row', name='Featured Block')

    def brands_block(self):
        super().__init__(type=By.CLASS_NAME, locator='swiper-viewport', name='Brands Block')

    def footer(self):
        super().__init__(type=By.By.XPATH, locator='//footer', name='Brands Block')