from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

URL = 'https://pt.aliexpress.com'


class Product:
    name = ''
    price = 0.0
    priceIsValid = False


def searchProduct(driver, product_text):
    driver.find_element('xpath', '//*[@id="search-key"]').send_keys(product_text)
    driver.find_element('xpath', '//*[@id="form-searchbar"]/div[1]/input').click()


def getProductsInPage(driver):
    browser = BeautifulSoup(driver.page_source, 'html.parser')
    listProducts = []
    elements = browser.find('div', attrs={'class': 'JIIxO'}).findAll('a', attrs={'class': '_3t7zg _2f4Ho'})

    for element in elements:
        spans = element.find('div', attrs={'class': 'mGXnE _37W_B'}).findAll('span')
        price = ''

        for span in spans:
            price = price + span.getText()

        product = Product()
        product.name = element.find('h1').getText()

        # Efetuei a validação, me fale o porque =)
        if len(price) > 3:
            product.price = float(price.replace('R$', '').replace('.', '').replace(',', '.'))
            product.priceIsValid = True

        listProducts.append(product)

    return listProducts


def main():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(URL)
    searchProduct(browser, 'redmi')
    listProducts = getProductsInPage(browser)
    # TODO: Salvar os elementos no banco de dados


if __name__ == "__main__":
    main()