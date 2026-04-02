import pytest
import time
import os
from login_page import LoginPage
from selenium.webdriver.common.by import By

def test_HU03_buscar_empleado(driver):
    """Escenario: Visualizar y buscar un registro existente (Read)"""
    driver.get("https://opensource-demo.orangehrmlive.com/")
    login = LoginPage(driver)
    
    # 1. Login
    login.ingresar_credenciales("Admin", "admin123")
    
    # 2. Acción CRUD: Read (Search)
    # Buscamos a "Jose" (asegúrate de haber corrido el test de Create antes)
    login.buscar_empleado("Arturo")
    
    # 3. Pausa para que la tabla refresque los resultados
    time.sleep(5)
    
    # 4. Evidencia
    if not os.path.exists('reports'): 
        os.makedirs('reports')
    driver.save_screenshot("reports/HU03_Busqueda_Exitoso.png")
    
    # 5. Validación: Buscamos el texto específicamente en la tabla de resultados
    # Esto es mucho más seguro que buscar en todo el 'page_source'
    resultados = driver.find_elements(By.XPATH, "//*[contains(text(), 'Jose')]")
    
    assert len(resultados) > 0, "Error: El empleado 'Jose' no apareció en los resultados de búsqueda."