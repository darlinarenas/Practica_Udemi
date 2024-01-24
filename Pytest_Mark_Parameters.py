import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Maquina_uno.MV1.PYTEST.Funciones import Funciones_Globales
from Page_Login import Funciones_Login
from selenium.webdriver import ActionChains
t=1
driver="" #declaramos la variabla para ponerla en cero y poder utilizarlas en todos lados
f=""

def get_Data():
    return [
        ("rodrigo","1234"),
        ("juan", "1233234"),
        ("pedro", "12232334"),
        ("erika", "1234232"),
        ("carlos", "1234sdf"),
        ("Admin", "admin123")
    ]

@pytest.mark.parametrize("user,clave",get_Data())
def test_login(user,clave):
    global driver, f
    driver = webdriver.Chrome()
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f = Funciones_Globales(driver)
    f.texto_Mixto_validado("id", "Email", user, t)
    f.texto_Mixto_validado("id", "Password", clave, t)
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
    print("ENTRADA AL SISTEMA A TESTEAR")


def teardown_function():
    print("::..SALIDA DEL TEST..::")
    driver.close()

