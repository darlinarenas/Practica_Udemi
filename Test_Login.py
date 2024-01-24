import pytest# NO IMPORTAMOS UNITEST  SOLO IMPORTAMOS LA LIBRERIA PYTEST POR QUE ES CON LA QUE TRABAJAREMOS
import time
import allure_pytest

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
t=.1

def test_login1(): # OJO falta buscar el error del driver, solo corre la primera funcion, las demas da errer de driver
    driver = webdriver.Chrome()
    FL=Funciones_Login(driver)
    FL.L1("Darlin699@gmail.com","12332145","No customer account found",t) #AQUI ACORTAMOS Y HICIMOS UNA PAGINA PARA HACER SOLO EL LLAMADO DE LAS FUNCIONES PARA ACORTAR EL CODIGO (COPIAR U PEGAR EL MENSAJE DE ERROR PARA HACER LAS VALIDACIONES )
    #FL.L2("","12332145","Please enter your email",t)
    #FL.L3("admin@yourstore.com","admin","Dashboard",t)


#   AQUI LA ESTRUCTURA ANTERIOR PARA HACER LAS PRUEBAS,
"""
    f=Funciones_Globales(driver)
    f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F",t)
    f.texto_Mixto_validado("id","Email","darlin699@gmail.com",t)
    f.texto_Mixto_validado("id","Password","1234",t)
    f.Click_Mixto("xpath","//button[@type='submit'][contains(.,'Log in')]",t)
    e1=f.SEX("//li[contains(.,'No customer account found')]") #AQUI PREGUNTAMOS  QUE TIENE EL XPATH PARA VALIDARLO (VALIDACION SI EL LOGIN O LA CONTRASEÑA SON INCORRECTAS)
    e1=e1.text #AQUI CONVERTIMOS EL  DATO EN UN TEXTO PARA IMPRIMIR
    print(e1)
    if(e1=="No customer account found"):
        print("PRUEBA DE VALIDACION  OK")
    else:
        print("FALLO PRUEBA DE VALIDACION")

    driver.close()

def test_login2():
    driver = webdriver.Chrome()
    f=Funciones_Globales(driver)
    f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F",t)
    f.texto_Mixto_validado("id","Email","",t)
    f.texto_Mixto_validado("id","Password","123gg4t3t4",t)
    f.Click_Mixto("xpath","//button[@type='submit'][contains(.,'Log in')]",t)
    e1=f.SEX("//span[contains(@id,'Email-error')]") #AQUI PREGUNTAMOS  QUE TIENE EL XPATH PARA VALIDARLO (VALIDACION SI EL LOGIN O LA CONTRASEÑA SON INCORRECTAS)
    e1=e1.text #AQUI CONVERTIMOS EL  DATO EN UN TEXTO PARA IMPRIMIR
    print(e1)
    if(e1=="Please enter your email"):
        print("PRUEBA DE EMAIL VACIA  OK")
    else:
        print("FALLO PRUEBA DE VALIDACION EMAIL VACIA")
        driver.close()

    driver.close()

def test_login3():
    driver = webdriver.Chrome()
    f=Funciones_Globales(driver)
    f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F",t)
    f.texto_Mixto_validado("id","Email","gfbdbdb",t)
    f.texto_Mixto_validado("id","Password","123gg4t3t4",t)
    f.Click_Mixto("xpath","//button[@type='submit'][contains(.,'Log in')]",t)
    e1=f.SEX("//span[contains(@id,'Email-error')]") #AQUI PREGUNTAMOS  QUE TIENE EL XPATH PARA VALIDARLO (VALIDACION SI EL LOGIN O LA CONTRASEÑA SON INCORRECTAS)
    e1=e1.text #AQUI CONVERTIMOS EL  DATO EN UN TEXTO PARA IMPRIMIR
    print(e1)

    if(e1=="Wrong email"):
        print("PRUEBA DE EMAIL INCORRECTO  OK")
    else:
        print("FALLO PRUEBA DE VALIDACION EMAIL INCORRECTO")
        driver.close()


    driver.close()

def test_login4():
    driver = webdriver.Chrome()
    f=Funciones_Globales(driver)
    f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F",t)
    f.texto_Mixto_validado("id","Email","admin@yourstore.com",t)
    f.texto_Mixto_validado("id","Password","admin",t)
    f.Click_Mixto("xpath","//button[@type='submit'][contains(.,'Log in')]",t)
    e1=f.SEX("//h1[contains(.,'Dashboard')]") #AQUI PREGUNTAMOS  QUE TIENE EL XPATH PARA VALIDARLO (VALIDACION SI EL LOGIN O LA CONTRASEÑA SON INCORRECTAS)
    e1=e1.text #AQUI CONVERTIMOS EL  DATO EN UN TEXTO PARA IMPRIMIR
    print(e1)

    if (e1 == "Dashboard"):
        print("PRUEBA LOGIN  OK")
    else:
        print("PRUEBA LOGIN FALLO")
        driver.close()

    driver.close()
"""

