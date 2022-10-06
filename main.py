# Bibliotecas Importadas
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Variaveis Globais
product_text = 'redmi'
URL_Main = 'https://pt.aliexpress.com'

#Classe de produtos
class Product:
    name = ''
    price = 0.0
    priceIsValid = False

# Função Main(Principal)
def main():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(URL_Main)
    browser.find_element('xpath', '//*[@id="search-key"]').send_keys(product_text)
    browser.find_element('xpath', '//*[@id="form-searchbar"]/div[1]/input').click()
    scroll_down(browser)
    listProducts = getItensInPage(browser)

# Função de descida da pagiona
def scroll_down(driver):
    for roll in range(5):
        driver.execute_script('window.scrollTo(0, {});'.format(roll*1000))

# Raspando as informações
def getItensInPage(driver):
    listProducts = []
    price= ''
    page = BeautifulSoup(driver.page_source, 'html.parser')
    elements = page.find('div', attrs={'class': 'JIIxO'}).find_all('a', attrs={'class': '_3t7zg _2f4Ho'})

    for element in elements:
        
        price_products = element.find('div', attrs={'class': 'mGXnE _37W_B'}).find_all('span')
        
        for name in price_products: ## Extraindo preço
            price = price + name.getText()

        product = Product() ## Extraindo Nome
        product.name = element.find('h1').getText()

        if len(price_products) > 3:
            product.price = float(price.replace('R$', '').replace('.', '').replace(',', '.'))
            product.priceIsValid = True

        listProducts.append(product.price)
        listProducts.append(product.name)
 
    return listProducts

# Executar codigo via terminal
if __name__ == "__main__":
    main()