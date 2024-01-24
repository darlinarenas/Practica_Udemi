import pytest   # NO IMPORTAMOS UNITEST  SOLO IMPORTAMOS LA LIBRERIA PYTEST POR QUE ES CON LA QUE TRABAJAREMOS
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Maquina_uno.MV1.PYTEST.Funciones import Funciones_Globales
from selenium.webdriver import ActionChains
from Page_Login import Funciones_Login
t=1
drive="" #declaramos la variabla para ponerla en cero y poder utilizarlas en todos lados
f=""


def setup_function(function):
    global driver,f #colocamos la variable aqui para utilizarlas en todos lados
    driver = webdriver.Chrome()
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    driver.maximize_window()
    print("..:: INICIANDO  TEST ::..")
    f = Funciones_Globales(driver)
    f.texto_Mixto_validado("id", "Email", "admin@yourstore.com", t)
    f.texto_Mixto_validado("id", "Password", "admin", t)
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)

def teardown_function(function):
    print("FIN DEL LOS TEST")
    driver.close()

def test_uno():
    f = Funciones_Globales(driver)
    f.Click_Mixto("xpath","(//p[contains(.,'Catalog')])[1]",t)
    f.Click_Mixto("xpath","(//p[contains(.,'Products')])[1]",t)
    f.texto_Mixto_validado("id","SearchProductName","lenovo",t)
    f.Click_Mixto("id","search-products",t)

def test_dos():
    f = Funciones_Globales(driver)
    f.Click_Mixto("xpath", "(//p[contains(.,'Catalog')])[1]", t)
    f.Click_Mixto("xpath", "(//p[contains(.,'Products')])[1]", t)
    f.Click_Mixto("xpath","//a[@href='/Admin/Product/Create']",t)
    f.texto_Mixto_validado("id","Name","dell pc nuevo",t)
    f.texto_Mixto_validado("id","ShortDescription","producto nuevo agregado al sistema",t)
    f.Click_Mixto("xpath","//span[@class='tox-mbtn__select-label'][contains(.,'File')]",t)
    f.Click_Mixto("xpath","//div[@class='tox-collection__item-label'][contains(.,'New document')]",t)
    driver.switch_to.frame(0) #EN ESTA LINEA LOCALIZAMOS EL IFRAME (CUANDO NO PODEMOS ESCRIBIR EN EL CAMPO SEECCIONADO )
    #f.texto_Mixto_validado("id","tinymce","full descripcion por id de frame",t) #ESTA LINEA SI FUNCIONA
    campo=driver.find_element(By.ID,"tinymce") #COMO NI ENCONTRAMOS EL CAMPO QUE SIGUE, UBICAMOS PARA HACER UN SEND_KEYS Y TABULADOR PARA BAJAR A LA SIGUIENTE LINEA
    campo.send_keys("descripcion larga"+Keys.TAB+ "343124")#AQJUI ESCRIBIMOS EN LA LINEA ANTERIOR EN EL FORMULARIO Y TABULADOR PARA ESCRIBIR EN EL CAMPO SIGUINTE
    















