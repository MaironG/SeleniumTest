from lib2to3.pgen2 import driver
from select import select
from socket import if_nameindex
from turtle import down
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class usando_unittest(unittest.TestCase):
    # se ejecuta siempre de primero
    def setUp(self):
        print("Este es el setUp")
        self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")

    # test
    # buecar articulo en amazon, elejir el segundo de la lista y añadirlo al caro
    def test_buscar(self):
        print("Este es el test_buscar")
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.amazon.com/")
        self.assertIn("Amazon.com", driver.title, msg="no estas en la pagina correcto")
        elemento = driver.find_element_by_id("twotabsearchtextbox")
        elemento.send_keys("PC")  # introduce aqui la palabra a buscar
        elemento.send_keys(Keys.ENTER)
        elemento = driver.find_element_by_css_selector(
            "div[class='s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_2'] span[class='a-size-medium a-color-base a-text-normal']"
        )
        elemento.click()

        try:
            if driver.find_element_by_css_selector(
                "#a-autoid-0-announce"
            ).is_enabled:  # evaluando si el boton de cantidad esta habilitado
                elemento = driver.find_element_by_css_selector("#a-autoid-0-announce")
                elemento.click()
                elemento = driver.find_element_by_css_selector("#quantity_1")
                elemento.send_keys(Keys.ARROW_DOWN)  # seleccionamos 2
                driver.implicitly_wait(1)
                elemento.click()
                elemento = driver.find_element_by_xpath(
                    "//input[@id='add-to-cart-button']"
                )
                elemento.click()
                time.sleep(10)
                return

        except:
            print("Este producto solo tiene uno en existencia")
            elemento = driver.find_element_by_xpath("//input[@id='add-to-cart-button']")
            elemento.click()
            time.sleep(3)

    # siempre se ejecuta de ultimo
    def tearDown(self):
        print("Este es el tearDown")
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
