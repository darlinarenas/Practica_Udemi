import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones import Funciones_Globales
from Page_Login import Funciones_Login
from selenium.webdriver import ActionChains
t=1
t=1
driver="" #declaramos la variabla para ponerla en cero y poder utilizarlas en todos lados
f=""


@pytest.fixture(scope='module')
def setup_Login():
    global driver, f
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f = Funciones_Globales(driver)
    f.texto_Mixto_validado("xpath", "//input[contains(@name,'username')]", "Admin", t)
    f.texto_Mixto_validado("xpath", "//input[contains(@type,'password')]", "admin123", t)
    f.Click_Mixto("xpath", "//button[contains(@type,'submit')]", t)
    print("ENTRADA AL SISTEMA A TESTEAR")

def teardown_function():
    print("FIN DE LOS TEST")
    driver.close()



@pytest.mark.usefixtures("setup_Login")
def test_uno():
    f = Funciones_Globales(driver)
    etiqueta=f.SEX("//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module'][contains(.,'Dashboard')]").text
    print(etiqueta)
    time.sleep(2)
    if (etiqueta=="Dashboard"):
        print("ENTRAMOS AL SISTEMA")
        assert etiqueta=="Dashboard"


    else:
        print("NO ENTRAMOS AL SISTEMA")
        assert etiqueta == "Dashboard"








