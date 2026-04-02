import pytest
import time
from login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

NOMBRE_BASE = f"Full{str(int(time.time()))[-3:]}"

def test_full_cycle(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    login = LoginPage(driver)
    login.ingresar_credenciales("Admin", "admin123")
    
    # 1. CREATE
    login.crear_empleado(NOMBRE_BASE, "Master")
    
    # 2. READ (SEARCH)
    login.buscar_empleado(NOMBRE_BASE)
    # Esperamos a que el nombre aparezca en el texto del body
    WebDriverWait(driver, 20).until(lambda d: NOMBRE_BASE in d.page_source)
    assert NOMBRE_BASE in driver.page_source
    
    # 3. UPDATE
    login.editar_empleado(NOMBRE_BASE + "Mod")
    WebDriverWait(driver, 30).until(EC.url_contains("viewPersonalDetails"))
    
    # 4. DELETE
    login.buscar_empleado(NOMBRE_BASE + "Mod")
    login.eliminar_empleado()
    
    # Esperamos a que el texto de "No hay registros" aparezca
    WebDriverWait(driver, 20).until(
        lambda d: "No Records Found" in d.find_element(By.TAG_NAME, "body").text
    )
    assert "No Records Found" in driver.page_source