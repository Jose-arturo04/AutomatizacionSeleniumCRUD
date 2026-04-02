import pytest
import time
import os
from login_page import LoginPage

def test_HU03_buscar_empleado(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    login = LoginPage(driver)
    login.ingresar_credenciales("Admin", "admin123")
    login.buscar_empleado("Jose") # Busca al que creamos antes
    time.sleep(3)
    driver.save_screenshot("reports/HU03_Read.png")
    assert "Jose" in driver.page_source

def test_HU04_editar_empleado(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    login = LoginPage(driver)
    login.ingresar_credenciales("Admin", "admin123")
    login.buscar_empleado("Jose")
    login.editar_empleado("Jose Editado") # Cambia el nombre
    time.sleep(5)
    driver.save_screenshot("reports/HU04_Update.png")
    assert "viewPersonalDetails" in driver.current_url

def test_HU05_eliminar_empleado(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    login = LoginPage(driver)
    login.ingresar_credenciales("Admin", "admin123")
    login.buscar_empleado("Jose Editado")
    login.eliminar_empleado() # ¡Adiós Jose!
    time.sleep(3)
    driver.save_screenshot("reports/HU05_Delete.png")
    # Si sale el mensaje de "No Records Found" o éxito, pasó
    assert "No Records Found" in driver.page_source or "Successfully Deleted" in driver.page_source