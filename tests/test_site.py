from pages.homepage import HomePage


def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    product_page = homepage.click_galaxy_s6()
    product_page.check_title_is('Samsung galaxy s6')
