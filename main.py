# Bibliotecas Importadas
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import db_connect

# Variaveis Globais
product_text = 'redmi'
URL_Main = 'https://pt.aliexpress.com'

#Classe de produtos
class Product:
    name = ''
    price = 0.0
    url = ''

# Função Main(Principal)
def main():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(URL_Main)
    search(browser, product_text)
    scroll_down(browser)
    listProducts = getItensInPage(browser)
    db_connect.insert_products(listProducts)
    select_list = db_connect.execute_query_select('SELECT name, price, url from public.products  order by price limit 5')
    
def search(driver, item):
    driver.find_element('xpath', '//*[@id="search-key"]').send_keys(item)
    driver.find_element('xpath', '//*[@id="form-searchbar"]/div[1]/input').click()

# Função de descida da pagiona
def scroll_down(driver):
    for roll in range(6):
        driver.execute_script('window.scrollTo(0, {});'.format(roll*1080))
''
# Raspando as informações
def getItensInPage(driver):
    listProducts = []
    page = BeautifulSoup(driver.page_source, 'html.parser')
    elements = page.find('div', attrs={'class': 'JIIxO'}).find_all('a', attrs={'class': '_3t7zg _2f4Ho'})

    for element in elements:
        price= ''        
        price_products = element.find('div', attrs={'class': 'mGXnE _37W_B'}).find_all('span')
        
        for name in price_products: ## Extraindo preço
            price = price + name.getText()

        product = Product() ## Extraindo Nome
        product.name = element.find('h1').getText()
        product.url = element.attrs['href'].replace('//', 'https://') ## Extraindo as URLS

        if len(price) > 3: ## Validação do valor para enviar para o banco de dados
            product.price = float(price.replace('R$', '').replace('.', '').replace(',', '.'))
            product.priceIsValid = True

        listProducts.append(product)
 
    return listProducts

# Executar codigo via terminal
if __name__ == "__main__":
    main()