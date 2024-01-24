import pytest
import time
import tracemalloc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import tracemalloc
tracemalloc.start()
import unittest
import warnings

class Funciones_Globales():
    def __init__():
        self.driver=driver


    def __init__(self, driver):
        self.driver = driver

    def saludos(self):
        print("Bienvenidos a Page Objet Model")

    def saludos2(self):
        print("ESTE ES EL SALUDO DOS")

    def Tiempo(self, Tiem):
        time.sleep(Tiem)
        return Tiem
#LINEA PARA BUSCAR PAGINA A TESTEAR
    def Navegar(self,Url,Tiem):
        self.driver.get(Url)
        self.driver.maximize_window()
        t = time.sleep(Tiem)
        return Tiem
# ESCRIBIENDO TEXTO POR XPATH SIN VALIDAR (TEXTO SENCILLO)
    def Texto_xpath(self,xpath,texto,Tiem):
        valor=self.driver.find_element(By.XPATH,xpath)
        valor.send_keys(texto)
        time.sleep(Tiem)
        return Tiem

# BLOQUE DE FINCIONES PARA VALIDACION DE EXPATH ("SEX" Seccion Expath, "SEXS"    "SEI" seccion ID  )
    def SEX(self,elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.XPATH,elemento)
        return val

    def SEXS(self,elemento):
        val = WebDriverWait(self.driver, 5).until(EC.element_located_to_be_selected((By.XPATH, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.XPATH,elemento)
        return val

    def SEI(self,elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.ID,elemento)
        return val
# BLOQUE DE FINCIONES PARA VALIDACION DE EXPATH ("SEX" Seccion Expath, "SEXS"    "SEI" )


# ESCRIBIENDO TEXTO POR XPATH VALIDADO ( CAMBIANDO LA VARIABLE XPATH POR ID Y EL ELEMENTO DE BUSQUEDA  FUNCIONA DE LA MISMA MANERA )
    def Texto_xpath_validado(self,xpath,texto,Tiem):
        try:
           valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,xpath)))
           valor=self.driver.find_element(By.XPATH,xpath)
           valor.send_keys(texto)
           time.sleep(Tiem)
           return Tiem
        except TimeoutException as ex:
           print(ex.msg)
           print("EL ELEMENTO diasSelect NO  ESTA DISPONIBLE" + xpath)
#FUNCION CLICK POR MIXTO ( CAMBIANDO LA VARIABLE XPATH POR ID Y EL ELEMENTO DE BUSQUEDA  FUNCIONA DE LA MISMA MANERA )
    def Click_Mixto(self, tipo, selector, tiempo):
        if (tipo == "xpath"):
            try:
                val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.XPATH,selector)
                val.click()
                print(tipo)
                print("dando click en {} -> {} ".format(selector, selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.ID,selector)
                val.click()
                print(tipo)
                print("dando click en {} -> {} ".format(selector, selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t

#AQUI HACEMOS FUNCION SELECT (IMPORTA LA LIBRERIA from selenium.webdriver.support.ui import Select)
    def Select_Xpath_Texto (self, xpath,texto,Tiem):
        try:
           valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,xpath)))
           valor=self.driver.find_element(By.XPATH,xpath)
           valor=Select(valor)
           valor.select_by_visible_text(texto)
           print("EL CAMPO SELECCIONADO {}".format(texto))
           time.sleep(Tiem)
           return Tiem
        except TimeoutException as ex:
           print(ex.msg)
           print("EL ELEMENTO NO  ESTA DISPONIBLE" + xpath)

#EN ESTA FUNCION ESTAMOS VALIDADDO EL TIPO DE ELEMENTO QUE SELECCIONAMOS, BIEN SEA EL XPATH POR INDEX, TEXT O VALUE (sepase que index es = a ser llamado con numeor [0,1,2,3,4,5 etc])
    def Select_Xpath_Type(self, xpath,tipo,dato, Tiem):
        try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            valor = self.driver.find_element(By.XPATH, xpath)
            valor = Select(valor)
            print("EL VALOR CAPTURADO ES:"+tipo)
            if(tipo=="text"):
                valor.select_by_visible_text(dato)
                print("AQUI SELECCIONAMOS EL CAMPO ->"+dato,"CON EL TIPO: ->"+tipo)
            elif(tipo=="value"):
                valor.select_by_value(dato)
                print("AQUI SELECCIONAMOS EL CAMPO ->"+dato,"CON EL TIPO: ->"+tipo)
            elif(tipo=="index"):
                valor.select_by_index(dato)
                print("AQUI SELECCIONAMOS EL CAMPO ->"+dato,"CON EL TIPO: ->"+tipo)
                print("EL CAMPO SELECCIONADO {}".format(dato))
            time.sleep(Tiem)
            return Tiem
        except TimeoutException as ex:
            print(ex.msg)
            print("EL ELEMENTO NO  ESTA DISPONIBLE" + xpath)

