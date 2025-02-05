from selenium.webdriver.common.by import By

from pages.product import ProductPage


class HomePage:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://demoblaze.com/index.html')

    def click_galaxy_s6(self) -> 'ProductPage':
        galaxy_s6 = self.browser.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
        galaxy_s6.click()
        return ProductPage(self.browser)
