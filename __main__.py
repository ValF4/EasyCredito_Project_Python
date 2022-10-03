from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

URL = 'https://pt.aliexpress.com'


class Product:
    name = ''
    price = 0.0
    priceIsValid = False


def searchProduct(driver, product_text):
    driver.find_element('xpath', '//*[@id="search-key"]').send_keys(product_text)
    driver.find_element('xpath', '//*[@id="form-searchbar"]/div[1]/input').click()
    last_height = driver.execute_script("return document.body.scrollHeight")

    for rolled in range(10):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break

        last_height = new_height


def getProductsInPage(driver):
    browser = BeautifulSoup(driver.page_source, 'html.parser')
    listProducts = []
    elements = browser.find('div', attrs={'class': 'JIIxO'}).findAll('a', attrs={'class': '_3t7zg _2f4Ho'})
    sleep(3)

    
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