#AQUI HACEMOS EL UPLOAD, (CARGA DE IMAGENES)
    def Upload_Xpath (self, xpath,ruta,Tiem):
        try:
           valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,xpath)))
           valor=self.driver.find_element(By.XPATH,xpath)
           valor.send_keys(ruta)
           print("SE CARGA IMAGEN DE LA RUTA{}".format(xpath))
           time.sleep(Tiem)
           return Tiem
        except TimeoutException as ex:
           print(ex.msg)
           print("EL ELEMENTO NO  ESTA DISPONIBLE" + xpath)

#AQUI HACEMOS LA FUNCION CHECK.
    def check_Xpath(self, xpath, Tiem):
        try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            valor = self.driver.find_element(By.XPATH, xpath)
            valor.click()
            print("AQUI ESTAMOS DANDO CLICH AL CHECK {}".format(xpath))
            print("PRUEBA OK")
            time.sleep(Tiem)
            return Tiem
        except TimeoutException as ex:
            print(ex.msg)
            print("EL ELEMENTO NO  ESTA DISPONIBLE" + xpath)

# AQUI HACEMOS LA FUNCION SELECCIONANDO VARIOS CHEKS
    def check_Xpath_Multiples(self ,Tiem,*args):
        try:
            for num in args:
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, num)))
                valor = self.driver.find_element(By.XPATH, num)
                valor.click()
                print("AQUI ESTAMOS DANDO CLICH AL CHECK {}".format(num))
                print("PRUEBA OK")
                time.sleep(Tiem)
                return Tiem
        except TimeoutException as ex:
            for num in args:
                print(ex.msg)
                print("EL ELEMENTO NO  ESTA DISPONIBLE" + num)

#AQUI OPTIMIZAMOS EL CODIGO, VALIDANDO EL XPATH O EL ID, HACIENDO MAS EFECTIVO EL CODIGO AL MOMENTO DE LA BUSQUEDA
    def texto_Mixto_validado(self,tipo,selector,texto,Tiem):
        if(tipo=="xpath"):
            try:
               valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,selector)))
               valor=self.driver.find_element(By.XPATH,selector)
               valor.clear()
               valor.send_keys(texto)
               print("Escribiendo por -> "+tipo+" <- el valor: "+texto)
               time.sleep(Tiem)
               return Tiem

            except TimeoutException as ex:
               print(ex.msg)
               print("EL ELEMENTO  NO  ESTA DISPONIBLE" + selector)
        elif(tipo=="id"):
            try:
               valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,selector)))
               valor=self.driver.find_element(By.ID,selector)
               valor.clear()
               valor.send_keys(texto)
               print("Escribiendo por -> " + tipo + " <- el valor: " + texto)
               time.sleep(Tiem)
               return Tiem

            except TimeoutException as ex:
               print(ex.msg)
               print("EL ELEMENTO  NO  ESTA DISPONIBLE" + selector)

# AQUI EL TEXTO EXISTE PARA VALIDAR LA FUNCION SI EXISTE O NO LO QUE ESTA EN LA BASE DE DATOS EXCEL
    def Existe(self, tipo, selector, tiempo):
        if (tipo == "xpath"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element (By.XPATH,selector)
                print("El elemento  {} -> existe ".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return "No Existe"
        elif (tipo == "id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element (By.ID,selector)
                print("El elemento  {} -> existe ".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return "No Existe"

#FUNCION DOBLE CLICK MEJORADO VALIDADO
    def Mouse_Doble(self,tipo,selector,Tiem):
        if(tipo=="xpath"):
            try:
               valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,selector)))
               valor=self.driver.find_element(By.XPATH,selector)
               act = ActionChains(self.driver)
               act.double_click(valor).perform()
               print("dando click por -> "+tipo)
               time.sleep(Tiem)
               return Tiem
            except TimeoutException as ex:
               print(ex.msg)
               print("EL ELEMENTO diasSelect NO  ESTA DISPONIBLE" + selector)
        elif(tipo=="id"):
            try:
               valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,selector)))
               valor=self.driver.find_element(By.ID,selector)
               act = ActionChains(self.driver)
               act.double_click(valor).perform()
               print("dando click por -> " + tipo )
               time.sleep(Tiem)
               return Tiem
            except TimeoutException as ex:
               print(ex.msg)
               print("EL ELEMENTO diasSelect NO  ESTA DISPONIBLE" + selector)

