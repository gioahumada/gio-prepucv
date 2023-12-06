from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

url = "https://www.adidas.cl/campus-00s-w/GY0042.html"

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--disable-extensions")
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get(url)

try:
    buy_zone = driver.find_element_by_id("add-to-bag")
    print("El id 'add-to-bag' está presente en la página.")
except NoSuchElementException:
    print("El id 'add-to-bag' no está presente en la página.")

driver.quit()
