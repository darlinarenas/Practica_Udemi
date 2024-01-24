import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from Maquina_uno.MV1.PYTEST.Funciones import Funciones_Globales



class Funciones_Login():

    def __init__(self,driver):
        self.driver=driver
        self.f = Funciones_Globales(driver)
        self.f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F",1)
        self.driver.maximize_window()

    def L1(self,email,clave,message, t):
        self.f.texto_Mixto_validado("id", "Email", email, t)
        self.f.texto_Mixto_validado("id", "Password", clave, t)
        self.f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
        e1 = self.f.SEX("//li[contains(.,'No customer account found')]")
        e1 = e1.text
        print(str(e1))
        if (e1 == message):
            print("El Error es Correcto")
            self.driver.close()
        else:
            print("No esta bien el error")
            self.driver.close()





    def L2(self,email,clave,message,t):
        self.f.texto_Mixto_validado("id", "Email", email, t)
        self.f.texto_Mixto_validado("id", "Password", clave, t)
        self.f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
        e1 = self.f.SEX("//span[contains(@id,'Email-error')]")
        e1 = e1.text
        print(e1)
        if (e1 == message):
            print("Email no valido prueba Exitosa")
            self.driver.close()
        else:
            print("Prueba de Email no Exitosa")
            self.driver.close()


    def L3(self,email,clave,message,t):
        self.f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)
        self.f.texto_Mixto_validado("id", "Email", email, t)
        self.f.texto_Mixto_validado("id", "Password", clave, t)
        self.f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
        e1 = self.f.SEX("//h1[contains(.,'Dashboard')]")
        e1 = e1.text
        print(e1)
        if (e1 == message):
            print("Login Exitoso")
            self.driver.close()
        else:
            print("Prueba no exitosa")
            self.driver.close()
