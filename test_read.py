import pytest
import time
import os
from login_page import LoginPage

def test_HU03_buscar_empleado(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    login = LoginPage(driver)
    login.ingresar_credenciales("Admin", "admin123")
    
    # Acción CRUD: Read (Search)
    login.buscar_empleado("Jose")
    
    time.sleep(4)
    if not os.path.exists('reports'): os.makedirs('reports')
    driver.save_screenshot("reports/HU03_Busqueda_Exitoso.png")
    
    # Validamos que aparezca en los resultados de la tabla
    assert "Jose" in driver.page_source