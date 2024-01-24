import allure #importar allure para que no falle las imagenes ni el reporte
import pytest
import time

from allure_commons.types import AttachmentType #libreria para porder hacer screenchots automaticos de las pruebas

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


@pytest.fixture(scope='module')
def setup_login_uno():
    global driver, f
    driver = webdriver.Chrome()
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f = Funciones_Globales(driver)
    f.texto_Mixto_validado("id", "Email", "admin@yourstore.com", t)
    f.texto_Mixto_validado("id", "Password", "admin", t)
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
    print("ENTRADA AL SISTEMA A TESTEAR")

@pytest.fixture(scope='module')
def setup_Login_dos():
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



@pytest.mark.usefixtures("setup_login_uno")
def test_uno():
    f = Funciones_Globales(driver)
    print("Entrando el sistema uno")
    f.Click_Mixto("xpath","(//p[contains(.,'Customers')])[1]",t)
    f.Click_Mixto("xpath","(//p[contains(.,'Customers')])[2]",t)
    f.texto_Mixto_validado("xpath","//input[contains(@id,'SearchFirstName')]","victoria",t)
    allure.attach(driver.get_screenshot_as_png(), name="buscando_nombre", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("xpath","//button[contains(@id,'search-customers')]",t)
    allure.attach(driver.get_screenshot_as_png(), name="customers", attachment_type=AttachmentType.PNG)#screenchost para reporte (colocar en el campo nombre el nombre de la imagen para saber cual es)
    #Creando un nuevo usuario
    f.Click_Mixto("xpath","//a[@href='/Admin/Customer/Create']",t)
    email=driver.find_element(By.XPATH,"//input[contains(@id,'Email')]")
    email.send_keys("juan@gmail.com"+Keys.TAB+"12345"+Keys.TAB+"Juan"+Keys.TAB+"Perez")
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="datos", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("xpath","//input[contains(@id,'Gender_Male')]",t)
    f.texto_Mixto_validado("xpath","//input[contains(@id,'DateOfBirth')]","2/20/2019",t)
    allure.attach(driver.get_screenshot_as_png(), name="fecha", attachment_type=AttachmentType.PNG)
    driver.close()



@pytest.mark.usefixtures("setup_Login_dos")
def test_dos():
    #el codigo funciona correctamnte, pero no puedo consegui el xpath , la pagina a testear no me deja correr el xpath o el id
    f = Funciones_Globales(driver)
    print("Entrando el sistema dos")
    time.sleep(1)
    f.Click_Mixto("xpath","//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][contains(.,'Admin')]",t)
    allure.attach(driver.get_screenshot_as_png(), name="administrador", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("xpath","//span[@class='oxd-topbar-body-nav-tab-item'][contains(.,'User Management')]",t)
    f.texto_Mixto_validado("xpath","/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input","Cheeku",t)
    allure.attach(driver.get_screenshot_as_png(), name="escribiendo", attachment_type=AttachmentType.PNG)
    #f.Click_Mixto("xpath", "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]", t)
    #f.Click_Mixto("xpath","//button[@class='oxd-button oxd-button--medium oxd-button--secondary']",t)
    #f.Select_Xpath_Type("(//div[@class='oxd-select-text-input'][contains(.,'-- Select --')])[1]","index",1,t)
    driver.close()
