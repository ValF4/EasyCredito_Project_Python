from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


URL_Main = 'https://pt.aliexpress.com'


class Product:
    name = ''
    price = 0.0
    Url = ''


def searchProduct(driver, product_text):
    driver.find_element('xpath', '//*[@id="search-key"]').send_keys(product_text)
    driver.find_element('xpath', '//*[@id="form-searchbar"]/div[1]/input').click()
    
    for roll in range(5):
        driver.execute_script('window.scrollTo(0, {});'.format(roll*1000))


def getItensInPage(driver):
    page = BeautifulSoup(driver.page_source, 'html.parser')
    listProducts = []
    price = ''
    elements = page.find('div', attrs={'class': 'JIIxO'}).find_all('a', attrs={'class': '_3t7zg _2f4Ho'})

    for element in elements:
        spans = element.find('div', attrs={'class': 'mGXnE _37W_B'}).find_all('span')
        
        for span in spans: ## Extraindo preço
            price = price + span.getText()

        product = Product() ## Extraindo Nome
        product.name = element.find('h1').getText()
        listProducts.append(product.name)

        product.Url = element.find('div', attrs={'class': '_3t7zg _2f4Ho'}).find.all('href')
        print(product.Url)

        product.name = element.find()

        if len(price) > 3:
            product.price = float(price.replace('R$', '').replace('.', '').replace(',', '.'))

        listProducts.append(product)
 
    return listProducts


def main():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(URL_Main)
    searchProduct(browser, 'redmi')
    listProducts = getItensInPage(browser)


if __name__ == "__main__":
    main()