#FUNCION DRAG DROP (ARRASTRAR ELEMENTOS CON EL MOUSE DE UN PUNTO A OTRO)
    def Mouse_DragDrop(self,tipo,selector1,selector2,Tiem):
        if(tipo=="xpath"):
            try:
               valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,selector1)))
               valor=self.driver.find_element(By.XPATH,selector1)
               valor2 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, selector2)))#VALOR DOS ES EL ELEMENTO DE DESTINO (A DONDE SERA ARRASTRADO)
               valor2 = self.driver.find_element(By.XPATH, selector2)
               act = ActionChains(self.driver)
               act.drag_and_drop(valor,valor2).perform()
               print("SE SOLTO EL ELEMENTO -> "+tipo)
               time.sleep(Tiem)
               return Tiem
            except TimeoutException as ex:
               print(ex.msg)
               print("EL ELEMENTO  NO  ESTA DISPONIBLE" + tipo)
        elif(tipo=="id"):
            try:
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, selector1)))
                valor = self.driver.find_element(By.ID, selector1)
                valor2 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, selector2)))  # VALOR DOS ES EL ELEMENTO DE DESTINO (A DONDE SERA ARRASTRADO)
                valor2 = self.driver.find_element(By.ID, selector2)
                act = ActionChains(self.driver)
                act.drag_and_drop(valor, valor2).perform()
                print("SE SOLTO EL ELEMENTO -> " + tipo)
                time.sleep(Tiem)
                return Tiem
            except TimeoutException as ex:
                print(ex.msg)
                print("EL ELEMENTO  NO ESTA DISPONIBLE" + tipo)

#FUNCION DRAG DROP CON COORDENADAS XY  (ARRASTRAR ELEMENTOS CON EL MOUSE DE UN PUNTO A OTRO)
    def Mouse_DragDrop_XY(self,tipo,selector,x,y,Tiem):
        if(tipo=="xpath"):
            try:
               self.driver.switch_to.frame(0)
               valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,selector)))
               valor=self.driver.find_element(By.XPATH,selector)
               act = ActionChains(self.driver)
               act.drag_and_drop_by_offset(valor,x,y).perform()
               print("SE SOLTO EL ELEMENTO -> "+tipo)
               time.sleep(Tiem)
               return Tiem
            except TimeoutException as ex:
               print(ex.msg)
               print("EL ELEMENTO  NO  ESTA DISPONIBLE" + tipo)
        elif(tipo=="id"):
            try:
                self.driver.switch_to.frame(0)
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, selector)))
                valor = self.driver.find_element(By.ID, selector)
                act = ActionChains(self.driver)
                act.drag_and_drop_by_offset(valor, x, y).perform()
                print("Se solto el elemento {}".format(selector))
                time.sleep(Tiem)
                return Tiem
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("EL ELEMENTO  NO ESTA DISPONIBLE" + tipo)

#FUNCION DAR CLICK CON COORDENADAS XY  (TOMANDO COMO PUNTO CERO EL XPATH O ID QUE SELECCIONEMOS )
    def Mouse_DragDrop_XY(self,tipo,selector,x,y,Tiem):
        if(tipo=="xpath"):
            try:
               #self.driver.switch_to.frame(0)    #solo habilitamos si  el boton a hacer click esta en un iframe
               valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,selector)))
               valor=self.driver.find_element(By.XPATH,selector)
               act = ActionChains(self.driver)
               act.drag_and_drop_by_offset(valor,x,y).click().perform()
               print("Click al elemento{} coordenada {}, {}".format(selector, x, y))
               time.sleep(Tiem)
               return Tiem
            except TimeoutException as ex:
               print(ex.msg)
               print("EL ELEMENTO  NO  ESTA DISPONIBLE" + tipo)
        elif(tipo=="id"):
            try:
                #self.driver.switch_to.frame(0)    #solo habilitamos si  el boton a hacer click esta en un iframe
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, selector)))
                valor = self.driver.find_element(By.ID, selector)
                act = ActionChains(self.driver)
                act.drag_and_drop_by_offset(valor, x, y).perform()
                print("Click al elemento{} coordenada {}, {}".format(selector, x, y))
                time.sleep(Tiem)
                return Tiem
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("EL ELEMENTO  NO ESTA DISPONIBLE" + tipo)

# FUNCION DAR CLICK DERECHO
    def Mouse_Derecho(self, tipo, selector, tiempo=.2):
        if (tipo == "xpath"):
            try:
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, selector)))
                valor = self.driver.find_element(By.XPATH, selector)
                act = ActionChains(self.driver)
                act.context_click(valor).perform()
                print("ClickDerecho en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, selector)))
                valor = self.driver.find_element(By.ID, selector)
                act = ActionChains(self.driver)
                act.context_click(valor).perform()
                print("ClickDerecho en {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t

